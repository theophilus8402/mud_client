import random

from achaea.basic import eqbal
from achaea.defences import basic_defs
from achaea.jester.bombs import make_bomb, throw_bomb
from achaea.jester.throw_dagger import throw_dagger
from achaea.state import s
from client import c, send

pranks_basic_defs = {"slippery"}
basic_defs.update(pranks_basic_defs)


def balancing(state):
    eqbal(f"stand;balancing {state}")


def backhandspring(direction):
    if direction == "":
        exits = list(s.room_info.exits.keys())
        direction = random.choice(exits)
    eqbal(f"stand;backhandspring {s.target} {direction}")


def backflip(direction):
    if direction == "":
        exits = list(s.room_info.exits.keys())
        direction = random.choice(exits)
    eqbal(f"stand;backflip {direction}")


def somersault(direction):
    if direction == "":
        exits = list(s.room_info.exits.keys())
        direction = random.choice(exits)
    eqbal(f"stand;somersault {direction}")


def wish(item):
    eqbal(f"stand;get 200 gold from pack;wish for 10 {item}")


pranks_aliases = [
    (
        "^wb$",
        "wield blackjack",
        lambda matches: eqbal(f"stand;unwield left;wield blackjack"),
    ),
    ("^m$", "bop t", lambda matches: eqbal(f"stand;bop &tar")),
    ("^wi bal$", "wish for 10 balloons", lambda matches: wish("balloon")),
    ("^wi mic$", "wish for 10 mickey", lambda matches: wish("mickey")),
    ("^wi it$", "wish for 10 itchpowder", lambda matches: wish("itchpowder")),
    # (   "^fly$",
    #    "inflate balloon",
    #    lambda matches: eqbal(f"stand;inflate balloon")
    # ),
    ("^bf(?: (.+))?$", "backflip dir", lambda matches: backflip(matches[0] or "")),
    ("^b$", "throw bombs!", lambda matches: throw_bomb("", "")),
    (
        "^bc(?: (.*))?$",
        "throw bombs!",
        lambda matches: throw_bomb("concussion", matches[0] or ""),
    ),
    (
        "^bb(?: (.*))?$",
        "throw bombs!",
        lambda matches: throw_bomb("butterfly", matches[0] or ""),
    ),
    (
        "^bs(?: (.*))?$",
        "throw bombs!",
        lambda matches: throw_bomb("smoke", matches[0] or ""),
    ),
    (
        "^bw(?: (.*))?$",
        "throw bombs!",
        lambda matches: throw_bomb("web", matches[0] or ""),
    ),
    (
        "^bd(?: (.*))?$",
        "throw bombs!",
        lambda matches: throw_bomb("dust", matches[0] or ""),
    ),
    ("^mb(?: (.+))?$", "make bombs!", lambda matches: make_bomb(matches[0] or "")),
    (
        "^bhs(?: (.+))?$",
        "backhandspring",
        lambda matches: backhandspring(matches[0] or ""),
    ),
    (
        "^bal(?: (.+))?$",
        "balancing [on]/off",
        lambda matches: balancing(matches[0] or "on"),
    ),
    (
        "^vent(?: (.+))?$",
        "vent t/[]",
        lambda matches: eqbal(f"vent {matches[0] or s.target}"),
    ),
    ("^bad$", "badjoke", lambda matches: eqbal(f"badjoke")),
    (
        "^mic(?: (.+))?$",
        "slip t/[] mickey",
        lambda matches: eqbal(f"slip {matches[0] or s.target} mickey"),
    ),
    (
        "^som(?: (.+))?$",
        "somersault dir/randomdir",
        lambda matches: somersault(matches[0] or ""),
    ),
    (
        "^arrow(?: (.+))?$",
        "arrowcatch []/on",
        lambda matches: eqbal(f"stand;arrowcatch {matches[0] or 'on'}"),
    ),
    (
        "^ban$",
        "litter floor with peels",
        lambda matches: eqbal(f"stand;litter floor with peels"),
    ),
    # TODO: pick up after banana peels
    ("^d(?!h)(.+)$", "throw daggers!", lambda matches: throw_dagger(matches[0])),
    (
        "^it(?: (.+))?$",
        "slip t/[] itchpowder",
        lambda matches: eqbal(f"slip {matches[0] or s.target} itchpowder"),
    ),
    (
        "^fishmice$",
        "fish for mice",
        lambda matches: eqbal(
            f"stand;outr rope;outr cheese;tie cheese to rope;fish for mice"
        ),
    ),
]
c.add_aliases("ab_pranks", pranks_aliases)
