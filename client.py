
import achaea.mud_logging

import asyncio
import functools
import json
import logging
import readline
import sys
import traceback

from contextlib import suppress


from achaea.tab_complete import TargetCompleter
from achaea import Achaea
from achaea.client import send, c
from achaea.state import s
from achaea.afflictions import summarize_afflictions
from multi_queue import MultiQueue
from telnet_manager import handle_telnet, strip_ansi, gmcp_queue

from prompt_toolkit.application import Application
from prompt_toolkit.layout.layout import Layout

import ui.core

async def handle_input(mud_client):

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
        #c.echo(f"cmd: {data}")
        for cmd in data.split(";"):
            if not mud_client.handle_aliases(cmd):
                send(cmd)
            # else assume msgs are sent as needed

        # everything has been queued in c.to_send
        # use c.send_flush() to actually send it
        c.send_flush()


    ui.core.input_field.accept_handler = accept

    application = Application(
        layout=Layout(ui.core.container, focused_element=ui.core.input_field),
        key_bindings=ui.core.kb,
        style=ui.core.style,
        mouse_support=True,
        full_screen=True,
    )

    #completer = TargetCompleter(s)

    result = await application.run_async()
    print(f"result: {result}")


async def handle_from_server_queue(from_server_queue, mud_client):

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
                mud_client.handle_triggers(stripped_line.strip())


                if c._delete_line == True:
                    # "delete" the line by not appending it to the output
                    c._delete_line = False
                elif c.modified_current_line == None:
                    output.append(line)
                elif c.modified_current_line != "":
                    output.append(c.modified_current_line)
            # some triggers have probably queued stuff to send, so send it
            if c.to_send:
                c.send_flush()
            c.echo("\n".join(output).strip())
            affs = summarize_afflictions()
            if affs:
                c.echo(f"Affs: {' '.join(affs)}")
            from_server_queue.task_done()
        except Exception as e:
            traceback.print_exc(file=sys.stdout)


async def handle_gmcp_queue(gmcp_queue, mud_client):

    while True:
        gmcp_type, gmcp_data = await gmcp_queue.get()

        gmcp_msg = json.dumps({"type": gmcp_type, "data": gmcp_data})
        c.main_log(gmcp_msg, "gmcp_data")

        try:
            mud_client.handle_gmcp(gmcp_type, gmcp_data)
        except Exception as e:
            printf(f"handle_gmcp_queue ERROR! {e}")

        gmcp_queue.task_done()


def main():

    event_loop = asyncio.get_event_loop()

    mud_client = Achaea()

    # handle reading stdin
    asyncio.ensure_future(handle_input(mud_client))

    host = "127.0.0.1"
    port = 8888

    c.from_server_queue = MultiQueue()
    asyncio.ensure_future(handle_telnet(host, port,
                         c.from_server_queue, c.send_queue))

    server_reader = c.from_server_queue.get_receiver("main")
    asyncio.ensure_future(handle_from_server_queue(server_reader, mud_client))

    # handle gmcp data
    asyncio.ensure_future(handle_gmcp_queue(gmcp_queue, mud_client))

    log = logging.getLogger("achaea")
    #logging.basicConfig(level=logging.DEBUG)

    log.debug('waiting for client to complete')
    try:
        event_loop.run_forever()
    except KeyboardInterrupt:
        print("main: Got a Keyboard Interrupt!!")
    except Exception as e:
        print(f"Other exception! {e}")
    finally:
        log.debug('closing event loop')

        c.from_server_queue.remove_receiver("main")

        # let the client close up connections/file handles
        c.close()

        # Let's also cancel all running tasks:
        event_loop = asyncio.get_event_loop()
        pending = asyncio.Task.all_tasks()
        for task in pending:
            task.cancel()
            # Now we should await task to execute it's cancellation.
            # Cancelled task raises asyncio.CancelledError that we can suppress:
            with suppress(asyncio.CancelledError):
                event_loop.run_until_complete(task)

        event_loop.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("__main__: Got a Keyboard Interrupt!!")

