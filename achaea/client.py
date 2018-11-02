
import asyncio
import re
import sys

from functools import partial

class Client():

    def __init__(self):
        self.send_queue = asyncio.Queue()
        #self.writer = None
        self.line = None
        self.delete_line = False
        self.handles = {}
        self.open_handle("default", "achaea.log")
        self.default_out_handle = self.handles["default"]
        self.current_out_handle = self.handles["default"]
        self.last_command = ""

    def open_handle(self, name, file_path):
        self.handles[name] = open(file_path, "w")

    def close(self):
        for handle in self.handles.values():
            handle.close()

client = Client()

async def read_queue(queue):

    data = None

    while data != "":
        data = await queue.get()
        print("Got data: {}".format(data))


def _send(client, msg):
    if not msg.endswith("\n"):
        msg = "{}\n".format(msg)
    client.send_queue.put_nowait(msg)

send = partial(_send, client)


def _echo(client, msg):
    print(msg)

def _delete_line(client):
    pass

def _redirect_line(client, file_name):
    pass


# help_info[group_name] = [(pattern, desc)]
help_info = {}

# aliases.append((compiled_pattern, function))
aliases = []
triggers = []

def add_aliases(group_name, new_aliases):

    global help_info
    global aliases

    if group_name in help_info.keys():
        print("{} already exists!", file=client.current_out_handle, flush=True)
        return False

    help_info[group_name] = []
    for pattern, desc, func in new_aliases:
        aliases.append((re.compile(pattern), func))
        help_info[group_name].append((pattern, desc))
    return True

def add_triggers(new_triggers):

    global triggers
    return False

def show_help(alias_group):

    print("{}:".format(alias_group), file=client.current_out_handle, flush=True)
    for pattern, desc in help_info[alias_group]:
        print("{} : {}".format(pattern, desc), file=client.current_out_handle, flush=True)

base_aliases = [
    (   "#help (.*)",
        "show help",
        lambda m: show_help(m[0])
    ),
]
add_aliases("base", base_aliases)

