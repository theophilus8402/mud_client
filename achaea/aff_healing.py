
from .client import send, add_aliases, add_triggers
from .basic import eqbal, eat_herb
from .variables import v


aff_healing_aliases = [
    (   "^dh$",
        "drink health",
        lambda m: send("drink health"),
    ),
    (   "^dm$",
        "drink mana",
        lambda m: send("drink mana"),
    ),
    (   "^moss$",
        "eat moss",
        lambda m: eat_herb("moss"),
    ),
    (   "^broot$",
        "eat bloodroot",
        lambda m: eat_herb("bloodroot"),
    ),
    (   "^coh$",
        "eat cohosh",
        lambda m: eat_herb("cohosh"),
    ),
    (   "^kelp$",
        "eat kelp",
        lambda m: eat_herb("kelp"),
    ),
    (   "^pear$",
        "eat pear",
        lambda m: eat_herb("pear"),
    ),
    (   "^pot$",
        "eat potash",
        lambda m: eat_herb("potash"),
    ),
    (   "^bay$",
        "eat bayberry",
        lambda m: eat_herb("bayberry"),
    ),
    (   "^gin$",
        "eat ginseng",
        lambda m: eat_herb("ginseng"),
    ),
    (   "^gold$",
        "eat goldenseal",
        lambda m: eat_herb("goldenseal"),
    ),
    (   "^kola$",
        "eat kola",
        lambda m: eat_herb("kola"),
    ),
    (   "^ash$",
        "eat ash",
        lambda m: eat_herb("ash"),
    ),
    (   "^bell$",
        "eat bellwort",
        lambda m: eat_herb("bellwort"),
    ),
    (   "^ech$",
        "eat echinacea",
        lambda m: eat_herb("echinacea"),
    ),
    (   "^haw$",
        "eat hawthorn",
        lambda m: eat_herb("hawthorn"),
    ),
    (   "^lob$",
        "eat lobelia",
        lambda m: eat_herb("lobelia"),
    ),
    (   "^ging$",
        "eat ginger",
        lambda m: eat_herb("ginger"),
    ),
    (   "^eskull$",
        "eat skullcap",
        lambda m: eat_herb("skullcap"),
    ),
    (   "^sil$",
        "apply sileris",
        lambda m: send("outr sileris;apply sileris"),
    ),
]
add_aliases("healing", aff_healing_aliases)


elixirs_aliases = {
    (   "^speed$",
        "drink speed",
        lambda m: send("drink speed"),
    ),
    (   "^frost$",
        "drink frost",
        lambda m: send("drink frost"),
    ),
    (   "^imm$",
        "drink immunity",
        lambda m: send("drink immunity"),
    ),
    (   "^levi$",
        "drink levitation",
        lambda m: send("drink levitation"),
    ),
    (   "^venom$",
        "drink venom",
        lambda m: send("drink venom"),
    ),
}
add_aliases("elixirs", elixirs_aliases)

salves_aliases = {
    (   "^calor$",
        "apply caloric",
        lambda m: send("apply caloric"),
    ),
    (   "^epi$",
        "apply epidermal to torso",
        lambda m: send("apply epidermal to torso"),
    ),
    (   "^mass$",
        "apply mass",
        lambda m: send("apply mass"),
    ),
    (   "^mend$",
        "apply mending",
        lambda m: send("apply mending"),
    ),
    (   "^mendl$",
        "apply mending to legs",
        lambda m: send("apply caloric"),
    ),
    (   "^menda$",
        "apply mending to arms",
        lambda m: send("apply mending to arms"),
    ),
    (   "^resto$",
        "apply restoration",
        lambda m: send("apply restoration"),
    ),
    (   "^restol$",
        "apply restoration to legs",
        lambda m: send("apply restoration to legs"),
    ),
    (   "^restoa$",
        "apply restoration to arms",
        lambda m: send("apply restoration to arms"),
    ),
}
add_aliases("salves", salves_aliases)

pipes_aliases = {
    (   "^lp$",
        "light pipes",
        lambda m: send("light pipes"),
    ),
    (   "^skull$",
        "smoke pipe with skullcap",
        lambda m: send("light pipes;smoke pipe with skullcap"),
    ),
    (   "^val$",
        "smoke pipe with valerian",
        lambda m: send("light pipes;smoke pipe with valerian"),
    ),
    (   "^elm$",
        "smoke pipe with elm",
        lambda m: send("light pipes;smoke pipe with elm"),
    ),
}
add_aliases("pipes", pipes_aliases)


"""
def multiple_ally(client, matches):
    for person in matches[0].split(" "):
        client.send("ally {}".format(person))

def multiple_enemy(client, matches):
    for person in matches[0].split(" "):
        client.send("enemy {}".format(person))

misc_aliases = {
    "^rat (.*)$" : ratting,
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

def exits(mud, matches):
    print("exits: {}".format(matches[0]))
    #pass

"""
