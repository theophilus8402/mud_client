
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
        lambda matches: eqbal(f"stand;smite {v.target}")
    ),
    (   "^cham$",
        "smite t chasten t mind",
        lambda _: eqbal(f"smite {v.target} chasten mind")
    ),
    (   "^chab$",
        "smite t chasten t body",
        lambda _: eqbal(f"stand;smite {v.target} chasten body")
    ),
    (   "^shine(?: (.+))?$",
        "angel shine []",
        lambda matches: eqbal(f"angel shine {matches[0] or ''}")
    ),
    (   "^call$",
        "call mace",
        lambda matches: eqbal("call mace")
    ),
    (   "^shd(?: (.+))?$",
        "angel aura 'me'/[]",
        lambda matches: eqbal("stand;angel aura {}".format(
            matches[0] or ""))
    ),
    (   "^pan(?: (.+))?$",
        "angel panic t/[]",
        lambda matches: eqbal(f"angel panic {matches[0] or v.target}")
    ),
    (   "^watch (.+)$",
        "angel watch []",
        lambda matches: eqbal(f"angel watch {matches[0]}")
    ),
    (   "^smam$",
        "smash arms t chasten mind",
        lambda _: eqbal(f"smash arms {v.target} chasten mind")
    ),
    (   "^smlb$",
        "smash legs t chasten mind",
        lambda _: eqbal(f"smash legs {v.target} chasten body")
    ),
    (   "^her$",
        "hunt heresy",
        lambda matches: eqbal("hunt heresy")
    ),
    (   "^seek(?: (.+))?$",
        "angel seek t/[]",
        lambda matches: eqbal("angel seek {}".format(matches[0] or v.target))
    ),
    (   "^push (.+)$",
        "angel seek t",
        lambda matches: eqbal(f"angel push {matches[0] or v.target}")
    ),
    (   "^abeck$",
        "angel beckon all",
        lambda matches: eqbal("angel beckon")
    ),
    (   "^beck$",
        "angel beckon t",
        lambda matches: eqbal(f"angel beckon {matches[0] or v.target}")
    ),
    (   "^sear(?: (.+))?$",
        "sear t/icewalldir",
        lambda _: sear
    ),
    (   "^judge(?: (.+))?$",
        "judge t/[]",
        lambda matches: eqbal("judge {}".format(matches[0] or v.target))
    ),
    (   "^strip(?: (.+))?$",
        "angel strip t/[]",
        lambda matches: eqbal("angel strip {}".format(matches[0] or v.target))
    ),
    (   "^ripp$",
        "angel ripples",
        lambda matches: eqbal("angel ripples")
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
        lambda matches: eqbal(f"angel trace {matches[0] or v.target}")
    ),
    (   "^sap(?: (.+))?$",
        "angel sap t/[]",
        lambda matches: eqbal(f"angel sap {matches[0] or v.target}")
    ),
    (   "^care(?: (.+))?$",
        "angel care []",
        lambda matches: eqbal(f"angel care {matches[0]}")
    ),
    (   "^refuge$",
        "angel refuge",
        lambda _: eqbal("angel refuge")
    ),
    (   "^emp(?: (.+))?$",
        "angel empathy []",
        lambda matches: eqbal(f"angel empathy {matches[0] or ''}")
    ),
    (   "^cont$",
        "contemplate t",
        lambda _: eqbal(f"contemplate {v.target}")
    ),
    (   "^sacri$",
        "angel sacrifice",
        lambda _: eqbal("angel sacrifice")
    ),
    (   "^absolve$",
        "angel absolve t",
        lambda _: eqbal(f"angel absolve {v.target}")
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

