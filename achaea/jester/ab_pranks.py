
import random

from ..client import send, c
from ..state import s
from ..basic import eqbal
from ..defences import basic_defs

pranks_basic_defs = {"slippery"}
basic_defs.update(pranks_basic_defs)


BOMB_HELP = """
BOMB INFO
con concussion - stuns, 1 iron
but butterfly - knock out of trees/sky, 1 iron
smo smoke - makes hungry, 1 iron
web web - web, 1 rope
dus dust - "knockout"?, 1 diamond dust
"""


def make_bomb(bomb_type=""):

    if bomb_type == "":
        c.echo(BOMB_HELP)
    elif "concussion".startswith(bomb_type.lower()):
        eqbal(f"stand;outr 1 iron;construct concussion bomb")
    elif "butterfly".startswith(bomb_type.lower()):
        eqbal(f"stand;outr 1 iron;construct butterfly bomb")
    elif "smoke".startswith(bomb_type.lower()):
        eqbal(f"stand;outr 1 iron;construct smoke bomb")
    elif "web".startswith(bomb_type.lower()):
        eqbal(f"stand;outr 1 rope;construct web bomb")
    elif "dust".startswith(bomb_type.lower()):
        eqbal(f"stand;outr 1 diamonddust;construct dust bomb")


def somersault(direction):
    if direction == "":
        direction = random.choice(["n", "e", "s", "w",
                                   "ne", "se", "sw", "nw",
                                   "in", "out"])
    eqbal(f"stand;somersault {direction}")


pranks_aliases = [
    (   "^m$",
        "bop t",
        lambda matches: eqbal(f"stand;bop &tar")
    ),
    (   "^gball$",
        "wish for 5 balloons",
        lambda matches: eqbal(f"stand;get 100 gold from pack;wish for 5 balloon")
    ),
    (   "^fly$",
        "inflate balloon",
        lambda matches: eqbal(f"stand;inflate balloon")
    ),
    (   "^bf (.+)?$",
        "backflip dir",
        lambda matches: eqbal(f"stand;backflip {matches[0]}")
    ),
    (   "^mb(?: (.+))?$",
        "make bombs!",
        lambda matches: make_bomb(matches[0] or "")
    ),
    (   "^vent(?: (.+))?$",
        "vent t/[]",
        lambda matches: eqbal(f"vent {matches[0] or s.target}")
    ),
    (   "^bad$",
        "badjoke",
        lambda matches: eqbal(f"badjoke")
    ),
    (   "^mic(?: (.+))?$",
        "slip t/[] mickey",
        lambda matches: eqbal(f"slip {matches[0] or s.target} mickey")
    ),
    (   "^som(?: (.+))?$",
        "somersault dir/randomdir",
        lambda matches: somersault(matches[0] or "")
    ),
    (   "^arrow(?: (.+))?$",
        "arrowcatch []/on",
        lambda matches: eqbal(f"stand;arrowcatch {matches[0] or 'on'}")
    ),
    (   "^jd$",
        "get daggers;juggle daggers",
        lambda matches: eqbal(f"stand;get dagger;get dagger;get dagger;unwield left;juggle dagger dagger")
    ),
    (   "^tdc$",
        "throw dagger curare",
        lambda matches: eqbal(f"stand;throw dagger at {s.target} curare")
    ),
    (   "^tdk$",
        "throw dagger kalmia",
        lambda matches: eqbal(f"stand;throw dagger at {s.target} kalmia")
    ),
    (   "^tdg$",
        "throw dagger gecko",
        lambda matches: eqbal(f"stand;throw dagger at {s.target} gecko")
    ),
    (   "^wb$",
        "wield blackjack",
        lambda matches: eqbal(f"stand;unwield left;wield blackjack")
    ),
]
c.add_aliases("ab_pranks", pranks_aliases)
