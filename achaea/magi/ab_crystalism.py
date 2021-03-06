from client import c, echo, send

from ..basic import eqbal
from ..state import s


def spin_crystals(crystals):
    commands = [f"outr {crystal};spin {crystal}" for crystal in crystals]
    return ";".join(commands)


def spin_n_embed(vibration, extra_args=""):
    spins = spin_crystals(crystal_map[vibration])
    eqbal(f"stand;{spins};embed {vibration} {extra_args}")


crystal_map = {
    "dissipate": ["pentagon"],
    "palpitation": ["cylinder"],
    "heat": ["pyramid"],
    "alarm": ["spiral"],
    "tremors": ["disc", "egg"],
    "reverberation": ["disc", "pentagon"],
    "sonicportal": ["sphere", "torus"],
    "adduction": ["disc", "polyhedron"],
    "harmony": ["egg", "sphere"],
    "creeps": ["torus"],
    "silence": ["egg"],
    "revelation": ["cube", "diamond"],
    "grounding": ["sphere"],
    "oscillate": ["diamond"],
    "focus": ["pyramid"],
    "disorientation": ["spiral"],
    "energise": ["polyhedron"],
    "stridulation": ["cylinder", "polyhedron"],
    "gravity": ["egg", "torus"],
    "forest": ["diamond", "pyramid"],
    "dissonance": ["cylinder", "sphere", "spiral"],
    "lullaby": ["pyramid"],
    "retardation": ["disc"],
    "cataclysm": [
        "cylinder",
        "cube",
        "diamond",
        "disc",
        "egg",
        "pentagon",
        "polyhedron",
        "pyramid",
        "spiral",
        "sphere",
        "torus",
    ],
}


def next_vibration(matches):
    vibes = [
        "dissipate",
        "palpitation",
        "harmony",
        "oscillate",
        "disorientation",
        "energise",
        "stridulation",
    ]
    if matches:
        vibes = vibes[int(matches[0]) :]

    for vibe in vibes:
        yield spin_n_embed(vibe)


crystalism_aliases = [
    (
        "^diss$",
        "dissipate - attack mana",
        lambda matches: spin_n_embed("dissipate"),
    ),
    (
        "^palp$",
        "palpitation - dmg",
        lambda matches: spin_n_embed("palpitation"),
    ),
    (
        "^heat$",
        "heat - counteract cold weather",
        lambda matches: spin_n_embed("heat"),
    ),
    (
        "^alarm$",
        "alarm",
        lambda matches: spin_n_embed("alarm"),
    ),
    (
        "^trem$",
        "tremors - knockdown / strip levitation",
        lambda matches: spin_n_embed("tremors"),
    ),
    (
        "^reverb$",
        "reverberation - protect vibes",
        lambda matches: spin_n_embed("reverberation"),
    ),
    (
        "^portal(?: (.+))?$",
        "portal []/t",
        lambda matches: spin_n_embed("sonicportal", matches[0] or s.target),
    ),
    (
        "^add$",
        "adduction - suck in people",
        lambda matches: spin_n_embed("adduction"),
    ),
    (
        "^crystalhome$",
        "crystalhome",
        lambda matches: eqbal("crystalhome"),
    ),
    (
        "^harm$",
        "harmony - heal affs or health/mana",
        lambda matches: spin_n_embed("harmony"),
    ),
    (
        "^tharmh$",
        "tune harmony healing",
        lambda matches: eqbal("tune harmony healing"),
    ),
    (
        "^tharmr$",
        "tune harmony restoration",
        lambda matches: eqbal("tune harmony restoration"),
    ),
    (
        "^creeps$",
        "creeps - shyness",
        lambda matches: spin_n_embed("creeps"),
    ),
    (
        "^silence$",
        "silence",
        lambda matches: spin_n_embed("silence"),
    ),
    (
        "^revel$",
        "revelation - conceal peeps",
        lambda matches: spin_n_embed("revelation"),
    ),
    (
        "^ground$",
        "grounding - make it difficult to be moved",
        lambda matches: spin_n_embed("grounding"),
    ),
    (
        "^osc$",
        "oscillate - gives amnesia",
        lambda matches: spin_n_embed("oscillate"),
    ),
    (
        "^vibes$",
        "vibes all",
        lambda matches: eqbal("vibes all"),
    ),
    (
        "^foc$",
        "focus - bring the pain or vibes",
        lambda matches: spin_n_embed("focus"),
    ),
    (
        "^dis$",
        "disorientation - dizziness",
        lambda matches: spin_n_embed("disorientation"),
    ),
    (
        "^ener$",
        "energise - drain health",
        lambda matches: spin_n_embed("energise"),
    ),
    (
        "^absorb$",
        "absorb energy",
        lambda matches: eqbal("absorb energy"),
    ),
    (
        "^strid$",
        "stridulation - if not deaf, lose eq else may strip deaf",
        lambda matches: spin_n_embed("stridulation"),
    ),
    (
        "^grav$",
        "gravity - pulls peeps out of trees and skies",
        lambda matches: spin_n_embed("gravity"),
    ),
    (
        "^forest$",
        "forest - dmg",
        lambda matches: spin_n_embed("forest"),
    ),
    (
        "^disso$",
        "dissonance - strip defs",
        lambda matches: spin_n_embed("dissonance"),
    ),
    (
        "^plague$",
        "plague - affs",
        lambda matches: spin_n_embed("plague"),
    ),
    (
        "^lull$",
        "lullaby - sleep!",
        lambda matches: spin_n_embed("lullaby"),
    ),
    (
        "^retard$",
        "retardation - slow down!!",
        lambda matches: spin_n_embed("retardation"),
    ),
    (
        "^cataclysm$",
        "cataclysm - whoa",
        lambda matches: spin_n_embed("cataclysm"),
    ),
    (
        r"^vib ?(\d+)?$",
        "next vibe",
        lambda matches: next_vibration(matches),
    ),
]
c.add_aliases("ab_crystalism", crystalism_aliases)
