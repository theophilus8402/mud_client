from achaea.basic import eqbal
from achaea.state import s
from client import c, echo, send

s.bashing_attack = lambda _: eqbal(f"stand;combo {s.target} sdk ucp ucp")

tekura_aliases = [
    (
        "^ma(?: (.+))?$",
        "sdk ucp ucp []/t",
        lambda matches: eqbal(f"stand;assist rino;combo &tar sdk ucp ucp"),
    ),
    (
        "^m(?: (.+))?$",
        "sdk ucp ucp []/t",
        s.bashing_attack,
    ),
    (
        "^ww(?: (.+))?$",
        "wwk ucp ucp []/t",
        lambda matches: eqbal(f"stand;combo {matches[0] or s.target} wwk ucp ucp"),
    ),
    (
        "^jk(?: (.+))?$",
        "jpk palmstrike palmstrike []/t",
        lambda matches: eqbal(f"stand;combo {matches[0] or s.target} jpk pmp pmp;drs"),
    ),
    (
        "^la(?: (.+))?$",
        "snk hfp hfp left []/t",
        lambda matches: eqbal(
            f"stand;combo {matches[0] or s.target} mnk left spp left spp left"
        ),
    ),
    (
        "^ra(?: (.+))?$",
        "snk hfp hfp right []/t",
        lambda matches: eqbal(
            f"stand;combo {matches[0] or s.target} mnk right spp right spp right"
        ),
    ),
    (
        "^tt(?: (.+))?$",
        "sdk hkp hkp []/t",
        lambda matches: eqbal(f"stand;combo {matches[0] or s.target} sdk hkp hkp"),
    ),
    (
        "^ll(?: (.+))?$",
        "snk hfp hfp left []/t",
        lambda matches: eqbal(
            f"stand;combo {matches[0] or s.target} snk left hfp left hfp left"
        ),
    ),
    (
        "^rl(?: (.+))?$",
        "snk hfp hfp right []/t",
        lambda matches: eqbal(
            f"stand;combo {matches[0] or s.target} snk right hfp right hfp right"
        ),
    ),
    (
        "^sk(?: (.+))?$",
        "swk hfp left hfp right []/t",
        lambda matches: eqbal(
            f"stand;combo {matches[0] or s.target} swk hfp left hfp left"
        ),
    ),
    (
        "^xx(?: (.+))?$",
        "axk upc upc []/t",
        lambda matches: eqbal(f"stand;combo {matches[0] or s.target} axk upc upc"),
    ),
    (
        "^bb(?: (.+))?$",
        "bbt []/t",
        lambda matches: eqbal(f"stand;bbt {matches[0] or s.target}"),
    ),
]
c.add_aliases("ab_tekura", tekura_aliases)
