
from client import c, send, echo
from ..timers import timers
from ..room_info.room_info import monolith_in_room

"""
# leave the room immediately, stay out for more than 15 seconds!
A beam of prismatic light suddenly shoots into the room.


# wand of portals, drop mono if one isn't there
The beginnings of a fiery portal appear before you.
A fiery portal opens in the air before you.


# Sonicportal, Magi only, drop mono if one isn't there
A piercing sound cleaves through the air.
A sonic portal opens in the air, edges vibrating slightly.


# Forestal gate/portal, Druid and Sylvan only
A gateway of light blazes into existence before your eyes.

"""


def incoming_prism():
    echo("### Someone PRISMING in!!!  Leave the room!! ###")
    timers.add(f"prism_wait",
        lambda: echo("It's been 15 seconds, should be safe now."), 15)


def incoming_portal(portal_type):
    echo(f"### Incoming Portal!!! {portal_type.upper()} Check for a mono in the room! ###")
    if monolith_in_room() == True:
        echo("Phew!  There's a monolith in the room!")
    else:
        echo("Panic!  There's no monolith in the room!")
    

portal_triggers = [
    (   "^A beam of prismatic light suddenly shoots into the room.$",
        # someone is prisming in!
        lambda _: incoming_prism()
    ),
    (   "^The beginnings of a fiery portal appear before you.$",
        # someone is portaling in!
        lambda _: incoming_portal("fiery_1")
    ),
    (   "^A fiery portal opens in the air before you.$",
        # someone is portaling in!
        lambda _: incoming_portal("fiery_2")
    ),
    (   "^A piercing sound cleaves through the air.$",
        # someone is portaling in!
        lambda _: incoming_portal("sonic_1")
    ),
    (   "^A sonic portal opens in the air, edges vibrating slightly.$",
        # someone is portaling in!
        lambda _: incoming_portal("sonic_2")
    ),
    (   "^A gateway of light blazes into existence before your eyes.$",
        # someone is portaling in!
        lambda _: incoming_portal("forestal_gate")
    ),
]
c.add_triggers(portal_triggers)
