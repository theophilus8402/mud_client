
from ..client import send, add_aliases, add_triggers, echo
from ..state import s
from ..basic import eqbal

def command_ent(entity, target):
    echo(f"TODO: command_ent {entity} {target}")


def auto_ent(entity, on):
    echo(f"TODO: auto_ent {entity} {on}")


domination_aliases = [
    (   "^derv(?: (.+))?$",
        "dervish []/t",
        lambda matches: command_ent("dervish", matches[0] or v.target)
    ),
    (   "^syc(?: (.+))?$",
        "sycophant []/t",
        lambda matches: command_ent("sycophant", matches[0] or v.target)
    ),
    (   "^grem(?: (.+))?$",
        "gremlin []/t",
        lambda matches: command_ent("gremlin", matches[0] or v.target)
    ),
    (   "^orb(?: (.+))?$",
        "orb []/me",
        lambda matches: command_ent("orb", matches[0] or "me")
    ),
    (   "^leech(?: (.+))?$",
        "bloodleech []/t",
        lambda matches: command_ent("bloodleech", matches[0] or v.target)
    ),
    (   "^leechon$",
        "auto bloodleech on",
        lambda _: auto_ent("bloodleech", on=True)
    ),
    (   "^leechoff$",
        "auto bloodleech off",
        lambda _: auto_ent("bloodleech", on=False)
    ),
    (   "^nem(?: (.+))?$",
        "nemesis []/t",
        lambda matches: command_ent("nemesis", matches[0] or v.target)
    ),
    (   "^nemon$",
        "auto nemesis on",
        lambda _: auto_ent("nemesis", on=True)
    ),
    (   "^nemoff$",
        "auto nemesis off",
        lambda _: auto_ent("nemesis", on=False)
    ),
    (   "^poss$",
        "order soulmaster possess t",
        lambda matches: send(f"order soulmaster possess {mud.v.target}")
    ),
    (   "^osp$",
        "order t smoke pipe with skullcap",
        lambda matches: send(f"order {mud.v.target} smoke pipe with skullcap")
    ),
]
add_aliases("ab_domination", domination_aliases)

