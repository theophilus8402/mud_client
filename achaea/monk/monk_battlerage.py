from achaea.basic import eqbal
from achaea.state import s
from client import c, echo, send


def spk_target():
    if s.char_status.rage >= 17:
        send("spk &tar")


battlerage_triggers = [
    (
        r"^A nearly invisible magical shield forms around (.*?).$",
        # someone just shielded!
        lambda _: spk_target(),
    ),
    (
        r"^A dizzying beam of energy strikes you as your attack rebounds off of (.*)'s shield.$",
        # someone (probably my target) is shielded!
        lambda _: spk_target(),
    ),
]
c.add_triggers(battlerage_triggers)


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
    (
        "^rp$",
        "ripplestrike t",
        lambda matches: send("rpst &tar"),
    ),
]
c.add_aliases("ab_battlerage", battlerage_aliases)
