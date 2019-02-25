
from .client import send, add_aliases, add_triggers
from .variables import v
from .basic import eqbal


def sear(client, matches):
    print("searing!")
    if not matches[0]:
        eqbal("angel sear {}".format(v.target), mud=client)
    elif matches[0] in {"n", "ne", "e", "se", "s", "sw", "w", "nw", "u",
                        "d", "in", "out"}:
        eqbal("stand;angel sear icewall {}".format(matches[0]), mud=client)
    else:
        eqbal("angel sear {}".format(matches[0]), mud=client)


spirituality_aliases = [
    (   "^m$",
        "smite t",
        lambda matches: eqbal("stand;smite {}".format(v.target))
    ),
    (   "^shd(?: (.+))?$",
        "angel aura 'me'/[]",
        lambda matches: eqbal("stand;angel aura {}".format(
            matches[0] or ""))
    ),
    (   "^shine(?: (.+))?$",
        "angel shine []",
        lambda matches: eqbal("angel shine {}".format(matches[0] or ""))
    ),
    (   "^cham$",
        "smite t chasten t mind",
        lambda _: eqbal("smite {t} chasten {t} mind".format(t=v.target))
    ),
    (   "^chab$",
        "smite t chasten t body",
        lambda _: "stand;smite {t} chasten {t} body".format(t=v.target)
    ),
    (   "^seek(?: (.+))?$",
        "angel seek t/[]",
        lambda matches: eqbal("angel seek {}".format(matches[0] or v.target))
    ),
    (   "^judge(?: (.+))?$",
        "judge t/[]",
        lambda matches: eqbal("judge {}".format(matches[0] or v.target))
    ),
    (   "^strip(?: (.+))?$",
        "angel strip t/[]",
        lambda matches: eqbal("angel strip {}".format(matches[0] or v.target))
    ),
    (   "^sear(?: (.+))?$",
        "sear t/icewalldir",
        lambda _: sear
    ),
    (   "^ward$",
        "angel ward",
        lambda _: eqbal("angel ward")
    ),
    (   "^pres$",
        "angel presences",
        lambda _: eqbal("angel presences")
    ),
    (   "^trace(?: (.+))?$",
        "angel trace t/[]",
        lambda matches: eqbal("angel trace {}".format(matches[0] or v.target))
    ),
    (   "^sap(?: (.+))?$",
        "angel sap t/[]",
        lambda matches: eqbal("angel sap {}".format(matches[0] or v.target))
    ),
    (   "^care(?: (.+))?$",
        "angel care []",
        lambda matches: eqbal("angel care {}".format(matches[0]))
    ),
    (   "^wra(?: (.+))?$",
        "angel spiritwrack t/[]",
        lambda matches: eqbal("angel spiritwrack {}".format(matches[0] or v.target))
    ),
    (   "^emp(?: (.+))?$",
        "angel empathy []",
        lambda mud, matches: eqbal("angel empathy {}".format(matches[0] or ""))
    ),
    (   "^cont$",
        "contemplate t",
        lambda _: eqbal("contemplate {}".format(v.target))
    ),
    (   "^sacri$",
        "angel sacrifice",
        lambda _: eqbal("angel sacrifice")
    ),
    (   "^absolve$",
        "angel absolve t",
        lambda _: eqbal("angel absolve {}".format(v.target))
    ),
]
add_aliases("ab_spirituality", spirituality_aliases)

spirituality_triggers = [
    (   "^White strands of light weave themselves together before your eyes, and within seconds you hold a spiritual mace within your grasp.$",
        # you're mace is here! wield it!
        lambda _: eqbal("wield mace")
    ),
]
add_triggers(spirituality_triggers)

