
import asyncio
import functools
import logging
import readline
import sys

from contextlib import suppress

from achaea import Achaea
from achaea.client import send, client
from multi_queue import MultiQueue
from telnet_manager import handle_telnet, strip_ansi, gmcp_queue

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

            if client.modified_current_line == None:
                output.append(line)
            elif client.modified_current_line:
                output.append(client.modified_current_line)
            # if client.modified_current_line is not None but "", it's meant to be deleted
        print("\n".join(output).strip(), file=client.current_out_handle, flush=True)
        from_server_queue.task_done()


async def handle_gmcp_queue(gmcp_queue, mud_client):

    while True:
        gmcp_type, gmcp_data = await gmcp_queue.get()

        mud_client.handle_gmcp(gmcp_type, gmcp_data)

        gmcp_queue.task_done()


if __name__ == "__main__":

    #msg_queue = asyncio.Queue()
    msg_queue = client.send_queue

    event_loop = asyncio.get_event_loop()

    mud_client = Achaea()

    # handle reading stdin
    event_loop.add_reader(sys.stdin, reader, sys.stdin, mud_client, msg_queue)

    #host = "192.168.1.156"
    host = "localhost"
    port = 4000
    #host = "achaea.com"
    #port = 23

    client.from_server_queue = MultiQueue()
    asyncio.ensure_future(handle_telnet(host, port, client.from_server_queue, msg_queue))

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
        pass

    finally:
        log.debug('closing event loop')

        client.from_server_queue.remove_receiver("main")

        # let the client close up connections/file handles
        client.close()

        # Let's also cancel all running tasks:
        pending = asyncio.Task.all_tasks()
        for task in pending:
            task.cancel()
            # Now we should await task to execute it's cancellation.
            # Cancelled task raises asyncio.CancelledError that we can suppress:
            with suppress(asyncio.CancelledError):
                event_loop.run_until_complete(task)

        event_loop.close()
