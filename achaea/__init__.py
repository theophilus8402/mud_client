
import re
import sys
import traceback

#from .client import client, aliases, triggers, gmcp_handlers
from .client import c
from . import state
from . import basic
from . import ab_battlerage
from . import ab_vision
from . import ab_survival
from . import aff_healing
from . import defences
from . import ratting
from . import room_info
from . import status
from . import tattoos
from . import group_fighting
## occultist modules
##from . import ab_occultism
##from . import ab_tarot
##from . import ab_domination
# magi modules
from achaea import ab_elementalism
from achaea import ab_crystalism
from achaea import ab_artificing
# cleric modules
#from . import ab_healing
#from . import ab_spirituality
#from . import ab_devotion
#from . import ab_zeal

def compile_aliases(aliases):

    compiled_aliases = {}


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
                    print("got a trigger match!")
                    print(f"match: {match}")
                    print(f"action: {action}")
                    action(match.groups())
                    trig_handled = True
                    #break
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

