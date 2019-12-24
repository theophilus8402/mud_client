
import asyncio

from .basic import eqbal, curebal
from .client import client, send, echo, add_aliases, add_triggers, add_gmcp_handler, add_temp_trigger, remove_temp_trigger
from .variables import v

def gmcp_defences(gmcp_data):
    v.defences = {defence["name"] for defence in gmcp_data}
add_gmcp_handler("Char.Defences.List", gmcp_defences)


def gmcp_defences_add(gmcp_data):
    defence = gmcp_data["name"]
    echo(f"Woo!  We've gained {defence}!")
    v.defences.add(defence)
add_gmcp_handler("Char.Defences.Add", gmcp_defences_add)


def gmcp_defences_remove(gmcp_data):
    lost_defences = set(gmcp_data)
    echo(f"Egads!  We've lost {lost_defences}!")
    v.defences.difference_update(lost_defences)
    #defences("")
add_gmcp_handler("Char.Defences.Remove", gmcp_defences_remove)

def fighting_defences(matches):

    if matches == "on":
        echo("Adding fighting defences!!")
        v.wanted_defences.update(fighting_defs)
    elif matches == "off":
        echo("Removing fighting defences!!")
        v.wanted_defences.difference_update(fighting_defs)

def defences(matches, fighting=False):
    current_defences = v.defences
    needed_defences = v.wanted_defences.difference(current_defences)
    echo("Needed defences: {}".format(needed_defences))

    # queue up the actions to gain the defences
    for defence in needed_defences:
        defence_info[defence]()

    """
    # this is for priest
    if needed_defences.intersection(bliss_defs):
        eqbal("perform bliss me")
    """

    remove_temp_trigger("defences_trigger")


defences_trigger = ("^You have the following defences:$",
                    # list of defences
                    defences,
                    ),


def check_defences(matches):
    eqbal("def")
    add_temp_trigger("defences_trigger", defences_trigger[0])


defence_aliases = [
    (   "^cdef$",
        "list of defences",
        check_defences,
    ),
    (   "^fdef(?: (.+))?$",
        "fighting defences",
        lambda matches: fighting_defences(matches[0] or "on"),
    ),
]
add_aliases("defences", defence_aliases)


def do_nothing():
    pass


bliss_defs = {"constitution", "toughness", "resistance"}

# these will be defs we keep on all the time
basic_defs = {
    "boartattoo",
    "mosstattoo",
    "deathsight",
    "lifevision",
    "mindseye",
    "selfishness",
    "cloak",
    "deafness",
    "blindness",
    "thirdeye",
    "nightsight",
}
v.wanted_defences.update(basic_defs)


# these will be setup and kept up when we need to fight
fighting_defs = {
    "kola",
    "insomnia",
    "temperance",
    "speed",
    "levitating",
    "poisonresist",
    "insulation",
    "fangbarrier",
}


# these will be ones for fighting but not all the time
auto_def = {
    # weapon rebounding
    # hold breath
    # mass
}


defence_info = {
    "preachblessing" : lambda: do_nothing,
    "boartattoo" : lambda: eqbal("touch boar"),
    "mosstattoo" : lambda: eqbal("touch moss"),
    #"deathsight" : lambda: send("outr skullcap;eat skullcap"),
    "deathsight" : lambda: eqbal("astralvision"),
    "lifevision" : lambda: eqbal("astralvision"),
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

