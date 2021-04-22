import asyncio
import re
from datetime import datetime, timedelta

from achaea.basic import eqbal
from achaea.state import s
from client import c, echo, send
from client.timers import timers


ratter = None


def rat_in_room():
    for mob_id, mob in s.mobs_in_room:
        if mob.get("short_name") == "rat":
            return True
    return False


def player_in_room():
    return len(s.players_in_room) > 0


def room_changed(last_room):
    return last_room.num != s.room_info.num


class Ratter():

    def __init__(self):
        timers.add("ratting", lambda: self.tick(), 3, recurring=True)
        self.last_room = s.room_info
        self.rats_killed = 0
        self.ticks_in_room = 0
        self.max_ticks_in_room = 12
        self.max_rats_in_room = 3

    def stop(self):
        echo("stopping ratter")
        timers.remove("ratting")

    def tick(self):

        self.ticks_in_room += 1

        try:
            if room_changed(self.last_room):
                echo("ratting room changed!")
                self.last_room = s.room_info
                self.rats_killed = 0
                self.ticks_in_room = 0
            echo(f"rats killed: {self.rats_killed}")

            if self.ticks_in_room >= self.max_ticks_in_room:
                echo(f"ratting ticks: {self.ticks_in_room}")
                echo("ratting: time to move on")
            elif self.rats_killed >= self.max_rats_in_room:
                echo("killed all the rats!")
            elif player_in_room():
                echo(f"ratting ticks: {self.ticks_in_room}")
                echo(f"players: {s.players_in_room}")
            elif rat_in_room():
                echo(f"ratting ticks: {self.ticks_in_room}")
                echo("ratter: attacking")
                self.ticks_in_room = 0
                self.attack()
            #else:
            #    echo("no rats!")
        except Exception as e:
            echo(f"ERROR: {e}")

    def attack(self):
        s.bashing_attack("")
        c.send_flush()


def rat_on():
    echo("creating ratter")
    global ratter
    ratter = Ratter()


def rat_off():
    echo("deleting ratter")
    global ratter
    ratter.stop()
    ratter = None


def dead_rat():
    if ratter:
        ratter.rats_killed += 1


ratting_aliases = [
    (
        "^rat on",
        "rat on",
        lambda _: rat_on(),
    ),
    (
        "^rat off",
        "rat off",
        lambda _: rat_off(),
    ),
]
c.add_aliases("ratting", ratting_aliases)


ratting_triggers = [
    (
        r"^You have slain a baby rat, retrieving the corpse.$",
        # killed a rat!
        lambda _: dead_rat(),
    ),
    (
        r"^You have slain a young rat, retrieving the corpse.$",
        # killed a rat!
        lambda _: dead_rat(),
    ),
    (
        r"^You have slain a rat, retrieving the corpse.$",
        # killed a rat!
        lambda _: dead_rat(),
    ),
    (
        r"^You have slain an old rat, retrieving the corpse.$",
        # killed a rat!
        lambda _: dead_rat(),
    ),
    (
        r"^You have slain a black rat, retrieving the corpse.$",
        # killed a rat!
        lambda _: dead_rat(),
    ),
]
c.add_triggers(ratting_triggers)
