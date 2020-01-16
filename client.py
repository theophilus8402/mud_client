
import asyncio
import functools
import logging
import readline
import sys
import threading

from contextlib import suppress

import achaea.tab_complete
from achaea import Achaea
from achaea.client import send, client
from multi_queue import MultiQueue
from telnet_manager import handle_telnet, strip_ansi, gmcp_queue


async def handle_input(mud_client):

    # note!  This is more on the "client" side
    # in that I should be handling aliases and what not

    loop = asyncio.get_event_loop()
    while True:
        data = await loop.run_in_executor(None, input)

        # check to see if the user just hit enter
        # if so, send the last command instead
        if data == "\n":
            data = client.last_command

        client.main_log(data, "user_input")
        client.last_command = data

        # check if we should break out of the loop
        if data == "qdq":
            break

        # handle user input
        for cmd in data.split(";"):
            if not mud_client.handle_aliases(cmd):
                send(cmd)
            # else assume msgs are sent as needed


def reader(file_handle, mud_client, queue):

    # note!  This is more on the "client" side
    # in that I should be handling aliases and what not
    # before putting something in the queue
    # I should also exchange the queue.put_nowait for "send"
    # to send stuff to the server

    data = file_handle.readline()

    # check to see if the user just hit enter
    # if so, send the last command instead
    if data == "\n":
        data = client.last_command

    client.last_command = data

    # handle user input
    for cmd in data.split(";"):
        if not mud_client.handle_aliases(cmd):
            send(cmd)
        # else assume msgs are sent as needed

    client.main_log(data, "user_input")


async def handle_from_server_queue(from_server_queue, mud_client):

    while True:
        data = await from_server_queue.get()
        client.current_chunk = data
        output = []
        for line in data.split("\n"):

            client.modified_current_line = None
            client.current_line = line
            stripped_line = strip_ansi(line)
            mud_client.handle_triggers(stripped_line.strip())

            client.main_log(line, "server_text")

            if client.modified_current_line == None:
                output.append(line)
            elif client.modified_current_line:
                output.append(client.modified_current_line)
            # if client.modified_current_line is not None but "", it's meant to be deleted
        print("\n".join(output).strip(), file=client.current_out_handle, flush=True)
        from_server_queue.task_done()


async def handle_gmcp_queue(gmcp_queue, mud_client):

    while True:
        #print("handle_gmcp_queue: awaiting gmcp_data")
        #print(f"gmcp_queue id: {id(gmcp_queue)}")
        gmcp_type, gmcp_data = await gmcp_queue.get()

        #print(f"handle_gmcp_queue: gmcp_data: {gmcp_data}")
        client.main_log(gmcp_data, "gmcp_data")

        #try:
        #    mud_client.handle_gmcp(gmcp_type, gmcp_data)
        #except Exception as e:
        #    printf(f"ERROR! {e}")

        gmcp_queue.task_done()
        #print(f"handle_gmcp_queue: done with: {gmcp_data}")


def start_tab_complete():
    from achaea.tab_complete import SimpleCompleter
    from achaea.variables import v
    import readline

    # set the completer function
    print(f"players: {id(v.players_in_room)}")
    print(f"mobs: {id(v.mobs_in_room)}")
    print(f"enemies: {id(v.enemies)}")
    simple_completer = SimpleCompleter(v.players_in_room,
                                       v.mobs_in_room,
                                       v.enemies)
    print("Setting tab completer")
    readline.set_completer(simple_completer.complete)

    # use the tab key for completion
    readline.parse_and_bind("tab: complete")


def main():

    msg_queue = client.send_queue

    event_loop = asyncio.get_event_loop()

    mud_client = Achaea()

    # start tab completer
    start_tab_complete()

    # handle reading stdin
    #asyncio.ensure_future(handle_input(mud_client))
    event_loop.add_reader(sys.stdin, reader, sys.stdin, mud_client, msg_queue)

    host = "127.0.0.1"
    port = 8888

    client.from_server_queue = MultiQueue()
    asyncio.ensure_future(handle_telnet(host, port,
                         client.from_server_queue, msg_queue))

    server_reader = client.from_server_queue.get_receiver("main")
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

        client.from_server_queue.remove_receiver("main")

        # let the client close up connections/file handles
        client.close()

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

