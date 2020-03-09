
from .client import c
from .state import s

"""
Char.Vitals { "hp": "4050", "maxhp": "4050", "mp": "5445", "maxmp": "5445", "ep": "15400", "maxep": "15400", "wp": "18734", "maxwp": "19900", "nl": "81", "bal": "1", "eq": "1", "vote": "1", "string": "H:4050/4050 M:5445/5445 E:15400/15400 W:18734/19900 NL:81/100 ", "charstats": [ "Bleed: 0", "Rage: 0", "Channels: F W A E " ] }
"""

def gmcp_bal_eq(gmcp_data):
    s.bal = gmcp_data.get("bal")
    s.eq = gmcp_data.get("eq")
    # sometimes, like with blackout, we won't get the hp/mp use the prev vals
    s.hp = int(gmcp_data.get("hp", s.hp))
    s.mp = int(gmcp_data.get("mp", s.mp))
c.add_gmcp_handler("Char.Vitals", gmcp_bal_eq)
