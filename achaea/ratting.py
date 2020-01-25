
import re

from datetime import datetime, timedelta

from .basic import eqbal
from .client import c, send, echo
from .state import s
from .timers import timers


def ratting_move_on(client):
    echo("need to fix ratting_move_on()")


def mob_entered_room(gmcp_data):
    #Char.Items.Add { "location": "room", "item": { "id": "118764", "name": "a young rat", "icon": "animal", "attrib": "m" } }
    # this is to check to see if a rat entered the room
    #s.rat_last_seen
    pass
c.add_gmcp_handler("Char.Items.Add", mob_entered_room)


def mob_left_room(gmcp_data):
    # Char.Items.Remove { "location": "room", "item": { "id": "118764", "name": "a young rat" } }
    # this is to check to see if a rat left the room
    #s.rat_last_seen
    pass
c.add_gmcp_handler("Char.Items.Remove", mob_left_room)


def ratting_room_info(gmcp_data):
    room_num = gmcp_data["num"]
    if room_num != s.ratting_room:
        echo(f"We changed ratting rooms! old: {s.ratting_room} new: {room_num}")
        s.ratting_room = room_num
c.add_gmcp_handler("Room.Info", ratting_room_info)


def rat(client, matches):

    if datetime.now() < s.last_rat_call + timedelta(seconds=1):
        #print("You've run 'rat' too recently!")
        return

    # print("running rat!")

    # if it looks like we've been ratting in the room before, move on
    """
    if s.room["num"] in s.rooms_ratted:
        print("It looks like we've ratted here before, moving on...")
        ratting_move_on(client)
        return
    """

    # if we've been waiting for 15 seconds with no sign of a rat, move on
    if datetime.now() >= s.rat_last_seen + timedelta(seconds=15):
        print("We've been waiting for too long!  It's time to move on!")
        ratting_move_on(client)
        # move on
        return

    s.last_rat_call = datetime.now()
    if len(s.players_in_room) >= 1:
        print("There ARE people in the room!")
        # move on
        ratting_move_on(client)
        return

    # check to see if we've killed all the rats in the room
    if s.rats_killed_in_room >= 3:
        print(f"Killed {s.rats_killed_in_room} rats here!  Moving on...")
        # move on
        ratting_move_on(client)
        return

    rat_in_room = False
    for mob in s.mobs_in_room:
        print(mob)
        if "rat" in mob["name"]:
            rat_in_room = True
            break
    if not rat_in_room:
        #print("There's NOT a rat in the room!")
        return

    if not (s.bal and s.eq):
        #print("You DON'T have bal/eq!")
        return
    eqbal("stand;warp rat")


def handle_rat_command(matches):
    if not matches[0]:
        echo(f"handle_rat_command single rat")
        rat(None, None)
    elif matches[0] == "on":
        timers.add("ratting", lambda: rat(None, None), 3, recurring=True)
        echo(f"handle_rat_command turn on the rat machine!")
    elif matches[0] == "off":
        print(timers.timers)
        timers.remove("ratting")
        echo(f"handle_rat_command turn it off!!!")
    else:
        echo("handle_rat_command ehhh????")


def rat_info(matches):
    echo("Showing rat info!")
    echo(f"mobs: {s.mobs_in_room}")
    echo(f"players: {s.players_in_room}")
    echo(f"rats killed: {s.rats_killed_in_room}")
    echo(f"now: {datetime.now()}, last_seen: {s.rat_last_seen}")

ratting_aliases = [
    (   "^rls$",
        "rat last seen",
        lambda matches: echo(f"rat last seen: {s.rat_last_seen}")
    ),
    (   "^rat(?: (.+))?$",
        "rat on/off//",
        lambda matches: handle_rat_command(matches)
    ),
    (   "^ri$",
        "rat info",
        rat_info
    ),
]
c.add_aliases("ratting", ratting_aliases)


