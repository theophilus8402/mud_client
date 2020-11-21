from client import c, send

from .basic import eqbal

# note: if I play someone who can shield differently again
# I can make a function that checks the current class and does different things

tattoo_aliases = [
    ("^shd$", "touch shield", lambda m: eqbal("touch shield")),
    ("^clk$", "touch cloak", lambda m: eqbal("touch cloak")),
    ("^tree$", "touch tree", lambda m: eqbal("touch tree")),
    ("^minds$", "touch mindseye", lambda m: eqbal("touch mindseye")),
]
c.add_aliases("ab_tattoos", tattoo_aliases)
