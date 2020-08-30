
from .basic import eqbal
from .client import c, send
from .defences import auto_defences
from .timers import timers


def generosity():
    auto_defences(["selfishness"], "off")
    timers.add(f"turnon_selfish", lambda: auto_defences("selfishness", "on"), 5)
    eqbal("generosity")
    
survival_aliases = [
    (   "^self$",
        "selfishness",
        lambda m: auto_defences(["selfishness"], "on")
    ),
    (   "^gener$",
        "generosity",
        lambda m: generosity()
    ),
    (   "^eg$",
        "enter grate",
        lambda m: eqbal("enter grate")
    ),
]
c.add_aliases("ab_survival", survival_aliases)

