
import re
import sys
import traceback

import achaea.mud_logging

from .client import c
from . import state
from . import anti_theft
from . import afflictions
from . import basic
from . import balances
from . import bleeding
#from . import ab_battlerage
from . import ab_vision
from . import ab_survival
from . import aff_healing
from . import defences
from . import ratting
from . import room_info
from . import status
from . import tattoos
from . import group_fighting
from . import sigil
from achaea.triggers import depthswalker
from achaea.triggers import generic
from achaea.triggers import serpent

#TODO: FIX THIS!!! Should have it as an extra argument when restarting the client?
# the gmcp isn't sufficient because of stopping and restarting the client
basic.handle_login_info({"name": "theophilus"})

class Achaea():

    def handle_aliases(self, msg):

        alias_handled = False
        #for compiled_pattern, action in self.aliases:
        for compiled_pattern, action in c._aliases:
            #print("handling: {}".format(compiled_pattern.pattern))
            match = compiled_pattern.match(msg)
            if match:
                action(match.groups())
                alias_handled = True
                break

        return alias_handled

    def handle_triggers(self, msg):

        trig_handled = False

        #for compiled_pattern, action in self.triggers:
        for search_method, action in c._triggers:
            #print("handling: <{}> {}".format(msg, compiled_pattern.pattern))
            #match = compiled_pattern.match(msg)
            match = search_method(msg)
            if match:
                try:
                    action(match.groups())
                    trig_handled = True
                except Exception as e:
                    print(f"handle_triggers: {e}")

        return trig_handled

    def handle_gmcp(self, gmcp_type, gmcp_data):
        try:
            for gmcp_handler in c._gmcp_handlers.get(gmcp_type, []):
                gmcp_handler(gmcp_data)
            #basic.echo(f"{gmcp_type} : {gmcp_data}")
        except Exception as e:
            print(f"problem with __init__.handle_gmcp {e}")
            traceback.print_exc(file=sys.stdout)

