

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


