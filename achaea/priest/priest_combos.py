import json
import random

from achaea.basic import classbal, eqbal
from achaea.state import s
from achaea.priest.priest_status import conviction, prayer_length, prayer
from client import c, send


with open("achaea/priest/verse_info.json") as f:
    verse_info = json.load(f)


def random_recite():
    """
    recite attend - undeaf
    recite fragility - more damage to next limb attack
    recite condemnation - justice
    guilt - guilt - if they focus, will cure, but also get a new aff
    unflinching - strike through parry + short heresy
    ash - spiritburn - dmg + mana dmg when on fire
    penance - paralysis
    reflection - give affs to them instead of me
    burn - drains mana on applying salves

    rebukes:
    chaos - need 3 verses - hallucinations
    darkness - 2 verses - paranoia
    evil - 3 verses - masochism

    """
    verses = [
        "attend",
        "fragility",
        "condemnation",
        "guilt",
        #"unflinching",  # not super helpful
        "ash",
        "penance",
        "reflection",
        "burn",
    ]
    rebuke = random.choice(["chaos", "darkness", "evil"])
    verse = random.choice(verses)
    return f"recite {verse} {s.target} rebuke {rebuke}"


priest_combo_aliases = [
    (
        "^r$",
        "recite random verse/rebuke",
        lambda m: eqbal(random_recite()),
    ),
    (
        "^rm$",
        "recite random verse/rebuke;smite t chasten mind",
        lambda m: eqbal(f"stand;{random_recite()};smite {s.target} chasten mind"),
    ),
    (
        "^rb$",
        "recite random verse/rebuke;smite t chasten body",
        lambda m: eqbal(f"stand;{random_recite()};smite {s.target} chasten body"),
    ),
]
c.add_aliases("priest_combo", priest_combo_aliases)
