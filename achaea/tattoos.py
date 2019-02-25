
from .basic import eqbal
from .client import send, add_aliases

tattoo_aliases = [
    #(   "^shd$",
    #    "touch shield",
    #    lambda m: eqbal("touch shield")
    #),
    (   "^clk$",
        "touch cloak",
        lambda m: eqbal("touch cloak")
    ),
    (   "^tree$",
        "touch tree",
        lambda m: eqbal("touch tree")
    ),
    (   "^minds$",
        "touch mindseye",
        lambda m: eqbal("touch mindseye")
    ),
]
add_aliases("ab_tattoos", tattoo_aliases)
