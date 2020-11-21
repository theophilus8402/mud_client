import random

from achaea.basic import eqbal
from achaea.jester.bombs import throw_bomb
from achaea.jester.throw_dagger import throw_dagger
from achaea.state import s
from client import c, send
from client.timers import timers

opposite_direction = {
    "n": "s",
    "e": "w",
    "s": "n",
    "w": "e",
    "ne": "sw",
    "se": "nw",
    "sw": "ne",
    "nw": "se",
    "in": "out",
    "out": "in",
    "u": "d",
    "d": "u",
}


run_back_direction = ""


def choose_direction():
    exits = list(s.room_info.exits.keys())
    direction = random.choice(exits)
    return direction


def run_away(direction):

    if direction == "":
        direction = choose_direction()

    global run_back_direction
    run_back_direction = opposite_direction[direction]

    eqbal(f"stand;backflip {direction}")


def run_and_bomb(bomb_type, direction):
    if direction == "":
        direction = choose_direction()
    run_away(direction)

    global run_back_direction
    timers.add(f"run_and_bomb", lambda: throw_bomb(bomb_type, run_back_direction), 0.1)


def run_back():
    global run_back_direction
    run_away(run_back_direction)


run_away_aliases = [
    ("^r(?: (.+))?$", "runaway dir", lambda matches: run_away(matches[0] or "")),
    (
        "^rc(?: (.+))?$",
        "runaway dir;throw concussion",
        lambda matches: run_and_bomb("concussion", matches[0] or ""),
    ),
    ("^rb$", "run back", lambda _: run_back()),
]
c.add_aliases("run_away", run_away_aliases)
