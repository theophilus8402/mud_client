
import random

from ..client import send, c
from ..state import s
from ..basic import eqbal
from ..defences import basic_defs
from ..jester.throw_dagger import throw_dagger


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


THROW_BOMB_HELP = """
THROW BOMB HELP
b   - THROW_BOMB_HELP
bc  - throw concussionbomb dir/at ground
bb  - throw butterflybomb dir/at ground
bs  - throw smokebomb dir/at ground
bw  - throw webbomb dir/at ground
bd  - throw dustbomb dir/at ground
"""

def _throw_bomb(bomb_type, direction=""):
    return f"stand;unwield left;wield {bomb_type} left;throw {bomb_type} {direction}"


def parse_throw_direction(matches):
    try:
        bomb_type, direction = matches.split(" ")
    except ValueError:
        direction = "at ground"
    return direction


def throw_bomb(matches):

    direction = parse_throw_direction(matches)

    if matches == "":
        c.echo(THROW_BOMB_HELP)
    elif matches.startswith("c"):
        c.send(_throw_bomb("concussionbomb", direction))
    elif matches.startswith("b"):
        c.send(_throw_bomb("butterflybomb", direction))
    elif matches.startswith("s"):
        c.send(_throw_bomb("smokebomb", direction))
    elif matches.startswith("w"):
        c.send(_throw_bomb("webbomb", direction))
    elif matches.startswith("d"):
        c.send(_throw_bomb("dustbomb", direction))
    else:
        send(f"b{matches}")


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
    (   "^b(?!ad|f)(.*)$",
        "throw bombs!",
        lambda matches: throw_bomb(matches[0])
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
    (   "^d(?!h)(.+)$",
        "throw daggers!",
        lambda matches: throw_dagger(matches[0])
    ),
    (   "^wb$",
        "wield blackjack",
        lambda matches: eqbal(f"stand;unwield left;wield blackjack")
    ),
]
c.add_aliases("ab_pranks", pranks_aliases)
