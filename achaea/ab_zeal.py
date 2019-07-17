
from .client import send, add_aliases
from .basic import eqbal
from .variables import v


"""
def channel_all(matches):
    
    for chan in ["air", "fire", "water", "earth", "spirit"]:
        eqbal("channel {}".format(chan))
"""

zeal_aliases = [
    (   "^att(?: (.+))?$",
        "recite attend */t",
        lambda m: eqbal(f"recite attend {m[0] or v.target}")
    ),
    (   "^prot(?: (.+))?$",
        "recite protection me",
        lambda m: eqbal(f"recite protection {m[0] or 'me'}")
    ),
]
add_aliases("ab_zeal", zeal_aliases)


