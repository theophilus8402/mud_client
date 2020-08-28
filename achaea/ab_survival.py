
from .basic import eqbal
from .client import c, send
from .defences import auto_defences


def generosity():
    auto_defences(["selfishness"], "off")
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

