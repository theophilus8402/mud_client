
from .client import send, add_aliases, add_triggers
from .variables import v
from .basic import eqbal


tarot_aliases = [
    (   "^sun$",
        "fling sun at ground",
        lambda _: eqbal("fling sun at ground")
    ),
    (   "^magi(?: (.+))?$",
        "fling magician at []/me",
        lambda matches: eqbal(f"fling magician at {matches[0] or 'me'}")
    ),
    (   "^priest(?: (.+))?$",
        "fling priestess at []/me",
        lambda matches: eqbal(f"fling priestess at {matches[0] or 'me'}")
    ),
    (   "^fool(?: (.+))?$",
        "fling fool at []/me",
        lambda matches: eqbal(f"fling fool at {matches[0] or 'me'}")
    ),
    (   "^fchar$",
        "fling chariot at ground",
        lambda matches: eqbal(f"fling chariot at ground")
    ),
    (   "^bchar$",
        "board chariot",
        lambda matches: eqbal(f"board chariot")
    ),
    (   "^fly$",
        "spur chariot skywards",
        lambda matches: eqbal(f"spur chariot skywards")
    ),
    (   "^fher(?: (.+))?$",
        "fling hermit at ground [tag]",
        lambda matches: eqbal(f"fling hermit at ground {matches[0] or ''}")
    ),
    (   "^aher(?: (.+))?$",
        "activate hermit [tag]",
        lambda matches: eqbal(f"outd hermit;activate hermit {matches[0] or ''}")
    ),
    (   "^hang(?: (.+))?$",
        "fling hangedman at []/t",
        lambda matches: eqbal(f"fling hangedman at {matches[0] or v.target}")
    ),
    (   "^star(?: (.+))?$",
        "fling star at []/t",
        lambda matches: eqbal(f"fling star at {matches[0] or v.target}")
    ),
    (   "^just(?: (.+))?$",
        "fling justice at []/t",
        lambda matches: eqbal(f"fling justice at {matches[0] or v.target}")
    ),
    (   "^aeon(?: (.+))?$",
        "fling aeon at []/t",
        lambda matches: eqbal(f"fling aeon at {matches[0] or v.target}")
    ),
    (   "^lust(?: (.+))?$",
        "fling lust at []/t",
        lambda matches: eqbal(f"fling lust at {matches[0] or v.target}")
    ),
    (   "^moon(?: (.+))?$",
        "fling moon at []/t",
        lambda matches: eqbal(f"fling moon at {matches[0] or v.target}")
    ),
    (   "^devil(?: (.+))?$",
        "fling devil at ground",
        lambda matches: eqbal("fling devil at ground")
    ),
    (   "^univ(?: (.+))?$",
        "fling universe at ground",
        lambda matches: eqbal("fling universe at ground")
    ),
]
add_aliases("ab_tarot", tarot_aliases)


