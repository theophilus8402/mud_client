
import asyncio

from functools import partial

class Client():

    def __init__(self):
        self.send_queue = asyncio.Queue()
        #self.writer = None
        self.line = None
        self.delete_line = False

client = Client()

async def read_queue(queue):

    data = None

    while data != "":
        data = await queue.get()
        print("Got data: {}".format(data))


def _send(client, msg):
    client.send_queue.put_nowait(msg)

send = partial(_send, client)


def _echo(client, msg):
    print(msg)

def _delete_line(client):
    pass

def _redirect_line(client, file_name):
    pass


