from achaea.basic import eqbal
from achaea.state import s
from client import c, send

jester_battlerage_aliases = [
    (
        "^nog(?: (.+))?$",
        "noogie t/[]",
        lambda matches: send("noogie {matches[0] or '&tar'}"),
    ),
    (
        "^ja(?: (.+))?$",
        "throw jacks at t/[]",
        lambda matches: send("throw jacks at {matches[0] or '&tar'}"),
    ),
    (
        "^ens(?: (.+))?$",
        "ensconce firecracker on t/[]",
        lambda matches: send("ensconce firecracker on {matches[0] or '&tar'}"),
    ),
]
c.add_aliases("ab_battlerage", jester_battlerage_aliases)


def shatter_target():
    # not checking for shielder == target because it might be a long mob name
    c.echo(f"rage: {s.rage}")
    if s.rage >= 17:
        c.send("throw jacks at &tar"),


battlerage_triggers = [
    (
        r"^A nearly invisible magical shield forms around (.*?).$",
        # someone just shielded!
        lambda matches: shatter_target(),
    ),
    (
        r"^A dizzying beam of energy strikes you as your attack rebounds off of (.*)'s shield.$",
        # someone (probably my target) is shielded!
        lambda matches: shatter_target(),
    ),
]
c.add_triggers(battlerage_triggers)
