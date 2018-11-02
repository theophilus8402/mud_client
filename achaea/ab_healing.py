
from .client import send
from .basic import eqbal
from .variables import v


def channel_all(client, matches):
    
    for chan in ["air", "fire", "water", "earth", "spirit"]:
        eq_bal("channel {}".format(chan), mud=client)

healing_aliases = {
    "^hdb$" : lambda mud, matches: eq_bal("heal {} blindness;heal {} deafness".format(mud.v.target, mud.v.target)),
    "^chans$" : channel_all,
}

def get_aliases():
    aliases = {}
    aliases["ab_healing"] = healing_aliases
    return aliases

def get_triggers():
    triggers = {}
    return triggers

misc_aliases = {
    "^men (.+)$" : multiple_enemy,
    "^mall (.+)$" : multiple_ally,
}


direction_aliases = {
    "^n$" : lambda mud,_: move("n", mud),
    "^ne$" : lambda mud,_: move("ne", mud),
    "^nw$" : lambda mud,_: move("nw", mud),
    "^e$" : lambda mud,_: move("e", mud),
    "^s$" : lambda mud,_: move("s", mud),
    "^se$" : lambda mud,_: move("se", mud),
    "^sw$" : lambda mud,_: move("sw", mud),
    "^w$" : lambda mud,_: move("w", mud),
    "^in$" : lambda mud,_: move("in", mud),
    "^out$" : lambda mud,_: move("out", mud),
    "^u$" : lambda mud,_: move("u", mud),
    "^d$" : lambda mud,_: move("d", mud),
    "^rdir$" : lambda mud,_: random_move(mud)
}

def says(mud, matches):
    #print("Found something that is a say!")
    with open("says.txt", "a") as f:
        f.write("{}\n".format(mud.line))

def echo(msg, mud=None):
    if mud:
        print(msg, end="")
    else:
        return lambda mud,_: print(msg, end="")

def exits(mud, matches):
    print("exits: {}".format(matches[0]))
    #pass


