
from client import c, send, echo
from achaea.basic import handle_login_info
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


class CharStatus():
    def __init__(self):
        # this is just meant to hold data from Char.Status
        # when we get a Char.Status, we never know what all
        # will come in (as far as info goes)
        # so this will just get updated as the info comes in
        pass

s.char_status = CharStatus()


def gmcp_char_status(gmcp_data):
    for key, value in gmcp_data.items():
        if key == "class" and getattr(s.char_status, "class", "") != value:
            # we've changed class and need to load the appropriate modules
            #TODO: fix this hack way of loading class modules
            handle_login_info({"name": "sarmenti"})
        setattr(s.char_status, key, value)
c.add_gmcp_handler("Char.Status", gmcp_char_status)


def show_char_status(char_status):
    echo("=== Char Status ===")
    for key, value in char_status.__dict__.items():
        echo(f"{key} = {value}")


char_status_aliases = [
    (   "^cs$",
        "show char status",
        lambda _: show_char_status(s.char_status)
    ),
]
c.add_aliases("char_status", char_status_aliases)

"""
Char.Status { "name": "Sarmenti", "fullname": "Sarmenti, Aspirant of Elocution", "age": "23", "race": "Human", "specialisation": "Rogue", "level": "79 (77%)", "xp": "77%", "xprank": "888", "class": "Jester", "city": "Mhaldor (1)", "house": "The Dread Legates(3)", "order": "(None)", "boundcredits": "0", "unboundcredits": "0", "lessons": "11", "explorerrank": "a Rambler", "mayancrowns": "0", "boundmayancrowns": "0", "gold": "3557", "bank": "14100", "unread_news": "13", "unread_msgs": "9", "target": "None", "gender": "male" }
"""
