
import re

from datetime import datetime, timedelta

from .basic import eqbal
from .client import send, add_gmcp_handler, echo, add_aliases
from .variables import v
from .timers import timers

def remember_path(on, mud):
    # set it to True/False as dictated by "on"
    mud.v.remember_path = on
    if on:
        mud.v.path_to_remember = list()
    #return ""

def show_path(mud, matches=None):
    path = getattr(mud.v, "path_to_remember", [])
    print("path: {}".format(path))

def ratting(client, matches):
    if matches[0] == "on":

        # call the ratting function again in 3 seconds just incase there hasn't been much movement in the room
        client.timers["ratting"] = client.mktimer(3, lambda: rat(client, matches))

        client.v.ratting = True
    else:
        client.v.ratting = False
        del(client.timers["ratting"])


def ratting_move_on(client):
    echo("need to fix ratting_move_on()")
    #client.v.rooms_ratted.add(client.v.room["num"])
    #random_move(client)
    pass


def mob_entered_room(gmcp_data):
    #Char.Items.Add { "location": "room", "item": { "id": "118764", "name": "a young rat", "icon": "animal", "attrib": "m" } }
    # this is to check to see if a rat entered the room
    v.rat_last_seen
add_gmcp_handler("Char.Items.Add", mob_entered_room)


def mob_left_room(gmcp_data):
    # Char.Items.Remove { "location": "room", "item": { "id": "118764", "name": "a young rat" } }
    # this is to check to see if a rat left the room
    v.rat_last_seen
add_gmcp_handler("Char.Items.Remove", mob_left_room)


def ratting_room_info(gmcp_data):
    room_num = gmcp_data["num"]
    if room_num != v.ratting_room:
        echo(f"We changed ratting rooms! old: {v.ratting_room} new: {room_num}")
        v.ratting_room = room_num
add_gmcp_handler("Room.Info", ratting_room_info)


def rat(client, matches):

    if datetime.now() < v.last_rat_call + timedelta(seconds=1):
        #print("You've run 'rat' too recently!")
        return

    # print("running rat!")

    # if it looks like we've been ratting in the room before, move on
    """
    if v.room["num"] in v.rooms_ratted:
        print("It looks like we've ratted here before, moving on...")
        ratting_move_on(client)
        return
    """

    # if we've been waiting for 15 seconds with no sign of a rat, move on
    if datetime.now() >= v.rat_last_seen + timedelta(seconds=15):
        print("We've been waiting for too long!  It's time to move on!")
        ratting_move_on(client)
        # move on
        return

    v.last_rat_call = datetime.now()
    if len(v.players_in_room) >= 1:
        print("There ARE people in the room!")
        # move on
        ratting_move_on(client)
        return

    # check to see if we've killed all the rats in the room
    if v.rats_killed_in_room >= 3:
        print("Killed {} rats here!  Moving on...".format(client.v.rats_killed_in_room))
        # move on
        ratting_move_on(client)
        return

    rat_in_room = False
    for mob in v.mobs_in_room:
        print(mob)
        if "rat" in mob["name"]:
            rat_in_room = True
            break
    if not rat_in_room:
        #print("There's NOT a rat in the room!")
        return

    if not (v.bal and v.eq):
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
    echo(f"mobs: {v.mobs_in_room}")
    echo(f"players: {v.players_in_room}")
    echo(f"rats killed: {v.rats_killed_in_room}")
    echo(f"now: {datetime.now()}, last_seen: {v.rat_last_seen}")

ratting_aliases = [
    (   "^rls$",
        "rat last seen",
        lambda matches: echo(f"rat last seen: {v.rat_last_seen}")
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
add_aliases("ratting", ratting_aliases)

def slain(client, matches):

    # this can be used for a number of things

    # check to see if we kill a rat for our ratting counter
    if "rat" in matches[0]:
        client.v.rats_killed_in_room += 1
        print("Rats killed in room: {}".format(client.v.rats_killed_in_room))

RE_CORPSE = re.compile("the corpse of (.*)")


mapping_aliases = {
    "^rpon$" : lambda mud,_: remember_path(on=True, mud=mud),
    "^rpoff$" : lambda mud,_: remember_path(on=False, mud=mud),
    "^showpath$" : show_path,
}

