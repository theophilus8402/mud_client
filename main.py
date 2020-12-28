import asyncio
import json
import logging
import signal
import sys
import traceback
from contextlib import suppress

from prompt_toolkit.application import Application
from prompt_toolkit.layout.layout import Layout

import ui.core
from achaea import initialize_logging
from achaea.afflictions import summarize_afflictions
from achaea.state import s
from achaea.tab_complete import TargetCompleter
from client import Brain, c, send
from multi_queue import MultiQueue
from telnet_manager import gmcp_queue, handle_telnet, strip_ansi

initialize_logging()


async def handle_input():

    # Attach accept handler to the input field. We do this by assigning the
    # handler to the `TextArea` that we created earlier. it is also possible to
    # pass it to the constructor of `TextArea`.
    # NOTE: It's better to assign an `accept_handler`, rather then adding a
    #       custom ENTER key binding. This will automatically reset the input
    #       field and add the strings to the history.
    def accept(input_buffer):

        data = input_buffer.text

        # check to see if the user just hit enter
        # if so, send the last command instead
        if data == "":
            data = c.last_command

        c.main_log(data, "user_input")
        c.last_command = data

        # handle user input
        for cmd in data.split(";"):
            if not c.handle_aliases(cmd):
                send(cmd)
            # else assume msgs are sent as needed

        # everything has been queued in c.to_send
        # use c.send_flush() to actually send it
        c.send_flush()

    ui.core.input_field.accept_handler = accept
    ui.core.input_field.completer = TargetCompleter(s)

    application = Application(
        layout=Layout(ui.core.container, focused_element=ui.core.input_field),
        key_bindings=ui.core.kb,
        style=ui.core.style,
        mouse_support=True,
        full_screen=True,
    )

    await application.run_async(set_exception_handler=True)


async def handle_from_server_queue(from_server_queue):

    while True:
        data = await from_server_queue.get()
        c.current_chunk = data
        c.main_log(data, "server_text")
        output = []
        try:
            for line in data.split("\n"):

                c.modified_current_line = None
                c.current_line = line
                stripped_line = strip_ansi(line)
                c.handle_triggers(stripped_line.strip())

                if c._delete_line is True or line in c._delete_lines:
                    # "delete" the line by not appending it to the output
                    c._delete_line = False
                elif c.modified_current_line is None:
                    output.append(line)
                elif c.modified_current_line != "":
                    output.append(c.modified_current_line)

            # clear the delete_lines
            c._delete_lines.clear()

            c.processed_tekura_combo = False

            # some triggers have probably queued stuff to send, so send it
            if c.to_send:
                c.send_flush()
            c.echo("\n".join(output).strip())
            affs = summarize_afflictions()
            if affs:
                c.echo(f"Affs: {' '.join(affs)}")

            from_server_queue.task_done()

        except Exception:
            traceback.print_exc(file=sys.stdout)


async def handle_gmcp_queue(gmcp_queue):

    while True:
        gmcp_type, gmcp_data = await gmcp_queue.get()

        gmcp_msg = json.dumps({"type": gmcp_type, "data": gmcp_data})
        c.main_log(gmcp_msg, "gmcp_data")

        try:
            c.handle_gmcp(gmcp_type, gmcp_data)
        except Exception as e:
            print(f"handle_gmcp_queue ERROR! {e}")

        gmcp_queue.task_done()


async def shutdown(signal, loop, shutdown_event):
    print("In shutdown")
    logger = logging.getLogger("achaea")
    logger.info(f"Received exit signal {signal.name}...")

    shutdown_event.set()

    # c.from_server_queue.remove_receiver("main")

    # let the client close up connections/file handles
    c.close()

    # Let's also cancel all running tasks:
    event_loop = asyncio.get_event_loop()
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]

    for task in tasks:
        task.cancel()

    logger.info("Cancelling outstanding tasks")
    await asyncio.gather(*tasks, return_exceptions=True)
    logger.info("Stopping loop")
    loop.stop()


def main(shutdown_event):

    event_loop = asyncio.get_event_loop()

    host = "127.0.0.1"
    port = 8888

    c.from_server_queue = MultiQueue()

    server_reader = c.from_server_queue.get_receiver("main")
    asyncio.ensure_future(handle_from_server_queue(server_reader))

    # handle gmcp data
    asyncio.ensure_future(handle_gmcp_queue(gmcp_queue))

    log = logging.getLogger("achaea")

    log.debug("waiting for client to complete")

    try:
        event_loop.create_task(
            handle_telnet(host, port, c.from_server_queue, c.send_queue)
        )
    except asyncio.CancelledError:
        log.info("Connection with the server is still running!")

    # handle reading stdin
    try:
        event_loop.run_until_complete(handle_input())
    except asyncio.CancelledError:
        print("main:handle_input cancelled")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    shutdown_event = asyncio.Event()

    signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT)
    for sig in signals:
        loop.add_signal_handler(
            sig,
            lambda sig=sig: asyncio.ensure_future(shutdown(sig, loop, shutdown_event)),
        )
    try:
        main(shutdown_event)
    finally:
        logger = logging.getLogger("achaea")
        logger.info("Successfully closed mud client.")
