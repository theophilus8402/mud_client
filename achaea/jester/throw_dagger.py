
from ..basic import eqbal
from ..client import send, c
from ..state import s

THROW_DAGGER_HELP = """
THROW DAGGERS!
dj  - juggle daggers
dc  - throw dagger curare (paralysis - broot/magnesium)
dk  - throw dagger kalmia (asthma - kelp/aurum)
dg  - throw dagger gecko (slickness - broot/magnesium // smoke val/realgar)
da  - throw dagger aconite (stupidity - goldenseal/plumbum/focus)
ds  - throw dagger slike (anorexia - epidermal/focus)
dv  - throw dagger vernalius (weariness - kelp/aurum)
"""

def _throw_dagger(target, venom):
    eqbal(f"stand;get dagger;throw dagger at {target} {venom}")


def throw_dagger(matches):

    if matches == "d":
        c.echo(THROW_DAGGER_HELP)
    elif matches == "j":
        eqbal(f"stand;get dagger;get dagger;get dagger;unwield left;juggle dagger dagger dagger;wield blackjack")
    elif matches == "c":
        _throw_dagger(s.target, "curare")
    elif matches == "k":
        _throw_dagger(s.target, "kalmia")
    elif matches == "g":
        _throw_dagger(s.target, "gecko")
    elif matches == "a":
        _throw_dagger(s.target, "aconite")
    elif matches == "s":
        _throw_dagger(s.target, "slike")
    elif matches == "v":
        _throw_dagger(s.target, "vernalius")
    else:
        # must be a normal command... send it
        send(f"d{matches}")
