
from client import send, c
from achaea.state import s
from achaea.basic import eqbal
from achaea.defences import basic_defs

puppetry_basic_defs = {"gripping"}
basic_defs.update(puppetry_basic_defs)


def puppet(target, action):
    action = action.format(target=target)
    eqbal(f"stand;wield left puppet {target};{action}")


def fashion(target):
    target = target.lower()
    eqbal(f"wield left puppet {target};fashion puppet of {target}",
          prepend=True)


puppetry_aliases = [
    (   "^fp(?: (.+))?$",
        "fashion puppet of []/",
        lambda m: fashion(m[0] or s.target)
    ),
    (   "^pup(?: (.+))?$",
        "prope []/",
        lambda m: send(f"p {{{m[0] or s.target}}}")
    ),
    (   "^trav(?: (.+))?$",
        "puppet travel []/",
        lambda m: puppet(m[0] or s.target, f"puppet travel")
    ),
]
c.add_aliases("ab_puppetry", puppetry_aliases)
