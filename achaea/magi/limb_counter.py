
from client import c, send, echo
from ..state import s
from ..basic import eqbal


"""
["2020/03/26 23:21:39.392648", "data_sent", "stand;staffstrike kog with water left arm;golem smash kog legs"]
["2020/03/26 23:21:39.483088", "server_text", "You call upon Sllshya and unleash a forceful blow towards Kog's left arm with your trusty staff.\r"]
["2020/03/26 23:21:39.484023", "server_text", "You direct a crystalline golem to smash the legs of Kog.\r"]
["2020/03/26 23:21:39.485742", "server_text", "The crackle of snapping bone can be heard as a crystalline golem viciously twists the left leg of Kog.\r"]
["2020/03/26 23:21:39.602900", "server_text", "Kog takes some salve from a vial and rubs it on his legs.\r"]
["2020/03/26 23:21:41.119817", "server_text", "Kog takes some salve from a vial and rubs it on his skin.\r"]

["2020/03/26 23:15:20.037502", "server_text", "You call upon Kkractle and unleash a forceful blow towards Kog with your trusty staff.\r"]
You call upon Whiirh and unleash a forceful blow towards (\w+)'s (\w+) with your trusty staff.
You call upon Garash and unleash a forceful blow towards Kog's left arm with your trusty staff.


["2020/03/26 23:15:20.037502", "server_text", "You call upon Kkractle and unleash a forceful blow towards Kog with your trusty staff.\r"]
["2020/03/26 23:15:20.040294", "server_text", "The attack rebounds back onto you!\r"]
"""

strike_map = {
    "Whiirh"   : "air",
    "Garash"   : "earth",
    "Sllshya"  : "water",
    "Kkractle" : "fire",
}

"""
class LimbCounter():

    def __init__(self):
        self._strikes = []
"""

def count_strike(matches):
    echo("Calling count_strike")
    strike_type = strike_map[matches[0]]
    person_hit = matches[1]
    limb = matches[2]
    echo(f"{strike_type} strike to {person_hit}'s {limb}")

    # need to check to see if I rebounded!
    #echo(f"current_chunk: '{c.current_chunk}'")
    if "The attack rebounds back onto you!" in c.current_chunk:
        echo("You fool!  You rebounded!")

# end of timeflux:
#Limea appears far less sluggish all of a sudden.

"""
You call upon Garash and unleash a forceful blow towards Limea's left leg with your trusty staff.
The attack rebounds onto you!
The element of earth shakes you to the core, breaking your left arm.
"""


limb_counter_triggers = [
    (   r"^You call upon (\w+) and unleash a forceful blow towards (\w+)'s (.*) with your trusty staff.$",
        # staffstrike to limb
        #lambda m:echo("limb_counter")
        lambda m: count_strike(m)
    ),
]
c.add_triggers(limb_counter_triggers)
