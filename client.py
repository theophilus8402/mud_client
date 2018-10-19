
import asyncio
import functools
import logging
import sys

from contextlib import suppress

from achaea import Achaea
from achaea.client import send
from telnet_manager import handle_telnet

def reader(file_handle, client, queue):

    # note!  This is more on the "client" side
    # in that I should be handling aliases and what not
    # before putting something in the queue
    # I should also exchange the queue.put_nowait for "send"
    # to send stuff to the server

    data = file_handle.readline()
    if not client.handle_aliases(data):
        send(data)
    # else assume msgs are sent as needed


async def handle_from_server_queue(from_server_queue):

    while True:
        data = await from_server_queue.get()
        print(data)
        from_server_queue.task_done()


if __name__ == "__main__":

    msg_queue = asyncio.Queue()

    event_loop = asyncio.get_event_loop()

    client = Achaea()

    # handle reading stdin
    event_loop.add_reader(sys.stdin, reader, sys.stdin, client, msg_queue)

    #host = "127.0.0.1"
    #port = 8888
    host = "achaea.com"
    port = 23

    from_server_queue = asyncio.Queue()
    asyncio.ensure_future(handle_from_server_queue(from_server_queue))
    asyncio.ensure_future(handle_telnet(host, port, from_server_queue, msg_queue))

    log = logging.getLogger('EchoClient')
    logging.basicConfig(level=logging.DEBUG)

    log.debug('waiting for client to complete')
    try:

        event_loop.run_forever()

    finally:
        log.debug('closing event loop')

        # Let's also cancel all running tasks:
        pending = asyncio.Task.all_tasks()
        for task in pending:
            task.cancel()
            # Now we should await task to execute it's cancellation.
            # Cancelled task raises asyncio.CancelledError that we can suppress:
            with suppress(asyncio.CancelledError):
                event_loop.run_until_complete(task)

        event_loop.close()

