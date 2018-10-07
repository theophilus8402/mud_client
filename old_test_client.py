
import asyncio
import functools
import logging
import sys

from contextlib import suppress

from telnet_manager import telnet_connect, mud_encoding, handle_telnet, strip_ansi

async def send_to_server(transport, msg_queue):
    while True:
        data = await msg_queue.get()
        transport.write(data.encode())
        msg_queue.task_done()


def reader(file_handle, queue):

    # note!  This is more on the "client" side
    # in that I should be handling aliases and what not
    # before putting something in the queue
    # I should also exchange the queue.put_nowait for "send"
    # to send stuff to the server

    data = file_handle.readline()
    queue.put_nowait(data)


class ConnectionManager(asyncio.Protocol):

    def __init__(self, future, msg_queue):
        super().__init__()
        self.msg_queue = msg_queue
        self.log = logging.getLogger('EchoClient')
        self.f = future

    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.log.debug(
            'connecting to {} port {}'.format(*self.address)
        )
        asyncio.ensure_future(send_to_server(transport, self.msg_queue))

    def data_received(self, data):
        #self.log.debug('received {!r}'.format(data))
        data = check_for_telnet_cmds(data)
        #data = strip_ansi(data.decode(mud_encoding))
        print(data)

    def eof_received(self):
        self.log.debug('received EOF')
        self.transport.close()
        if not self.f.done():
            self.f.set_result(True)

    def connection_lost(self, exc):
        self.log.debug('server closed connection')
        self.transport.close()
        if not self.f.done():
            self.f.set_result(True)
        super().connection_lost(exc)


async def handle_from_server_queue(from_server_queue):

    while True:
        data = await from_server_queue.get()
        print(data)
        from_server_queue.task_done()


if __name__ == "__main__":


    client_completed = asyncio.Future()

    msg_queue = asyncio.Queue()

    """
    client_factory = functools.partial(
        ConnectionManager,
        future=client_completed,
        msg_queue=msg_queue,
    )
    """

    event_loop = asyncio.get_event_loop()

    event_loop.add_reader(sys.stdin, reader, sys.stdin, msg_queue)

    #host = "127.0.0.1"
    #port = 8888
    host = "achaea.com"
    port = 23
    #telnet_socket = telnet_connect(host, port)

    """
    factory_coroutine = event_loop.create_connection(
        client_factory,
        #sock=telnet_socket.sock,
        host,
        port,
    )
    """
    from_server_queue = asyncio.Queue()
    asyncio.ensure_future(handle_from_server_queue(from_server_queue))
    asyncio.ensure_future(handle_telnet(host, port, from_server_queue, msg_queue))

    log = logging.getLogger('EchoClient')
    logging.basicConfig(level=logging.DEBUG)

    log.debug('waiting for client to complete')
    try:
        #event_loop.run_until_complete(factory_coroutine)
        #event_loop.run_until_complete(client_completed)
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

