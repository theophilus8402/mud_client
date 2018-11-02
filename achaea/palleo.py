
from .variables import v
from .basic import eqbal
from .client import client,send


spirituality_aliases = [
    (   "^m$",
        "attack",
        lambda m: eqbal("smite {}".format(v.target))
    ),
]

def target(matches):
    v.target = matches[0]
    print("now targeting: {}".format(v.target))

misc_aliases = [
    (   "^t (.*)$",
        "target",
        target
    ),
]

def get_aliases():

    aliases = {}
    aliases["spirituality"] = spirituality_aliases
    aliases["misc"] = misc_aliases
    return aliases

def get_triggers():

    triggers = {}
    triggers["queue"] = queue_triggers
    triggers["intro"] = intro_triggers
    return triggers

