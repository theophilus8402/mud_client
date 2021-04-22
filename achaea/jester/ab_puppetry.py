from achaea.basic import eqbal
from achaea.defences import basic_defs
from achaea.state import s
from client import c, send

puppetry_basic_defs = {"gripping"}
basic_defs.update(puppetry_basic_defs)


def puppet(target, action):
    action = action.format(target=target)
    eqbal(f"stand;wield left puppet {target};{action}")


def fashion(target):
    target = target.lower()
    eqbal(f"wield left puppet {target};fashion puppet of {target}", prepend=True)


puppetry_aliases = [
    (
        "^fp(?: (.+))?$",
        "fashion puppet of []/",
        lambda m: fashion(m[0] or s.target)
    ),
    (
        "^pup(?: (.+))?$",
        "prope []/",
        lambda m: send(f"p {{{m[0] or s.target}}}")
    ),
    (
        "^conf(?: (.+))?$",
        "puppet confusion []/",
        lambda m: puppet(m[0] or s.target, f"puppet confusion"),
    ),
    (
        "^diz(?: (.+))?$",
        "puppet dizzy []/t",
        lambda m: puppet(m[0] or s.target, f"puppet dizzy"),
    ),
    (
        "^sl(?: (.+))?$",
        "puppet sleep []/t",
        lambda m: puppet(m[0] or s.target, f"puppet sleep"),
    ),
    (
        "^spy(?: (.+))?$",
        "puppet spy []/t",
        lambda m: puppet(m[0] or s.target, f"puppet spy"),
    ),
    (
        "^pstat(?: (.+))?$",
        "puppet status []/t",
        lambda m: puppet(m[0] or s.target, f"puppet status"),
    ),
    (
        "^psum(?: (.+))?$",
        "puppet summary []/t",
        lambda m: puppet(m[0] or s.target, f"puppet summary"),
    ),
    (
        "^strip(?: (.+))?$",
        "puppet strip []/t",
        lambda m: puppet(m[0] or s.target, f"puppet strip"),
    ),
    (
        "^par(?: (.+))?$",
        "puppet paralyse []/t",
        lambda m: puppet(m[0] or s.target, f"puppet paralyse"),
    ),
    (
        "^pba(?: (.+))?$",
        "puppet break arms []/t",
        lambda m: puppet(m[0] or s.target, f"puppet break arms"),
    ),
    (
        "^pbl(?: (.+))?$",
        "puppet break legs []/t",
        lambda m: puppet(m[0] or s.target, f"puppet break legs"),
    ),
    (
        "^th(?: (.+))?$",
        "puppet throttle []/t",
        lambda m: puppet(m[0] or s.target, f"puppet throttle;fashion puppet of {s.target}"),
    ),
    (
        "^rec(?: (.+))?$",
        "puppet reckless []/t",
        lambda m: puppet(m[0] or s.target, f"puppet reckless"),
    ),
    (
        "^tic(?: (.+))?$",
        "puppet tickle []/t",
        lambda m: puppet(m[0] or s.target, f"puppet tickle"),
    ),
    (
        "^burn(?: (.+))?$",
        "puppet burn []/t",
        lambda m: puppet(m[0] or s.target, f"puppet burn"),
    ),
    (
        "^bleed(?: (.+))?$",
        "puppet bleed []/t",
        lambda m: puppet(m[0] or s.target, f"puppet bleed"),
    ),
    (
        "^trav(?: (.+))?$",
        # travel just needs you to not be on a mono, target can be on a mono
        "puppet travel []/t",
        lambda m: puppet(m[0] or s.target, f"puppet travel"),
    ),
    (
        "^tie$",
        "puppet tonguetie t",
        lambda m: puppet(s.target, f"puppet tonguetie"),
    ),
    (
        "^crip(?: (.+))?$",
        "puppet cripple []/t",
        lambda m: puppet(m[0] or s.target, f"puppet cripple"),
    ),
    (
        "^comm (.+)$",
        "puppet command []/t",
        lambda m: puppet(s.target, f"puppet command {m[0]}"),
    ),
    (
        "^slow(?: (.+))?$",
        "puppet slow []/t",
        lambda m: puppet(m[0] or s.target, f"puppet slow"),
    ),
    (
        "^punc(?: (.+))?$",
        "puppet puncture []/t",
        lambda m: puppet(m[0] or s.target, f"puppet puncture"),
    ),
]
c.add_aliases("ab_puppetry", puppetry_aliases)
