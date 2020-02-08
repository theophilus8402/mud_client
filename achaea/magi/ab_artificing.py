
from ..client import c, send, echo
from ..state import s
from ..basic import eqbal


artificing_aliases = [
    (   "^club(?: (.+))?$",
        "golem club []/t (egg) - dmg",
        lambda matches: send(f"stand;golem club {matches[0] or s.target}"),
    ),
    (   "^smasha(?: (.+))?$",
        "golem smash []/t arms (pentagon) - break arm",
        lambda matches: send(f"stand;golem smash {matches[0] or s.target} arms"),
    ),
    (   "^smashl(?: (.+))?$",
        "golem smash []/t legs (pentagon) - break leg",
        lambda matches: send(f"stand;golem smash {matches[0] or s.target} legs"),
    ),
    (   "^hypo(?: (.+))?$",
        "golem hypothermia []/t (cube) - can't heal frozen",
        lambda matches: send(f"stand;golem hypothermia {matches[0] or s.target}"),
    ),
    (   "^scald(?: (.+))?$",
        "golem scald []/t (cylinder) - no parry",
        lambda matches: send(f"stand;golem scald {matches[0] or s.target}"),
    ),
    (   "^sch(?: (.+))?$",
        "golem scorch []/t (cylinder) - fire",
        lambda matches: send(f"stand;golem scorch {matches[0] or s.target}"),
    ),
    (   "^pum(?: (.+))?$",
        "golem pummel []/t (torus) - dmg frozen",
        lambda matches: send(f"stand;golem pummel {matches[0] or s.target}"),
    ),
    (   "^deh(?: (.+))?$",
        "golem dehydrate []/t (polyhedron) - need prone, ablaze, more mending",
        lambda matches: send(f"stand;golem dehydrate {matches[0] or s.target}"),
    ),
    (   "^flux(?: (.+))?$",
        "golem timeflux []/t (disc) - slow salve",
        lambda matches: send(f"stand;golem timeflux {matches[0] or s.target}"),
    ),
]
c.add_aliases("ab_artificing", artificing_aliases)
