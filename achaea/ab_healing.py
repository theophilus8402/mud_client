
from .client import send, add_aliases
from .basic import eqbal
from .variables import v


def channel_all(matches):
    
    for chan in ["air", "fire", "water", "earth", "spirit"]:
        eqbal("channel {}".format(chan))

healing_aliases = [
    (   "^hdb$",
        "heal t blindness/deafness",
        lambda m: eqbal("heal {t} blindness;heal {t} deafness".format(t=v.target)),
    ),
    (   "^chans$",
        "channel all",
        channel_all,
    ),
]
add_aliases("ab_healing", healing_aliases)


