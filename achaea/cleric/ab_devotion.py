from client import c

from ..basic import eqbal
from ..state import s


def pilgrimage(matches):
    if matches[0]:
        eqbal(f"perform pilgrimage {matches[0]}")
    else:
        eqbal("perform rite of pilgrimage")


devotion_aliases = [
    (
        "^hh(?: (.+))?$",
        "perform hands []",
        lambda matches: eqbal(f"perform hands {matches[0] or ''}"),
    ),
    (
        "^part (.+)$",
        "perform truth",
        lambda m: eqbal(f"perform parting {m[0]}"),
    ),
    (
        "^truth$",
        "perform truth",
        lambda _: eqbal("perform truth"),
    ),
    (
        "^bliss(?: (.+))?$",
        "perform bliss []/me",
        lambda matches: eqbal(f"perform bliss {matches[0] or 'me'}"),
    ),
    ("^insp$", "perform inspiration", lambda matches: eqbal("perform inspiration")),
    (
        "^pilg(?: (.+))?$",
        "perform pilg [] / perf right of pilg",
        lambda matches: pilgrimage(matches),
    ),
    (
        "^pur(?: (.+))?$",
        "perform purity []/t",
        lambda matches: eqbal(f"perform purity {matches[0] or '&tar'}"),
    ),
    (
        "^vis(?: (.+))?$",
        "perform visions []/t",
        lambda matches: eqbal(f"perform visions {matches[0] or '&tar'}"),
    ),
    (
        "^pward$",
        "perform rite of warding",
        lambda matches: eqbal("perform rite of warding"),
    ),
    (
        "^force (.+)$",
        "perform force stuff",
        lambda matches: eqbal("perform force matches[0]"),
    ),
    (
        "^piety$",
        "perform right of piety",
        lambda matches: eqbal("perform rite of piety"),
    ),
    (
        "^daz(?: (.+))?$",
        "perform dazzle t",
        lambda matches: eqbal(f"perform dazzle {matches[0] or '&tar'}"),
    ),
    (
        "^demons$",
        "perform right of demons",
        lambda matches: eqbal("perform rite of demons"),
    ),
    (
        "^slo(?: (.+))?$",
        "perform sloth t",
        lambda matches: eqbal(f"perform sloth {matches[0] or '&tar'}"),
    ),
    (
        "^alls$",
        "perform rite of allsight",
        lambda matches: eqbal("perform rite of allsight"),
    ),
    (
        "^pheal$",
        "perform rite of healing",
        lambda matches: eqbal("perform rite of healing"),
    ),
    (
        "^pen(?: (.+))?$",
        "perform penitence []/t",
        lambda matches: eqbal(f"perform penitence {matches[0] or '&tar'}"),
    ),
]
c.add_aliases("ab_devotion", devotion_aliases)
