
from .variables import v
from .basic import eqbal


def pilgrimage(matches):
    if matches[0]:
        eqbal("perform pilgrimage {}".format(matches[0]))
    else:
        eqbal("perform rite of pilgrimage")

devotion_aliases = [
    (   "^hh(?: (.+))?$",
        "perform hands []",
        lambda matches: eq_bal("perform hands {}".format(matches[0] or ""))
    ),
    (   "^truth$",
        "perform truth",
        lambda _: eq_bal("perform truth"),
    ),
    (   "^bliss(?: (.+))?$",
        "perform bliss []/me",
        lambda matches: eq_bal("perform bliss {}".format(matches[0] or "me"))
    ),
    (   "^pur(?: (.+))?$",
        "perform purity []/t",
        lambda matches: eq_bal("perform purity {}".format(matches[0] or v.target))
    ),
    (   "^hell(?: (.+))?$",
        "perform hellsight []/t",
        lambda matches: eq_bal("perform hellsight {}".format(matches[0] or v.target))
    ),
    (   "^pilg(?: (.+))?$",
        "perform pilg [] / perf right of pilg",
        lambda matches: pilgrimage(matches)
    ),
    (   "^insp$"
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
]

def channel_all(client, matches):
    
    for chan in ["air", "fire", "water", "earth", "spirit"]:
        eq_bal("channel {}".format(chan), mud=client)

def get_aliases():

    aliases = {}
    aliases["ab_devotion"] = devotion_aliases
    return aliases

def get_triggers():
    triggers = {}
    return triggers

