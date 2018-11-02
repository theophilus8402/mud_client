
import re

from .client import client, aliases, triggers
from . import palleo
from . import basic
from . import ab_spirituality
from . import aff_healing

def compile_aliases(aliases):

    compiled_aliases = {}


class Achaea():

    """
    def __init__(self):

        self.modules = [ab_spirituality, palleo, basic]

        self.aliases = []
        self.help_info = {}
        self.initialize_aliases()

        self.triggers = []
        self.initialize_triggers()

    def get_base_aliases(self):
        base_aliases = [
            (   "#help (.*)",
                "show help",
                lambda m: self.show_help(m[0])
            ),
        ]
        return base_aliases

    def initialize_aliases(self):
        self.help_info[group_name] = []
        for pattern, desc, func in aliases:
            self.aliases.append((re.compile(pattern), func))
            self.help_info[group_name].append((pattern, desc))
    """

    def handle_aliases(self, msg):

        global aliases
        alias_handled = False
        #for compiled_pattern, action in self.aliases:
        for compiled_pattern, action in aliases:
            #print("handling: {}".format(compiled_pattern.pattern))
            match = compiled_pattern.match(msg)
            if match:
                #print("got a match! msg")
                action(match.groups())
                alias_handled = True
                break

        return alias_handled

    """
    def show_help(self, alias_group):

        print("{}:".format(alias_group), file=client.current_out_handle, flush=True)
        for pattern, desc in self.help_info[alias_group]:
            print("{} : {}".format(pattern, desc), file=client.current_out_handle, flush=True)

    def initialize_triggers(self):

        for mod in self.modules:
            for group, trigs in mod.get_triggers().items():
                for pattern, action in trigs:
                    self.triggers.append((re.compile(pattern), action))
    """

    def handle_triggers(self, msg):

        trig_handled = False

        #for compiled_pattern, action in self.triggers:
        for compiled_pattern, action in triggers:
            #print("handling: <{}> {}".format(msg, compiled_pattern.pattern))
            match = compiled_pattern.match(msg)
            if match:
                #print("got a match!")
                action(match.groups())
                trig_handled = True
                break

        return trig_handled

