
import asyncio
import json
import re

from collections import defaultdict
from datetime import datetime
from functools import singledispatch
from telnetlib import IAC, SB, SE

GMCP = b'\xc9'


from .state import DiffState

class Client():

    def __init__(self):
        # it's a little weird, but to_send is going to be a "prequeue"
        # I'll use self.send_flush() to actuall send the traffic
        # with this, I can group commands together more easily... hopefully
        self.to_send = []
        self.send_queue = asyncio.Queue()
        self._delete_line = False

        self.line = None
        self.modified_current_line = None
        self.last_command = ""

        # handles
        self.handles = {}
        self.open_handle("default", "achaea.log")
        self.default_out_handle = self.handles["default"]
        self.current_out_handle = self.handles["default"]
        self.log = self.start_main_log()
        self.open_handle("says", "says.log")
        self.says_handle = self.handles["says"]

        # aliases.append((compiled_pattern, function))
        self._aliases = []

        # triggers
        self._temp_triggers = {}
        self._triggers = []
        self.add_temp_trigger("target_trigger", ("target_trigger", lambda m: False))

        # gmcp
        self._gmcp_handlers = defaultdict(list)

        # help_info[group_name] = [(pattern, desc)]
        self.help_info = {}

    def add_aliases(self, group_name, new_aliases):
        if group_name in self.help_info.keys():
            print(f"{group_name} already exists!",
                  file=self.current_out_handle, flush=True)
            return False
    
        self.help_info[group_name] = []
        for pattern, desc, func in new_aliases:
            self._aliases.append((re.compile(pattern), func))
            self.help_info[group_name].append((pattern, desc))
        return True

    def open_handle(self, name, file_path):
        self.handles[name] = open(file_path, "a")

    def close(self):
        for handle in self.handles.values():
            handle.close()

    def start_main_log(self):
        now = datetime.now()
        log_name = f"logs/achaea/{now.strftime('%Y-%m-%d.txt')}"
        self.open_handle("main_log", log_name)
        return self.handles["main_log"]

    def main_log(self, msg, msg_type):
        try:
            timestamp = datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f')
            str_json = json.dumps((timestamp, msg_type, msg)).strip()
            print(f"{str_json}", file=self.log, flush=True)
            #self.log.write(f"{str_json}\n")
        except Exception as e:
            print(f"Exception: {e}")

    def add_temp_trigger(self, name, trigger, flags=0):
        if name in self._temp_triggers:
            self.echo(f"trigger: {name} already exists... removing it before adding new one...")
            self.remove_temp_trigger(name)
        self._temp_triggers[name] = self.add_trigger(trigger, flags=flags)
    
    def remove_temp_trigger(self, name):
        if name in self._temp_triggers:
            self.remove_trigger(self._temp_triggers.get(name))
            del(self._temp_triggers[name])

    def add_triggers(self, new_triggers, flags=0):
        for new_trig in new_triggers:
            self.add_trigger(new_trig, flags=flags)
        return True
    
    def add_trigger(self, new_trigger, flags=0):
        pattern, action = new_trigger
        print(f"adding trigger: {pattern}")
        try:
            compiled_pattern = re.compile(pattern, flags=flags)
        except Exception as e:
            print(f"bad pattern? {pattern}")
        if pattern.startswith("^"):
            search_method = compiled_pattern.match
        else:
            search_method = compiled_pattern.search
        self._triggers.append((search_method, action))
        return self._triggers[-1]
    
    def remove_trigger(self, trigger):
        try:
            self._triggers.remove(trigger)
        except ValueError:
            self.echo("Trying to remove a trigger that doesn't exist!")

    def send(self, msg):
        self.to_send.append(msg)

    def send_flush(self):
        msg_blob = ";".join(self.to_send)
        if isinstance(msg_blob, str) and not msg_blob.endswith("\n"):
            msg_blob = f"{msg_blob}\n"
            self.main_log(msg_blob.strip(), "data_sent")
        #echo(f"to_send: {self.to_send} sending: {msg_blob}")
        self.send_queue.put_nowait(msg_blob)
        self.to_send.clear()

    def gmcp_send(self, msg):
        self.send(msg.encode("iso-8859-1"))
    
    def echo(self, msg):
        # TODO: move this functionality somewhere else
        print(msg.rstrip(), file=self.current_out_handle, flush=True)

        ds = DiffState()
        ds.echo_lines.append(msg)
        return ds

    def set_line(self, new_line):
        self.modified_current_line = new_line
    
    def delete_line(self):
        self._delete_line = True

    def add_gmcp_handler(self, gmcp_type, action):
        print(f"adding handler: {gmcp_type} {action}")
        self._gmcp_handlers[gmcp_type].append(action)


c = Client()

# making these functions just to typing them shorter/easier
send = c.send
echo = c.echo
set_line = c.set_line
delete_line = c.delete_line


