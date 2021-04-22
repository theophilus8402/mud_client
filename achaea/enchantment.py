from client import c, echo
from achaea.basic import eqbal

enchantment_aliases = [
    (
        "iw (.*)",
        "icewall dir",
        lambda m: eqbal(f"point ench/icewall {m[0]}")
    ),
    (
        "fl (.*)",
        "firelash dir",
        lambda m: eqbal(f"point ench/firelash at {m[0]}")
    ),
]
c.add_aliases("enchantment", enchantment_aliases)
