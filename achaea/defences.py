
import asyncio

from .basic import eqbal, curebal
from .client import client, send, echo, add_aliases, add_triggers, add_gmcp_handler
from .variables import v

def gmcp_defences(gmcp_data):
    v.defences = [defence["name"] for defence in gmcp_data]
add_gmcp_handler("Char.Defences.List", gmcp_defences)

def defences(matches):
    current_defences = set(v.defences)
    total_defences = set(defence_info.keys())
    needed_defences = total_defences.difference(current_defences)
    echo("Needed defences: {}".format(needed_defences))

    # queue up the actions to gain the defences
    for defence in needed_defences:
        defence_info[defence]()

    if needed_defences.intersection(bliss_defs):
        eqbal("perform bliss me")

defence_triggers = [
    (   "^You have the following defences:$",
        # list of defences
        defences,
    ),
]
add_triggers(defence_triggers)

def do_nothing():
    pass

bliss_defs = {"constitution", "toughness", "resistance"}

defence_info = {
    "preachblessing" : lambda: do_nothing,
    "boartattoo" : lambda: eqbal("touch boar"),
    "mosstattoo" : lambda: eqbal("touch moss"),
    "deathsight" : lambda: send("outr skullcap;eat skullcap"),
    "constitution" : lambda: echo("Missing CONSTITUTION"),
    "toughness" : lambda: echo("Missing TOUGHNESS"),
    "resistance" : lambda: echo("Missing RESISTANCE"),
    "mindseye" : lambda: eqbal("touch mindseye"),
    "deafness" : lambda: curebal("hawthorn"),
    "blindness" : lambda: curebal("bayberry"),
    "kola" : lambda: curebal("kola"),
    "temperance" : lambda: curebal("frost"),
    "speed" : lambda: curebal("speed"),
    "levitating" : lambda: curebal("levitation"),
    "poisonresist" : lambda: curebal("venom"),
    "insulation" : lambda: curebal("caloric"),
    "thirdeye" : lambda: curebal("echinacea"),
    "nightsight" : lambda: eqbal("nightsight"),
    "selfishness" : lambda: eqbal("selfishness"),
    "fangbarrier" : lambda: curebal("sileris"),
    "insomnia" : lambda: curebal("cohosh"),
    "cloak" : lambda: eqbal("touch cloak"),
}

"""
['preachblessing', 'boartattoo', 'mosstattoo', 'deathsight', 'constitution', 'resistance', 'toughness', 'mindseye', 'deafness', 'blindness', 'kola', 'temperance', 'speed', 'levitating', 'poisonresist', 'insulation', 'thirdeye', 'nightsight', 'selfishness', 'fangbarrier', 'insomnia', 'cloak']
"""

"""
You have the following defences:
preachblessing
boartattoo
mosstattoo
deathsight
constitution
resistance
toughness
mindseye
deafness
blindness
insomnia
kola
temperance
speed
levitating
poisonresist
insulation
thirdeye
nightsight
selfishness
fangbarrier
You are benefitting from a 10% bonus to experience gain.
You are protected by 21 defences.
"""

"""
bliss:
    constitution to prevent nausea
    toughness
channels?
Curseward
Deathsight
Mindseye
Cloak
insomnia
blind
deaf
speed
levitation
kola
frost
caloric
mass
thirdeye
nightsight
selfishness
rebounding
venom
sileris
magic/cold/fire/electric resistances (if you have the enchantments)

"""

