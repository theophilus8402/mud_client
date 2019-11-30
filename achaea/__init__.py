
import re

from .client import client, aliases, triggers, gmcp_handlers
from . import basic
from . import ab_battlerage
#from . import ab_healing
from . import ab_vision
from . import ab_survival
from . import aff_healing
from . import defences
from . import ratting
from . import room_info
from . import status
from . import tattoos
# occultist modules
from . import ab_occultism
from . import ab_tarot
from . import ab_domination
"""
# cleric modules
from . import ab_spirituality
from . import ab_devotion
from . import ab_zeal
"""

def compile_aliases(aliases):

    compiled_aliases = {}


class Achaea():

    def handle_aliases(self, msg):

        global aliases
        alias_handled = False
        #for compiled_pattern, action in self.aliases:
        for compiled_pattern, action in aliases:
            #print("handling: {}".format(compiled_pattern.pattern))
            match = compiled_pattern.match(msg)
            if match:
                #print(f"got a match! {msg}")
                action(match.groups())
                alias_handled = True
                break

        return alias_handled

    def handle_triggers(self, msg):

        trig_handled = False

        #for compiled_pattern, action in self.triggers:
        for search_method, action in triggers:
            #print("handling: <{}> {}".format(msg, compiled_pattern.pattern))
            #match = compiled_pattern.match(msg)
            match = search_method(msg)
            if match:
                #print("got a match!")
                action(match.groups())
                trig_handled = True
                break

        return trig_handled

    def handle_gmcp(self, gmcp_type, gmcp_data):
        if gmcp_type in gmcp_handlers:
            for gmcp_handler in gmcp_handlers[gmcp_type]:
                gmcp_handler(gmcp_data)
        #else:
        #basic.echo("{} : {}".format(gmcp_type, gmcp_data))
            #pass

