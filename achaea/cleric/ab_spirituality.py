
from ..client import send, c
from ..state import s
from ..basic import eqbal


def sear(matches):
    print("searing!")
    if not matches[0]:
        eqbal(f"angel sear &tar")
    elif matches[0] in {"n", "ne", "e", "se", "s", "sw", "w", "nw", "u",
                        "d", "in", "out"}:
        eqbal(f"stand;angel sear icewall {matches[0]}")
    else:
        eqbal(f"angel sear {matches[0]}")


spirituality_aliases = [
    (   "^m$",
        "smite t",
        lambda matches: eqbal(f"stand;smite &tar")
    ),
    (   "^cham$",
        "smite t chasten t mind",
        lambda _: eqbal(f"smite &tar chasten mind")
    ),
    (   "^chab$",
        "smite t chasten t body",
        lambda _: send(f"stand;smite &tar chasten body")
    ),
    (   "^pchab$",
        "penance;smite t chasten t body",
        lambda _: eqbal(f"stand;recite penance &tar;smite &tar chasten body")
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
        lambda matches: eqbal(f"stand;angel aura {matches[0] or ''}")
    ),
    (   "^pan(?: (.+))?$",
        "angel panic t/[]",
        lambda matches: eqbal(f"angel panic {matches[0] or '&tar'}")
    ),
    (   "^watch (.+)$",
        "angel watch []",
        lambda matches: eqbal(f"angel watch {matches[0]}")
    ),
    (   "^smam$",
        "smash arms t chasten mind",
        lambda _: eqbal(f"smash arms &tar chasten mind")
    ),
    (   "^smlb$",
        "smash legs t chasten mind",
        lambda _: eqbal(f"smash legs &tar chasten body")
    ),
    (   "^her$",
        "hunt heresy",
        lambda matches: eqbal("hunt heresy")
    ),
    (   "^seek(?: (.+))?$",
        "angel seek t/[]",
        lambda matches: eqbal(f"angel seek {matches[0] or '&tar'}")
    ),
    (   "^apush (.+)$",
        "angel seek t",
        lambda matches: eqbal(f"angel push {matches[0] or '&tar'}")
    ),
    (   "^abeck$",
        "angel beckon all",
        lambda matches: eqbal("angel beckon")
    ),
    (   "^beck$",
        "angel beckon t",
        lambda matches: eqbal(f"angel beckon {matches[0] or '&tar'}")
    ),
    (   "^sear(?: (.+))?$",
        "sear t/icewalldir",
        lambda matches: sear(matches)
    ),
    (   "^judge(?: (.+))?$",
        "judge t/[]",
        lambda matches: eqbal(f"judge {matches[0] or '&tar'}")
    ),
    (   "^strip(?: (.+))?$",
        "angel strip t/[]",
        lambda matches: eqbal(f"angel strip {matches[0] or '&tar'}")
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
        lambda matches: eqbal(f"angel trace {matches[0] or '&tar'}")
    ),
    (   "^sap(?: (.+))?$",
        "angel sap t/[]",
        lambda matches: eqbal(f"angel sap {matches[0] or '&tar'}")
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
        lambda _: eqbal(f"contemplate &tar")
    ),
    (   "^sacri$",
        "angel sacrifice",
        lambda _: eqbal("angel sacrifice")
    ),
    (   "^absolve$",
        "angel absolve t",
        lambda _: eqbal(f"angel absolve &tar")
    ),
]
c.add_aliases("ab_spirituality", spirituality_aliases)

spirituality_triggers = [
    (   "^White strands of light weave themselves together before your eyes, and within seconds you hold a spiritual mace within your grasp.$",
        # you're mace is here! wield it!
        lambda _: eqbal("wield mace;attach fist to mace")
    ),
]
c.add_triggers(spirituality_triggers)

