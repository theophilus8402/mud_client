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
from client import c, send
from multi_queue import MultiQueue
from telnet_manager import gmcp_queue, handle_telnet, strip_ansi


async def start_application(tab_completer):

    ui.core.input_field.accept_handler = c.handle_input
    ui.core.input_field.completer = tab_completer

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
                stripped_line = strip_ansi(line).rstrip("\r")
                c.handle_triggers(stripped_line)

                # c.echo(f"stripped_line: '{ascii(stripped_line)}'")
                # c.echo(f"dl: {c._delete_lines}")
                if c._delete_line is True or stripped_line in c._delete_lines:
                    # "delete" the line by not appending it to the output
                    c._delete_line = False
                elif c.modified_current_line is None:
                    output.append(line)
                elif c.modified_current_line != "":
                    output.append(c.modified_current_line)

            # clear the delete_lines
            c._delete_lines.clear()

            c.run_after_current_chunk()

            # some triggers have probably queued stuff to send, so send it
            if c.to_send:
                c.send_flush()
            c.echo("\n".join(output).strip())

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


def main(host, port, shutdown_event, mud_module):

    event_loop = asyncio.get_event_loop()

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

    tab_completer = mud_module.get_tab_completer()

    # handle reading stdin
    try:
        event_loop.run_until_complete(start_application(tab_completer))
    except asyncio.CancelledError:
        print("main:start_application cancelled")


if __name__ == "__main__":

    import argparse
    import importlib
    import json

    parser = argparse.ArgumentParser(description="Play a MUD!")
    parser.add_argument("config", help="config to point to the mud")
    args = parser.parse_args()

    with open(args.config) as f:
        config = json.load(f)

    host = config.get("proxy_ip") or config.get("ip")
    port = config.get("proxy_port") or config.get("port")

    mud_module = importlib.import_module(config.get("module"))

    loop = asyncio.get_event_loop()

    shutdown_event = asyncio.Event()

    signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT)
    for sig in signals:
        loop.add_signal_handler(
            sig,
            lambda sig=sig: asyncio.ensure_future(shutdown(sig, loop, shutdown_event)),
        )
    try:
        main(host, port, shutdown_event, mud_module)
    finally:
        logger = logging.getLogger("achaea")
        logger.info("Successfully closed mud client.")
