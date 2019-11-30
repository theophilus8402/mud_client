
import asyncio
import re

from collections import defaultdict
from datetime import datetime
from functools import partial

class Client():

    def __init__(self):
        self.send_queue = asyncio.Queue()
        #self.writer = None
        self.line = None
        self.delete_line = False
        self.handles = {}
        self.modified_current_line = None
        self.open_handle("default", "achaea.log")
        self.default_out_handle = self.handles["default"]
        self.current_out_handle = self.handles["default"]
        self.log = self.start_main_log()
        self.last_command = ""

    def open_handle(self, name, file_path):
        self.handles[name] = open(file_path, "w")

    def close(self):
        for handle in self.handles.values():
            handle.close()

    def start_main_log(self):
        now = datetime.now()
        log_name = f"logs/achaea/{now.strftime('%Y-%m-%d_%H:%M:%S.%f.txt')}"
        self.open_handle("main_log", log_name)
        return self.handles["main_log"]

    def main_log(self, msg, msg_type):
        print(f"{datetime.now()} //\\\\ {msg_type} //\\\\ {msg}",
                file=self.log)


client = Client()

async def read_queue(queue):

    data = None

    while data != "":
        data = await queue.get()
        print("Got data: {}".format(data))


def _send(client, msg):
    if not msg.endswith("\n"):
        msg = "{}\n".format(msg)
    client.main_log(msg.strip(), "data_sent")
    client.send_queue.put_nowait(msg)

send = partial(_send, client)


def echo(msg):
    print(msg, file=client.current_out_handle, flush=True)

def set_line(new_line):
    global client
    client.modified_current_line = new_line

def delete_line():
    set_line("")

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

def add_triggers(new_triggers, flags=0):

    global triggers

    for new_trig in new_triggers:
        add_trigger(new_trig, flags=flags)

    return True

def add_trigger(new_trigger, flags=0):

    global triggers
    pattern, action = new_trigger
    #echo("adding trigger: {}".format(pattern))
    compiled_pattern = re.compile(pattern, flags=flags)
    if pattern.startswith("^"):
        search_method = compiled_pattern.match
    else:
        search_method = compiled_pattern.search
    triggers.append((search_method, action))
    return triggers[-1]

def remove_trigger(trigger):
    global triggers
    #for trig in triggers:
    #    echo(trig)
    try:
        triggers.remove(trigger)
    except ValueError:
        echo("Trying to remove a trigger that doesn't exist!")

temp_triggers = {}

def add_temp_trigger(name, trigger, flags=0):
    global temp_triggers
    if name in temp_triggers:
        echo("trigger: {} already exists... removing it before adding new one...".format(
                name))
        remove_temp_trigger(name)
    temp_triggers[name] = add_trigger(trigger, flags=flags)

def remove_temp_trigger(name):
    global temp_triggers
    remove_trigger(temp_triggers[name])
    del(temp_triggers[name])


gmcp_handlers = defaultdict(list)

def add_gmcp_handler(gmcp_type, action):
    gmcp_handlers[gmcp_type].append(action)

def show_help(alias_group):

    print("{}:".format(alias_group), file=client.current_out_handle, flush=True)
    for pattern, desc in help_info.get(alias_group, []):
        print("{:15.15} : {}".format(pattern, desc), file=client.current_out_handle,
                                    flush=True)

base_aliases = [
    (   "#help (.*)",
        "show help",
        lambda m: show_help(m[0])
    ),
]
add_aliases("base", base_aliases)

