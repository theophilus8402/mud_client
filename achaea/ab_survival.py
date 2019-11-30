
from .basic import eqbal
from .client import send, add_aliases

survival_aliases = [
    (   "^self$",
        "selfishness",
        lambda m: eqbal("selfishness")
    ),
    (   "^gener$",
        "generosity",
        lambda m: eqbal("generosity")
    ),
    (   "^eg$",
        "enter grate",
        lambda m: eqbal("enter grate")
    ),
]
add_aliases("ab_survival", survival_aliases)

