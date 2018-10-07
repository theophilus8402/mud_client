
from .variables import v
from .client import client,send

queue_triggers = [
    (   "^\[System\]: Running queued eqbal command: (.*)$",
        # catch lines for system eqbal
        lambda m: print("Found eqbal: {}".format(m[0]))
    )
]


spirituality_aliases = [
    (   "^m$",
        "attack",
        lambda m: send("smite {}".format(v.target))
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
    return triggers

