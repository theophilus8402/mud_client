

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


