import re
from copy import copy

from colorama import Fore

from achaea.basic import eqbal, highlight_current_line
from achaea.state import s
from client import c, echo, send
from telnet_manager import strip_ansi


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
            lambda m: highlight_current_line(Fore.RED, pattern=person, flags=re.I),
        )
        c.add_temp_trigger(
            f"enemy_trigger_{person}", enemy_trigger, flags=re.IGNORECASE
        )


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


def ally_person(person):
    send(f"ally {person}")


def multiple_ally(matches):
    for person in matches[0].replace(",", "").split(" "):
        ally_person(person)


def multiple_enemy(matches):
    for person in matches[0].replace(",", "").split(" "):
        enemy_person(person)


def find_and_ally_party(matches):
    first_dash = False
    members = []
    for line in c.current_chunk.split("\r\n"):
        line = strip_ansi(line)
        if line == "Your party has the following members:":
            continue
        elif line == "-------------------------------------------------":
            if not first_dash:
                first_dash = True
            else:
                # should be at the end
                break
        else:
            line = line.rstrip(".")
            line = line.rstrip(",")
            echo(line)
            members.extend(line.split(", "))
            echo(members)
    [ally_person(m) for m in members]
    c.remove_temp_trigger("party_member_trigger")


def ally_party(matches):
    send("party members")
    # set the enemy trigger
    party_member_trigger = (
        "^Your party has the following members:$",
        find_and_ally_party,
    )
    c.add_temp_trigger(
        f"party_member_trigger", party_member_trigger, flags=re.IGNORECASE
    )


group_fighting_aliases = [
    ("^pton$", "party announcements on", lambda _: pton()),
    ("^ptoff$", "party announcements off", lambda _: ptoff()),
    ("^men (.+)$", "multiply enemy", lambda matches: multiple_enemy(matches)),
    (
        "^enemy(?: (.+))?$",
        "enemy []/target",
        lambda matches: enemy_person(matches[0] or "&tar"),
    ),
    ("^unenemy (.+)$", "unenemy []", lambda matches: unenemy_person(matches[0])),
    ("^unemall$", "unenemy all", lambda matches: unenemy_person("all")),
    ("^mall (.+)$", "multiple ally", lambda matches: multiple_ally(matches)),
    (
        "^pally$",
        "ally party",
        ally_party,
    ),
]
c.add_aliases("group_fighting", group_fighting_aliases)
