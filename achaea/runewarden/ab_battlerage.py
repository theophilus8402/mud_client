from client import c, send

from achaea.basic import eqbal
from achaea.state import s


def fragment_target():
    c.echo(f"rage: {s.rage}")
    if s.rage >= 17:
        send("fragment &tar")


battlerage_triggers = [
    (
        r"^A nearly invisible magical shield forms around (.*?).$",
        # someone just shielded!
        lambda _: fragment_target(),
    ),
]
c.add_triggers(battlerage_triggers)


# runewarden battlerage
runewarden_battlerage_aliases = [
    (
        "^co(?: (.+))?$",
        "collide t/[]",
        lambda matches: send("collide {matches[0] or '&tar'}"),
    ),
    ("^bul$", "bulwark", lambda matches: send("bulwark")),
    (
        "^ons(?: (.+))?$",
        "onslaught t/[]",
        lambda matches: send("onslaught {matches[0] or '&tar'}"),
    ),
    (
        "^fr(?: (.+))?$",
        "fragment t/[]",
        lambda matches: send("fragment {matches[0] or '&tar'}"),
    ),
    (
        "^sf (.+)?$",
        "safeguard []",
        lambda matches: send("safeguard {matches[0]}")
    ),
]
c.add_aliases("ab_battlerage", runewarden_battlerage_aliases)
