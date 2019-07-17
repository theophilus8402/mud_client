
import asyncio
import contextlib
import sys


class ServerConnectProtocol(asyncio.Protocol):

    def __init__(self, from_server_queue, to_server_queue):
        self.transport = None
        self.from_server_queue = from_server_queue
        self.to_server_queue = to_server_queue

    def connection_made(self, transport):
        self.transport = transport
        self.send_to_server_task = asyncio.ensure_future(self.send_to_server())

    async def send_to_server(self):
        while True:
            msg = await self.to_server_queue.get()
            try:
                self.transport.write(msg)
            except e:
                print(f"Egads!  Couldn't send: {msg}")
                print(e)

    def data_received(self, data):
        #print("Received from server:", data.decode())
        self.from_server_queue.put_nowait(data)

    def connection_lost(self, exc):
        # The socket has been closed
        print("Closed the server connection socket!")


class LocalServerProtocol(asyncio.Protocol):

    def __init__(self, from_server_queue, to_server_queue, connect_to_server,
                    host, host_port):
        print("creating the local server")
        self.from_server_queue = from_server_queue
        self.to_server_queue = to_server_queue
        self.connect_to_server = connect_to_server
        self.host = host
        self.host_port = host_port
        print("__init__", id(self.connect_to_server), self.connect_to_server)

    def connection_made(self, transport):
        # setup the reader for the queue
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport
        self.server_reader = asyncio.ensure_future(self.read_from_server_queue())

        print(id(self.connect_to_server), self.connect_to_server)
        if not self.connect_to_server.done():
            task = asyncio.create_task(
                    self.start_server_connection())
            self.connect_to_server.set_result(task)
            print(id(self.connect_to_server), self.connect_to_server)

    async def start_server_connection(self):
        print("Connecting to remote server...")
        loop = asyncio.get_running_loop()

        self.server_transport, self.server_protocol = await loop.create_connection(
            lambda: ServerConnectProtocol(
                        self.from_server_queue,
                        self.to_server_queue),
            self.host, self.host_port)

    def connection_lost(self, exc):
        self.server_reader.cancel()
        print("Local connection closed.")

    # read from_server_queue
    async def read_from_server_queue(self):
        while True:
            msg = await self.from_server_queue.get()
            # need to send it to the local socket
            #TODO don't print to screen, send to the socket
            print(f"trying to send: {msg}")
            self.transport.write(msg)

    def data_received(self, data):
        self.to_server_queue.put_nowait(data)
        # add data to the to_server_queue


async def main(bind_address, port, host, host_port):
    event_loop = asyncio.get_event_loop()

    from_server_queue = asyncio.Queue()
    to_server_queue = asyncio.Queue()

    connect_to_server = event_loop.create_future()
    server = await event_loop.create_server(
        lambda: LocalServerProtocol(from_server_queue, to_server_queue,
                                    connect_to_server, host, host_port),
        bind_address, port)

    async with server:
        await server.serve_forever()

    for task in asyncio.Task.all_tasks():
        task.cancel()

        with contextlib.suppress(asyncio.CancelledError):
            event_loop.run_until_complete(task)

    event_loop.close()


def parse_address(address):

    pieces = address.split(":")

    # if bind_address is not specified, prepend the default
    if len(pieces) == 3:
        pieces.insert(0, "127.0.0.1")

    if len(pieces) == 4:
        bind_address = pieces[0]
        port = pieces[1]
        host = pieces[2]
        host_port = pieces[3]
        
    else:
        print("Ack!  You did not provide an appropriate address!")
        print("It should look like this: [bind_address]:port:host:host_port")
        sys.exit(1)

    return bind_address, port, host, host_port


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description="Proxy stuff!")
    parser.add_argument("-L", metavar="address",
                        help="[bind_address]:port:host:hostport")
    args = parser.parse_args()

    if args.L:
        bind_address, port, host, host_port = parse_address(args.L)
    else:
        bind_address, port, host, host_port = parse_address("127.0.0.1:8888:127.0.01:9999")

    asyncio.run(main(bind_address, port, host, host_port))

