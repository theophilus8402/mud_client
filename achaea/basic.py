
from .client import client, send, add_aliases
from .variables import v

def eqbal(msg):
    send("queue add eqbal {}".format(msg))


def eat_herb(herb, mud=None, matches=None):
    send("outr {herb}\neat {herb}".format(herb=herb))


def target(matches):
    v.target = matches[0]
    print("now targeting: {}".format(v.target), file=client.current_out_handle, flush=True)


basic_aliases = [
    (   "^t (.*)$",
        "target",
        target
    ),
    (   "^gg$",
        "get gold",
        lambda m: eqbal("get gold")
    ),
    (   "^pg$",
        "put gold in pack",
        lambda m: eqbal("put gold in pack")
    ),
    (   "^gp (\d+)$",
        "get # gold from pack",
        lambda m: eqbal("get {} gold from pack".format(m[0]))
    ),
]
add_aliases("basic", basic_aliases)


queue_triggers = [
    (   "\[System\]: Running queued eqbal command: (.*)",
        # catch lines for system eqbal
        lambda m: print("Found eqbal: {}".format(m[0]))
    )
]

intro_triggers = [
    #(   "Multi.*",
    #    lambda m: print("Found a match!!")
    #),
    (   "Achaea, Dreams of Divine Lands",
        lambda m: print("Found an achaean match!!")
    )
]

