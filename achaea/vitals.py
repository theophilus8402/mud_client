
import asyncio
import logging
import time

from .client import c, echo
from .state import s

import ui

logger = logging.getLogger("achaea")


"""
Char.Vitals:
{"hp": "1350", "maxhp": "1350", "mp": "1485", "maxmp": "1485", "ep": "4600", "maxep": "4600", "wp": "4600", "maxwp": "4600", "nl": "1", "bal": "1", "eq": "1", "string": "H:1350/1350 M:1485/1485 E:4600/4600 W:4600/4600 NL:1/100 ", "charstats": ["Bleed: 0", "Rage: 0"]}
"""
def gmcp_vitals(gmcp_data):
    ui.core.update_prompt_info(gmcp_data)
c.add_gmcp_handler("Char.Vitals", gmcp_vitals)
