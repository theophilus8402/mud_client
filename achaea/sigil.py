
from .client import c
from .state import s


sigil_aliases = [
    (   "^eyesig$",
        "wield eyesigil;throw eyesigil at ground",
        lambda matches: c.send("wield eyesigil;throw eyesigil at ground")
    ),
]
c.add_aliases("sigil", sigil_aliases)
