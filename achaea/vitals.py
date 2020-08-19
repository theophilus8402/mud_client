
import asyncio
import logging
import time

from .client import c, echo
from .state import s

logger = logging.getLogger("achaea")


"""
Char.Vitals:
{"hp": "1350", "maxhp": "1350", "mp": "1485", "maxmp": "1485", "ep": "4600", "maxep": "4600", "wp": "4600", "maxwp": "4600", "nl": "1", "bal": "1", "eq": "1", "string": "H:1350/1350 M:1485/1485 E:4600/4600 W:4600/4600 NL:1/100 ", "charstats": ["Bleed: 0", "Rage: 0"]}
"""
def gmcp_vitals(gmcp_data):
    bal = gmcp_data.get("bal")
    eq = gmcp_data.get("eq")

    if bal == "1" and s.bal == "0":
        #echo("Got back balance!")
        pass
    elif bal == "0" and s.bal == "1":
        #echo("Lost balance!")

        # time how long it takes
        if s.show_balance_times:
            end_msg = r"^You have recovered balance on all limbs.$"
            create_end_timer("bal", end_msg)

    if eq == "1" and s.eq == "0":
        #echo("Got back eq!")
        pass
    elif eq == "0" and s.eq == "1":
        #echo("Lost eq!")

        # time how long it takes
        if s.show_balance_times:
            end_msg = r"^You have recovered equilibrium.$"
            create_end_timer("eq", end_msg)

    s.bal = bal
    s.eq = eq
c.add_gmcp_handler("Char.Vitals", gmcp_vitals)
