
from .variables import v
from .basic import eqbal
from .client import add_aliases, add_triggers


def pilgrimage(matches):
    if matches[0]:
        eqbal("perform pilgrimage {}".format(matches[0]))
    else:
        eqbal("perform rite of pilgrimage")

devotion_aliases = [
    (   "^hh(?: (.+))?$",
        "perform hands []",
        lambda matches: eqbal("perform hands {}".format(matches[0] or ""))
    ),
    (   "^truth$",
        "perform truth",
        lambda _: eqbal("perform truth"),
    ),
    (   "^bliss(?: (.+))?$",
        "perform bliss []/me",
        lambda matches: eqbal("perform bliss {}".format(matches[0] or "me"))
    ),
    (   "^pur(?: (.+))?$",
        "perform purity []/t",
        lambda matches: eqbal("perform purity {}".format(matches[0] or v.target))
    ),
    (   "^hell(?: (.+))?$",
        "perform hellsight []/t",
        lambda matches: eqbal("perform hellsight {}".format(matches[0] or v.target))
    ),
    (   "^pilg(?: (.+))?$",
        "perform pilg [] / perf right of pilg",
        lambda matches: pilgrimage(matches)
    ),
    (   "^insp$",
        "perform inspiration",
        lambda matches: eqbal("perform inspiration")
    ),
    (   "^pheal$",
        "perform rite of healing",
        lambda matches: eqbal("perform rite of healing")
    ),
    (   "^demons$",
        "perform right of demons",
        lambda matches: eqbal("perform rite of demons")
    ),
    (   "^piety$",
        "perform right of piety",
        lambda matches: eqbal("perform rite of piety")
    ),
]
add_aliases("ab_devotion", devotion_aliases)

def channel_all(client, matches):
    
    for chan in ["air", "fire", "water", "earth", "spirit"]:
        eqbal("channel {}".format(chan), mud=client)


