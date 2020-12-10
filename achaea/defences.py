import asyncio

from achaea.basic import curebal, eqbal
from achaea.state import s
from client import c, echo, send
from client.timers import timers


def gmcp_defences(gmcp_data):
    s.defences = tuple(defence["name"] for defence in gmcp_data)


c.add_gmcp_handler("Char.Defences.List", gmcp_defences)


def gmcp_defences_add(gmcp_data):
    defence = gmcp_data["name"]
    # echo(f"Woo!  We've gained {defence}!")
    s.defences = (*s.defences, defence)


c.add_gmcp_handler("Char.Defences.Add", gmcp_defences_add)


def gmcp_defences_remove(gmcp_data):
    lost_defences = set(gmcp_data)
    echo(f"Egads!  We've lost {lost_defences}!")
    s.defences = tuple(set(s.defences).difference(lost_defences))
    # defences("")


c.add_gmcp_handler("Char.Defences.Remove", gmcp_defences_remove)


def add_wanted_defence(wanted_defences, defence):
    return tuple(set(wanted_defences).union({defence}))


def add_wanted_defences(wanted_defences, new_defences):
    return tuple(set(wanted_defences).union(set(new_defences)))


def remove_wanted_defence(wanted_defences, defence):
    return tuple(set(wanted_defences).difference({defence}))


def remove_wanted_defences(wanted_defences, remove_defences):
    return tuple(set(wanted_defences).difference(set(remove_defences)))


def relax(defence, delay=5):
    auto_defences([defence], "off")
    timers.add(f"turnon_{defence}", lambda: auto_defences([defence], "on"), 5)
    eqbal(f"relax {defence}")


def fighting_defences(matches):
    if matches == "on":
        echo("Adding fighting defences!!")
        s.wanted_defences = add_wanted_defences(s.wanted_defences, fighting_defs)
        for fdef in fighting_defs:
            set_defence(fdef, 25, state=s)
    elif matches == "off":
        echo("Removing fighting defences!!")
        s.wanted_defences = remove_wanted_defences(s.wanted_defences, fighting_defs)
        for fdef in fighting_defs:
            set_defence(fdef, 0, state=s)


def get_needed_defences(current_defences, wanted_defences):
    return tuple(set(wanted_defences).difference(set(current_defences)))


def defences(matches, fighting=False):
    needed_defences = get_needed_defences(s.defences, s.wanted_defences)
    echo(f"Needed defences: {needed_defences}")

    c.remove_temp_trigger("defences_trigger")


defences_trigger = (
    "^You have the following defences:$",
    # list of defences
    defences,
)


def check_defences(matches):
    eqbal("def")
    c.add_temp_trigger("defences_trigger", defences_trigger)


def auto_defences(defs, state):
    if state == "on":
        for defence in defs:
            echo(f"Auto {defence} on!!!")
            send(f"CURING PRIORITY DEFENCE {defence} 25")
    elif state == "off":
        for defence in defs:
            echo(f"Auto {defence} off!!!")
            send(f"CURING PRIORITY DEFENCE {defence} reset")


auto_defs = ["mass"]


def set_basic_defs(matches):
    global basic_defs
    for bdef in basic_defs:
        set_defence(bdef, 25, state=s)


defence_aliases = [
    (
        "^cdef$",
        "list of defences",
        check_defences,
    ),
    (
        "^fdef(?: (.+))?$",
        "fighting defences",
        lambda matches: fighting_defences(matches[0] or "on"),
    ),
    (
        "^sdef_basic$",
        "set basic defences to 25",
        set_basic_defs,
    ),
    (
        "^adef on$",
        "auto defences",
        lambda matches: auto_defences(auto_defs, "on"),
    ),
    (
        "^adef off$",
        "auto defences",
        lambda matches: auto_defences(auto_defs, "off"),
    ),
    (
        "^adef (.+) (.+)$",
        "auto defences",
        lambda matches: auto_defences([matches[0]], matches[1]),
    ),
    (
        r"^relax (\w+)$",
        "relax defence 5",
        lambda matches: relax(matches[0], "5"),
    ),
    (
        r"^relax (\w+) (\d+)$",
        "relax defence #sec",
        lambda matches: relax(matches[0], matches[1]),
    ),
]
c.add_aliases("defences", defence_aliases)


def do_nothing():
    pass


bliss_defs = {"constitution", "toughness", "resistance"}

# these will be defs we keep on all the time
basic_defs = {
    # "boartattoo",
    "mosstattoo",
    "deathsight",
    "insomnia",
    # "lifevision",
    "mindseye",
    "selfishness",
    "cloak",
    "deafness",
    "blindness",
    "thirdeye",
    "nightsight",
    # "shroud",
}
s.wanted_defences = tuple(basic_defs)


def set_defence(defence, priority, state=s):
    setattr(state, defence, priority)
    if priority == 0:
        priority = "reset"
    send(f"CURING PRIORITY DEFENCE {defence} {priority}")


# these will be setup and kept up when we need to fight
fighting_defs = {
    "kola",
    "temperance",
    "speed",
    "levitating",
    "poisonresist",
    "insulation",
    "fangbarrier",
}


defence_info = {
    "preachblessing": lambda: do_nothing,
    "boartattoo": lambda: eqbal("touch boar"),
    "mosstattoo": lambda: eqbal("touch moss"),
    "deathsight": lambda: send("outr skullcap;eat skullcap"),
    # "deathsight" : lambda: eqbal("astralvision"),
    # "lifevision" : lambda: eqbal("astralvision"),
    "constitution": lambda: echo("Missing CONSTITUTION"),
    "toughness": lambda: echo("Missing TOUGHNESS"),
    "resistance": lambda: echo("Missing RESISTANCE"),
    "mindseye": lambda: eqbal("touch mindseye"),
    "deafness": lambda: curebal("hawthorn"),
    "blindness": lambda: curebal("bayberry"),
    "kola": lambda: curebal("kola"),
    "temperance": lambda: curebal("frost"),
    "speed": lambda: curebal("speed"),
    "levitating": lambda: curebal("levitation"),
    "poisonresist": lambda: curebal("venom"),
    "insulation": lambda: curebal("caloric"),
    "thirdeye": lambda: curebal("echinacea"),
    "nightsight": lambda: eqbal("nightsight"),
    "selfishness": lambda: eqbal("selfishness"),
    "fangbarrier": lambda: curebal("sileris"),
    "insomnia": lambda: curebal("insomnia"),
    "cloak": lambda: eqbal("touch cloak"),
    "shroud": lambda: eqbal("shroud"),
}
