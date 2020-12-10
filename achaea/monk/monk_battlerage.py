from achaea.basic import eqbal
from achaea.state import s
from client import c, echo, send

battlerage_aliases = [
    (
        "^sb$",
        "spinningbackfist t",
        lambda matches: send("sbp &tar"),
    ),
    (
        "^spk$",
        "splinterkick t",
        lambda matches: send("spk &tar"),
    ),
    (
        "^tnk$",
        "tornadokick t",
        lambda matches: send("tnk &tar"),
    ),
    (
        "^mb$",
        "mind blast t",
        lambda matches: send("mb &tar"),
    ),
]
c.add_aliases("ab_battlerage", battlerage_aliases)
