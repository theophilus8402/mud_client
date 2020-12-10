from achaea.basic import eqbal
from achaea.state import s
from client import c, echo, send

tekura_aliases = [
    (
        "^m(?: (.+))?$",
        "sdk ucp ucp []/t",
        lambda matches: eqbal(f"combo {matches[0] or s.target} sdk ucp ucp"),
    ),
    (
        "^ww(?: (.+))?$",
        "wwk hfp left hfp left []/t",
        lambda matches: eqbal(f"combo {matches[0] or s.target} wwk hfp left hfp left"),
    ),
    (
        "^jk(?: (.+))?$",
        "jpk palmstrike palmstrike []/t",
        lambda matches: eqbal(f"combo {matches[0] or s.target} jpk pmp pmp"),
    ),
    (
        "^la(?: (.+))?$",
        "snk hfp hfp left []/t",
        lambda matches: eqbal(
            f"combo {matches[0] or s.target} mnk left spp left spp left"
        ),
    ),
    (
        "^ra(?: (.+))?$",
        "snk hfp hfp right []/t",
        lambda matches: eqbal(
            f"combo {matches[0] or s.target} mnk right spp right spp right"
        ),
    ),
    (
        "^tt(?: (.+))?$",
        "sdk hkp hkp []/t",
        lambda matches: eqbal(f"combo {matches[0] or s.target} sdk hkp hkp"),
    ),
    (
        "^ll(?: (.+))?$",
        "snk hfp hfp left []/t",
        lambda matches: eqbal(
            f"combo {matches[0] or s.target} snk left hfp left hfp left"
        ),
    ),
    (
        "^rl(?: (.+))?$",
        "snk hfp hfp right []/t",
        lambda matches: eqbal(
            f"combo {matches[0] or s.target} snk right hfp right hfp right"
        ),
    ),
    (
        "^sk(?: (.+))?$",
        "swk hfp left hfp right []/t",
        lambda matches: eqbal(f"combo {matches[0] or s.target} swk hfp left hfp right"),
    ),
]
c.add_aliases("ab_tekura", tekura_aliases)
