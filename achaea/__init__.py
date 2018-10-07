
import re

from . import palleo

def compile_aliases(aliases):

    compiled_aliases = {}


class Achaea():

    def __init__(self):

        self.modules = [palleo]

        self.aliases = []
        self.help_info = {}
        self.initialize_aliases()

        self.triggers = []
        self.initialize_triggers()

    def initialize_aliases(self):
        for mod in self.modules:
            for group_name, aliases in mod.get_aliases().items():

                alias_info = []
                for pattern, desc, func in aliases:
                    self.aliases.append((re.compile(pattern), func))
                    alias_info.append((pattern, desc))

                self.help_info[group_name] = alias_info

    def handle_aliases(self, msg):

        alias_handled = False
        for compiled_pattern, action in self.aliases:
            print("handling: {}".format(compiled_pattern.pattern))
            match = compiled_pattern.match(msg)
            if match:
                print("got a match! msg")
                action(match.groups())
                alias_handled = True
                break

        return alias_handled

    def show_help(self, alias_group):

        print("{}:".format(alias_group))
        for pattern, desc in self.help_info[alias_group]:
            print("{} : {}".format(pattern, desc))

    def initialize_triggers(self):

        for mod in self.modules:
            for group, trigs in mod.get_triggers().items():
                for pattern, action in trigs:
                    self.triggers.append((re.compile(pattern), action))

    def handle_triggers(self, msg):

        trig_handled = False

        for compiled_pattern, action in self.triggers:
            print("handling: {}".format(compiled_pattern.pattern))
            match = compiled_pattern.match(msg)
            if match:
                print("got a match! msg")
                action(match.groups())
                trig_handled = True
                break

        return trig_handled

