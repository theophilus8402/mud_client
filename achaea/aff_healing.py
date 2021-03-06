from client import c, send

from .basic import eat_herb, eqbal

aff_healing_aliases = [
    (
        "^dh$",
        "drink health",
        lambda m: send("drink health"),
    ),
    (
        "^dm$",
        "drink mana",
        lambda m: send("drink mana"),
    ),
    (
        "^conc$",
        "concentrate",
        lambda m: send("concentrate"),
    ),
    (
        "^moss$",
        "eat moss",
        lambda m: eat_herb("moss"),
    ),
    (
        "^broot$",
        "eat bloodroot",
        lambda m: eat_herb("bloodroot"),
    ),
    (
        "^coh$",
        "eat cohosh",
        lambda m: eat_herb("cohosh"),
    ),
    (
        "^kelp$",
        "eat kelp",
        lambda m: eat_herb("kelp"),
    ),
    (
        "^pear$",
        "eat pear",
        lambda m: eat_herb("pear"),
    ),
    (
        "^pot$",
        "eat potash",
        lambda m: eat_herb("potash"),
    ),
    (
        "^bay$",
        "eat bayberry",
        lambda m: eat_herb("bayberry"),
    ),
    (
        "^gin$",
        "eat ginseng",
        lambda m: eat_herb("ginseng"),
    ),
    (
        "^gold$",
        "eat goldenseal",
        lambda m: eat_herb("goldenseal"),
    ),
    (
        "^kola$",
        "eat kola",
        lambda m: eat_herb("kola"),
    ),
    (
        "^ash$",
        "eat ash",
        lambda m: eat_herb("ash"),
    ),
    (
        "^bell$",
        "eat bellwort",
        lambda m: eat_herb("bellwort"),
    ),
    (
        "^ech$",
        "eat echinacea",
        lambda m: eat_herb("echinacea"),
    ),
    (
        "^haw$",
        "eat hawthorn",
        lambda m: eat_herb("hawthorn"),
    ),
    (
        "^lob$",
        "eat lobelia",
        lambda m: eat_herb("lobelia"),
    ),
    (
        "^ging$",
        "eat ginger",
        lambda m: eat_herb("ginger"),
    ),
    (
        "^eskull$",
        "eat skullcap",
        lambda m: eat_herb("skullcap"),
    ),
    (
        "^sil$",
        "apply sileris",
        lambda m: send("outr sileris;apply sileris"),
    ),
    (
        "^cal$",
        "eat calcite",
        lambda m: eat_herb("calcite"),
    ),
]
c.add_aliases("healing", aff_healing_aliases)


elixirs_aliases = {
    (
        "^speed$",
        "drink speed",
        lambda m: send("drink speed"),
    ),
    (
        "^frost$",
        "drink frost",
        lambda m: send("drink frost"),
    ),
    (
        "^imm$",
        "drink immunity",
        lambda m: send("drink immunity"),
    ),
    (
        "^levi$",
        "drink levitation",
        lambda m: send("drink levitation"),
    ),
    (
        "^venom$",
        "drink venom",
        lambda m: send("drink venom"),
    ),
}
c.add_aliases("elixirs", elixirs_aliases)

salves_aliases = {
    (
        "^calor$",
        "apply caloric",
        lambda m: send("apply caloric"),
    ),
    (
        "^epi$",
        "apply epidermal to torso",
        lambda m: send("apply epidermal to torso"),
    ),
    (
        "^mass$",
        "apply mass",
        lambda m: send("apply mass"),
    ),
    (
        "^mend$",
        "apply mending",
        lambda m: send("apply mending"),
    ),
    (
        "^mendl$",
        "apply mending to legs",
        lambda m: send("apply caloric"),
    ),
    (
        "^menda$",
        "apply mending to arms",
        lambda m: send("apply mending to arms"),
    ),
    (
        "^resto$",
        "apply restoration",
        lambda m: send("apply restoration"),
    ),
    (
        "^restol$",
        "apply restoration to legs",
        lambda m: send("apply restoration to legs"),
    ),
    (
        "^restoa$",
        "apply restoration to arms",
        lambda m: send("apply restoration to arms"),
    ),
}
c.add_aliases("salves", salves_aliases)

pipes_aliases = {
    (
        "^lp$",
        "light pipes",
        lambda m: send("light pipes"),
    ),
    (
        "^sp$",
        "smoke pipe with skullcap",
        lambda m: send("light pipes;smoke pipe with skullcap"),
    ),
    (
        "^val$",
        "smoke pipe with valerian",
        lambda m: send("light pipes;smoke pipe with valerian"),
    ),
    (
        "^elm$",
        "smoke pipe with elm",
        lambda m: send("light pipes;smoke pipe with elm"),
    ),
}
c.add_aliases("pipes", pipes_aliases)
