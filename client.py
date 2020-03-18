
import asyncio
import functools
import json
import logging
import readline
import sys

from contextlib import suppress

from achaea.tab_complete import TargetCompleter
from achaea import Achaea
from achaea.client import send, c
from achaea.state import s
from achaea.afflictions import summarize_afflictions
from multi_queue import MultiQueue
from telnet_manager import handle_telnet, strip_ansi, gmcp_queue

from prompt_toolkit.shortcuts import PromptSession


async def handle_input(mud_client):

    # note!  This is more on the "client" side
    # in that I should be handling aliases and what not

    session = PromptSession("", reserve_space_for_menu=3)

    completer = TargetCompleter(s)
    # Run echo loop. Read text from stdin, and reply it back.
    while True:
        try:
            data = await session.prompt_async(completer=completer)
        except (EOFError, KeyboardInterrupt):
            return

        # check to see if the user just hit enter
        # if so, send the last command instead
        if data == "":
            data = c.last_command

        c.main_log(data, "user_input")
        c.last_command = data

        # check if we should break out of the loop
        if data == "qdq":
            break

        # handle user input
        #c.echo(f"cmd: {data}")
        for cmd in data.split(";"):
            if not mud_client.handle_aliases(cmd):
                send(cmd)
            # else assume msgs are sent as needed

        # everything has been queued in c.to_send
        # use c.send_flush() to actually send it
        c.send_flush()


async def handle_from_server_queue(from_server_queue, mud_client):

    while True:
        data = await from_server_queue.get()
        c.current_chunk = data
        output = []
        try:
            for line in data.split("\n"):

                c.modified_current_line = None
                c.current_line = line
                stripped_line = strip_ansi(line)
                mud_client.handle_triggers(stripped_line.strip())

                c.main_log(line, "server_text")

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
            print("\n".join(output).strip(), file=c.current_out_handle, flush=True)
            summarize_afflictions()
            from_server_queue.task_done()
        except Exception as e:
            print(f"Trouble with triggers: {e}")


async def handle_gmcp_queue(gmcp_queue, mud_client):

    while True:
        gmcp_type, gmcp_data = await gmcp_queue.get()

        gmcp_msg = json.dumps({"type": gmcp_type, "data": gmcp_data})
        c.main_log(gmcp_msg, "gmcp_data")

        try:
            mud_client.handle_gmcp(gmcp_type, gmcp_data)
        except Exception as e:
            printf(f"ERROR! {e}")

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

    log = logging.getLogger('EchoClient')
    logging.basicConfig(level=logging.DEBUG)

    log.debug('waiting for client to complete')
    try:
        event_loop.run_forever()
    except KeyboardInterrupt:
        print("main: Got a Keyboard Interrupt!!")
    except Exception as e:
        print(f"Other exception! {e}")
    finally:
        log = logging.getLogger('EchoClient')
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

