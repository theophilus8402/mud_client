from achaea.basic import eqbal
from achaea.defences import basic_defs
from achaea.state import s
from client import c, echo, send

kaido_basic_defs = {"weathering", "vitality", "toughness"}
basic_defs.update(kaido_basic_defs)


def kai_trance(new_state):
    if new_state == "on":
        eqbal("kai trance")
    else:
        eqbal("break trance")


kaido_aliases = [
    (
        "^regen(?: (.+))?$",
        "regeneration [on]/off",
        lambda matches: eqbal(f"regeneration {matches[0] or 'on'};boost regeneration"),
    ),
    (
        "^tr(?: (.+))?$",
        "transmute 300/#",
        lambda matches: eqbal(f"transmute {matches[0] or '300'}", prepend=True),
    ),
    (
        "^nu$",
        "numb",
        lambda matches: eqbal(f"numb"),
    ),
    (
        "^kt(?: (.+))?$",
        "kai trance [on]/off",
        lambda matches: kai_trance(matches[0] or "on"),
    ),
    (
        "^kc(?: (.+))?$",
        "kai choke []/t (10 kai)",
        lambda matches: eqbal(f"kai choke {matches[0] or s.target}"),
    ),
    (
        "^kr(?: (.+))?$",
        "kai cripple []/t (41 kai)",
        lambda matches: eqbal(f"kai cripple {matches[0] or s.target}"),
    ),
    (
        "^kh$",
        "kai heal (21 kai)",
        lambda matches: eqbal(f"kai heal"),
    ),
    (
        "^ks(?: (.+))?$",
        "kai surge []/t (31 kai)",
        lambda matches: eqbal(f"kai surge {matches[0] or s.target}"),
    ),
    (
        "^kb(?: (.+))?$",
        "kai boost (11 kai)",
        lambda matches: eqbal(f"kai boost"),
    ),
]
c.add_aliases("ab_kaido", kaido_aliases)
