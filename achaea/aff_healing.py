
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
        "eat hawthorne",
        lambda m: eat_herb("hawthorne"),
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
    "^frost$" : "drink frost",
    "^imm$" : "drink immunity",
    "^levi$" : "drink levitation",
    "^speed$" : "drink speed",
    "^venom$" : "drink venom",
}
#add_aliases("elixirs", elixirs_aliases)

salves_aliases = {
    "^calor$" : "apply caloric",
    "^epi$" : "apply epidermal to torso",
    "^mass$" : "apply mass",
    "^mend$" : "apply mending",
    "^mendl$" : "apply mending to legs",
    "^menda$" : "apply mending to arms",
    "^resto$" : "apply restoration",
    "^restol$" : "apply restoration to legs",
    "^restoa$" : "apply restoration to arms",
}
#add_aliases("salves", salves_aliases)

pipes_aliases = {
    "^lp$" : "light pipes",
    "^skull$" : "light pipes;smoke pipe with skullcap",
    "^val$" : "light pipes;smoke pipe with valerian",
    "^elm$" : "light pipes;smoke pipe with elm",
}
#add_aliases("pipes", pipes_aliases)


"""
def channel_all(client, matches):
    
    for chan in ["air", "fire", "water", "earth", "spirit"]:
        eq_bal("channel {}".format(chan), mud=client)

healing_aliases = {
    "^hdb$" : lambda mud, matches: eq_bal("heal {} blindness;heal {} deafness".format(mud.v.target, mud.v.target)),
    "^chans$" : channel_all,
}


def multiple_ally(client, matches):
    for person in matches[0].split(" "):
        client.send("ally {}".format(person))

def multiple_enemy(client, matches):
    for person in matches[0].split(" "):
        client.send("enemy {}".format(person))

misc_aliases = {
    "^pg$" : "put coins in pack",
    "^gg$" : "get gold",
    "^gp (.+)$" : lambda mud, matches: "get {} gold from pack".format(matches[0]),
    "^rat$" : rat,
    "^rat (.*)$" : ratting,
    "^men (.+)$" : multiple_enemy,
    "^mall (.+)$" : multiple_ally,
}

anti_theft_aliases = {
    "^self$" : "selfishness",
    "^gener$" : "generosity",
}

occultism_aliases = {
    "^ague(?: (.+))?$" : lambda mud, matches: eq_bal("ague {}".format(matches[0] or mud.v.target)),
    "^agl(?: (.+))?$" : lambda mud, matches: eq_bal("auraglance {}".format(matches[0] or mud.v.target)),
    "^bwarp$" : eq_bal("bodywarp"),
    "^att(?: (.+))?$" : lambda mud, matches: eq_bal("attend {}".format(matches[0] or mud.v.target)),
    "^ene(?: (.+))?$" : lambda mud, matches: eq_bal("enervate {}".format(matches[0] or mud.v.target)),
    "^qui(?: (.+))?$" : lambda mud, matches: eq_bal("quicken {}".format(matches[0] or mud.v.target)),
    "^sarm(?: (.+))?$" : lambda mud, matches: eq_bal("shrivel arms {}".format(mud.v.target)),
    "^sleg(?: (.+))?$" : lambda mud, matches: eq_bal("shrivel legs {}".format(mud.v.target)),
    "^twarp(?: (.+))?$" : eq_bal("timewarp"),
    "^daura(?: (.+))?$" : eq_bal("distortaura"),
    "^pclk(?: (.+))?$" : lambda mud, matches: eq_bal("pinchaura {} cloak".format(matches[0] or mud.v.target)),
    "^pspe(?: (.+))?$" : lambda mud, matches: eq_bal("pinchaura {} speed".format(mud.v.target)),
    "^pcalor(?: (.+))?$" : lambda mud, matches: eq_bal("pinchaura {} caloric".format(mud.v.target)),
    "^pfrost(?: (.+))?$" : lambda mud, matches: eq_bal("pinchaura {} frost".format(mud.v.target)),
    "^plevi(?: (.+))?$" : lambda mud, matches: eq_bal("pinchaura {} levitation".format(mud.v.target)),
    "^pinsom(?: (.+))?$" : lambda mud, matches: eq_bal("pinchaura {} insomnia".format(mud.v.target)),
    "^pkola(?: (.+))?$" : lambda mud, matches: eq_bal("pinchaura {} kola".format(mud.v.target)),
    "^spe(?: (.+))?$" : eq_bal("unnamable speak"),
    "^vis(?: (.+))?$" : eq_bal("unnamable vision"),
    "^devo(?: (.+))?$" : lambda mud, matches: eq_bal("devolve {}".format(mud.v.target)),
    "^caura(?: (.+))?$" : lambda mud, matches: eq_bal("cleanseaura {}".format(mud.v.target)),
    "^tent(?: (.+))?$" : eq_bal("tentacles"),
    "^inst(?: (.+))?$" : lambda mud, matches: instill(matches[0] or mud.v.target),
    "^whisp$" : lambda mud, matches: eq_bal("whisperingmadness {}".format(mud.v.target)),
    "^dev$" : eq_bal("devilmark"),
    "^enl$" : lambda mud, matches: eq_bal("enlighten {}".format(matches[0] or mud.v.target)),
    "^ast$" : eq_bal("astralform"),
    "^devo$" : lambda mud, matches: eq_bal("unravel mind of {}".format(mud.v.target)),
    "^ra$" : lambda mud, matches: eq_bal("readaura {}".format(mud.v.target)),
}

tarot_aliases = {
    "^sun$" : eq_bal("fling sun at ground"),
    "^priest(?: (.+))?$" : lambda mud, matches: eq_bal("fling priestess at {}".format(matches[0] or "me")),
    "^magi(?: (.+))?$" : lambda mud, matches: eq_bal("fling magician at {}".format(matches[0] or "me")),
    "^fool(?: (.+))?$" : lambda mud, matches: eq_bal("fling fool at {}".format(matches[0] or "me")),
    "^hang(?: (.+))?$" : lambda mud, matches: eq_bal("fling hangedman at {}".format(matches[0] or mud.v.target)),
    "^star(?: (.+))?$" : lambda mud, matches: eq_bal("fling star at {}".format(matches[0] or mud.v.target)),
    "^just(?: (.+))?$" : lambda mud, matches: eq_bal("fling justice at {}".format(matches[0] or mud.v.target)),
    "^aeon(?: (.+))?$" : lambda mud, matches: eq_bal("fling aeon at {}".format(matches[0] or mud.v.target)),
    "^lust(?: (.+))?$" : lambda mud, matches: eq_bal("fling lust at {}".format(matches[0] or mud.v.target)),
    "^moon(?: (.+))?$" : lambda mud, matches: eq_bal("fling moon at {}".format(matches[0] or mud.v.target)),
    "^devil(?: (.+))?$" : lambda mud, matches: eq_bal("fling devil at ground"),
    "^univ(?: (.+))?$" : lambda mud, matches: eq_bal("fling universe at ground"),
}

domination_aliases = {
    "^derv(?: (.+))?$" : lambda mud, matches: command_ent("dervish", matches[0] or mud.v.target),
    "^syc(?: (.+))?$" : lambda mud, matches: command_ent("sycophant", matches[0] or mud.v.target),
    "^grem(?: (.+))?$" : lambda mud, matches: command_ent("gremlin", matches[0] or mud.v.target),
    "^orb(?: (.+))?$" : lambda mud, matches: command_ent("orb", matches[0] or "me"),
    "^leech(?: (.+))?$" : lambda mud, matches: command_ent("bloodleech", matches[0] or mud.v.target),
    "^leechon$" : auto_ent("bloodleech", on=True),
    "^leechoff$" : auto_ent("bloodleech", on=False),
    "^nem(?: (.+))?$" : lambda mud, matches: command_ent("nemesis", matches[0] or mud.v.target),
    "^nemon$" : auto_ent("nemesis", on=True),
    "^nemoff$" : auto_ent("nemesis", on=False),
    "^poss$" : lambda mud, matches: mud.send("order soulmaster possess {}".format(mud.v.target)),
    "^osp$" : lambda mud, matches: mud.send("order {} smoke pipe with skullcap".format(mud.v.target)),
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

def target(mud, matches):
    mud.v.target = matches[0]
    print("new target: {}".format(mud.v.target))

def attack(mud, _):
    #mud.send("stand\nwarp {}".format(mud.v.target))
    eq_bal("stand;smite {}".format(mud.v.target), mud=mud)

def echo(msg, mud=None):
    if mud:
        print(msg, end="")
    else:
        return lambda mud,_: print(msg, end="")

def exits(mud, matches):
    print("exits: {}".format(matches[0]))
    #pass

"""
