
import re

from colorama import *
from copy import copy

from .basic import eqbal, highlight_current_line
from client import c, send, echo
from .state import s

def pton():
    echo("Turning party announcements ON!")
    s.pt_announce = True

def ptoff():
    echo("Turning party announcements OFF!")
    s.pt_announce = False

def enemy_person(person):
    if person == "all":
        echo("Why are you trying to enemy all?")
    else:
        s.enemies.add(person)
        send(f"enemy {person}")

        # set the enemy trigger
        enemy_trigger = (
                person,
                lambda m: highlight_current_line(Fore.RED, pattern=person, flags=re.I)
            )
        c.add_temp_trigger(f"enemy_trigger_{person}", enemy_trigger, flags=re.IGNORECASE)

def unenemy_person(person):
    if person == "all":
        copy_enemies = copy(s.enemies)
        for enemy in copy_enemies:
            unenemy_person(enemy)
        send("unenemy all")
    else:
        s.enemies.discard(person)
        send(f"unenemy {person}")

        # remove the previous target trigger
        c.remove_temp_trigger(f"enemy_trigger_{person}")


def multiple_ally(matches):
    for person in matches[0].replace(",", "").split(" "):
        send(f"ally {person}")

def multiple_enemy(matches):
    for person in matches[0].replace(",", "").split(" "):
        enemy_person(person)

group_fighting_aliases = [
    (   "^pton$",
        "party announcements on",
        lambda _: pton()
    ),
    (   "^ptoff$",
        "party announcements off",
        lambda _: ptoff()
    ),
    (   "^men (.+)$",
        "multiply enemy",
        lambda matches: multiple_enemy(matches)
    ),
    (   "^enemy(?: (.+))?$",
        "enemy []/target",
        lambda matches: enemy_person(matches[0] or '&tar')
    ),
    (   "^unenemy (.+)$",
        "unenemy []",
        lambda matches: unenemy_person(matches[0])
    ),
    (   "^unemall$",
        "unenemy all",
        lambda matches: unenemy_person("all")
    ),
    (   "^mall (.+)$",
        "multiple ally",
        lambda matches: multiple_ally(matches)
    ),
]
c.add_aliases("group_fighting", group_fighting_aliases)

