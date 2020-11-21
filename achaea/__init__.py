import re
import sys
import traceback

from achaea.mud_logging import initialize_logging
from achaea.triggers import depthswalker, druid, generic, jester, monk, portal, serpent

from . import (
    ab_survival,
    ab_vision,
    aff_healing,
    afflictions,
    anti_theft,
    balances,
    basic,
    bleeding,
    bopalopia,
    defences,
    group_fighting,
    inventory,
    ratting,
    room_info,
    sigil,
    state,
    status,
    tattoos,
    vitals,
)
