
from .client import send, add_aliases, add_triggers, echo
from .variables import v
from .basic import eqbal


def instill(target):
    echo(f"TODO: instill {target}")


occultism_aliases = [
    (   "^ague(?: (.+))?$",
        "ague []/t",
        lambda matches: eqbal(f"ague {matches[0] or v.target}")
    ),
    (   "^agl(?: (.+))?$",
        "auraglance []/t",
        lambda matches: eqbal(f"auraglance {matches[0] or v.target}")
    ),
    (   "^m(?: (.+))?$",
        "warp []/t",
        lambda matches: eqbal(f"warp {matches[0] or v.target}"),
    ),
    (   "^night$",
        "night",
        lambda _: eqbal("night"),
    ),
    (   "^shroud$",
        "shroud",
        lambda _: eqbal("shroud"),
    ),
    (   "^bwarp$",
        "bodywarp",
        lambda _: eqbal("bodywarp"),
    ),
    (   "^mist$",
        "eldritchmists",
        lambda _: eqbal("eldritchmists"),
    ),
    (   "^mask$",
        "mask",
        lambda _: eqbal("mask"),
    ),
    (   "^att(?: (.+))?$",
        "attend []/t",
        lambda matches: eqbal(f"attend {matches[0] or v.target}")
    ),
    (   "^ene(?: (.+))?$",
        "enervate []/t",
        lambda matches: eqbal(f"enervate {matches[0] or v.target}"),
    ),
    (   "^qui(?: (.+))?$",
        "quicken []/t",
        lambda matches: eqbal(f"quicken {matches[0] or v.target}")
    ),
    (   "^astralvision$",
        "astralvision",
        lambda _: eqbal("astralvision"),
    ),
    (   "^sarm(?: (.+))?$",
        "shrivel arms []/t",
        lambda matches: eqbal(f"shrivel arms {matches[0] or v.target}")
    ),
    (   "^sleg(?: (.+))?$",
        "shrivel legs []/t",
        lambda matches: eqbal(f"shrivel legs {matches[0] or v.target}")
    ),
    (   "^ra(?: (.+))?$",
        "readaura []/t",
        lambda matches: eqbal(f"readaura {matches[0] or v.target}")
    ),
    (   "^heartstone$",
        "heartstone",
        lambda _: eqbal("heartstone")
    ),
    (   "^simulacrum$",
        "simulacrum",
        lambda _: eqbal("simulacrum")
    ),
    (   "^twarp$",
        "timewarp",
        lambda _: eqbal("timewarp")
    ),
    (   "^daura",
        "distortaura",
        lambda _: eqbal("distortaura")
    ),
    (   "^pclk(?: (.+))?$",
        "pinchaura []/t cloak",
        lambda matches: eqbal(f"pinchaura {matches[0] or v.target} cloak")
    ),
    (   "^pspe(?: (.+))?$",
        "pinchaura []/t speed",
        lambda matches: eqbal(f"pinchaura {matches[0] or v.target} speed")
    ),
    (   "^pcalor(?: (.+))?$",
        "pinchaura []/t caloric",
        lambda matches: eqbal(f"pinchaura {matches[0] or v.target} caloric")
    ),
    (   "^pfrost(?: (.+))?$",
        "pinchaura []/t frost",
        lambda matches: eqbal(f"pinchaura {matches[0] or v.target} frost")
    ),
    (   "^plevi(?: (.+))?$",
        "pinchaura []/t levitation",
        lambda matches: eqbal(f"pinchaura {matches[0] or v.target} levitation")
    ),
    (   "^pinsom(?: (.+))?$",
        "pinchaura []/t insomnia",
        lambda matches: eqbal(f"pinchaura {matches[0] or v.target} insomnia")
    ),
    (   "^pkola(?: (.+))?$",
        "pinchaura []/t kola",
        lambda matches: eqbal(f"pinchaura {matches[0] or v.target} kola")
    ),
    (   "^spe(?: (.+))?$",
        "unnamable speak",
        lambda _: eqbal("unnamable speak"),
    ),
    (   "^vis(?: (.+))?$",
        "unnamable vision",
        lambda _: eqbal("unnamable vision"),
    ),
    (   "^devo(?: (.+))?$",
        "devolve []/t",
        lambda matches: eqbal(f"devolve {matches[0] or v.target}")
    ),
    (   "^caura(?: (.+))?$",
        "devolve []/t",
        lambda matches: eqbal(f"cleanseaura {matches[0] or v.target}")
    ),
    (   "^tent$",
        "tentacles",
        lambda _: eqbal("tentacles")
    ),
    (   "^rays$",
        "chaosrays",
        lambda _: eqbal("chaosrays")
    ),
    (   "^inst(?: (.+))?$",
        "instill []/t",
        lambda matches: instill(matches[0] or v.target),
    ),
    (   "^whisp$",
        "whisperingmadness t",
        lambda matches: eqbal(f"whisperingmadness {v.target}")
    ),
    (   "^dev$",
        "devilmark",
        lambda _: eqbal("devilmark"),
    ),
    (   "^trc$",
        "truename corpse",
        lambda matches: eqbal(f"truename corpse")
    ),
    (   "^utr$",
        "utter truename t",
        lambda matches: eqbal(f"utter truename {v.target}")
    ),
    (   "^ast$",
        "astralform",
        lambda _: eqbal(f"astralform"),
    ),
    (   "^enl$",
        "enlighten []/t",
        lambda matches: eqbal(f"enlighten {matches[0] or v.target}")
    ),
    (   "^unr$",
        "unravel mind of t",
        lambda matches: eqbal(f"unravel mind of {v.target}")
    ),
]
add_aliases("ab_occultism", occultism_aliases)


