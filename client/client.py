import asyncio
import json
import re
import sys
import traceback
from collections import defaultdict
from datetime import datetime

from telnet_manager import strip_ansi


class Client:
    def __init__(self):
        # it's a little weird, but to_send is going to be a "prequeue"
        # I'll use self.send_flush() to actuall send the traffic
        # with this, I can group commands together more easily... hopefully
        self.to_send = []
        self.send_queue = asyncio.Queue()
        self._delete_line = False
        self._delete_lines = set()

        self.current_line = None
        self.current_chunk = None
        self.modified_current_line = None
        self.last_command = ""

        self._after_current_chunk_processes = []

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

    def handle_input(self, input_buffer):

        data = input_buffer.text

        # check to see if the user just hit enter
        # if so, send the last command instead
        if data == "":
            data = self.last_command

        self.main_log(data, "user_input")
        self.last_command = data

        # handle user input
        for cmd in data.split(";"):
            if not self.handle_aliases(cmd):
                self.send(cmd)
            # else assume msgs are sent as needed

        # everything has been queued in self.to_send
        # use self.send_flush() to actually send it
        self.send_flush()

    def handle_aliases(self, msg):

        alias_handled = False
        # for compiled_pattern, action in self.aliases:
        for compiled_pattern, action in self._aliases:
            match = compiled_pattern.match(msg)
            if match:
                action(match.groups())
                alias_handled = True
                break

        return alias_handled

    def handle_triggers(self, msg):

        trig_handled = False

        # for compiled_pattern, action in self.triggers:
        for search_method, action in self._triggers:
            # match = compiled_pattern.match(msg)
            match = search_method(msg)
            if match:
                # c.echo(match.re.pattern)
                try:
                    action(match.groups())
                    trig_handled = True
                except Exception as e:
                    print(f"handle_triggers: {e}")

        return trig_handled

    def handle_gmcp(self, gmcp_type, gmcp_data):
        try:
            for gmcp_handler in self._gmcp_handlers.get(gmcp_type, []):
                gmcp_handler(gmcp_data)
            # basic.echo(f"{gmcp_type} : {gmcp_data}")
        except Exception as e:
            print(f"problem with __init__.handle_gmcp {e}")
            traceback.print_exc(file=sys.stdout)

    def add_aliases(self, group_name, new_aliases):
        if group_name in self.help_info.keys():
            self.echo(
                f"{group_name} already exists!",
                file=self.current_out_handle,
                flush=True,
            )
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
            timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")
            str_json = json.dumps((timestamp, msg_type, msg)).strip()
            print(f"{str_json}", file=self.log, flush=True)
            # self.log.write(f"{str_json}\n")
        except Exception as e:
            print(f"Exception: {e}")

    def add_temp_trigger(self, name, trigger, flags=0):
        if name in self._temp_triggers:
            self.echo(
                f"trigger: {name} already exists... removing it before adding new one..."
            )
            self.remove_temp_trigger(name)
        self._temp_triggers[name] = self.add_trigger(trigger, flags=flags)

    def remove_temp_trigger(self, name):
        if name in self._temp_triggers:
            self.remove_trigger(self._temp_triggers.get(name))
            del self._temp_triggers[name]

    def add_triggers(self, new_triggers, flags=0):
        for new_trig in new_triggers:
            self.add_trigger(new_trig, flags=flags)
        return True

    def add_trigger(self, new_trigger, flags=0):
        pattern, action = new_trigger
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

    def add_after_current_chunk_process(self, process):
        self._after_current_chunk_processes.append(process)

    def run_after_current_chunk(self):
        for process in self._after_current_chunk_processes:
            process()

    def send(self, msg):
        self.to_send.append(msg)

    def send_flush(self):
        max_cmd_len = 10
        for i in range(0, len(self.to_send), max_cmd_len):
            msg_blob = ";".join(self.to_send[i:max_cmd_len])
            if isinstance(msg_blob, str) and not msg_blob.endswith("\n"):
                msg_blob = f"{msg_blob}\n"
                self.main_log(msg_blob.strip(), "data_sent")
            # self.echo(f"to_send: {self.to_send} sending: {msg_blob}")
            self.send_queue.put_nowait(msg_blob)
        self.to_send.clear()

    def gmcp_send(self, msg):
        self.send_queue.put_nowait(msg.encode("iso-8859-1"))

    def echo(self, msg):
        print(msg, file=self.current_out_handle, flush=True)

    def set_line(self, new_line):
        self.modified_current_line = new_line

    def delete_line(self):
        self._delete_line = True

    def delete_lines(self, lines):
        for line in lines:
            self._delete_lines.add(strip_ansi(line).rstrip("\r"))

    def add_gmcp_handler(self, gmcp_type, action):
        # self.echo(f"adding handler: {gmcp_type} {action}")
        self._gmcp_handlers[gmcp_type].append(action)
