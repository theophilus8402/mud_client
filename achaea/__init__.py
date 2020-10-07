
import re
import sys
import traceback

#import achaea.mud_logging

from . import state
from . import anti_theft
from . import afflictions
from . import basic
from . import balances
from . import bleeding
from . import bopalopia
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
from . import vitals
from achaea.triggers import depthswalker
from achaea.triggers import generic
from achaea.triggers import serpent

#TODO: FIX THIS!!! Should have it as an extra argument when restarting the client?
# the gmcp isn't sufficient because of stopping and restarting the client
#basic.handle_login_info({"name": "sarmenti"})
