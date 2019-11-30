
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


def mob_entered_or_left_room(gmcp_data):
    # this is to check to see if a rat entered or left the room
    v.rat_last_seen
add_gmcp_handler("Char.Items.Add", mob_entered_or_left_room)
add_gmcp_handler("Char.Items.Remove", mob_entered_or_left_room)


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

"""
def find_rats_in_room(gmcp_data):
    if gmcp_data["location"] != "room":
        return False

    rats = [item for item in gmcp_data["items"] if item.get("attrib") == "m" and
                                        "rat" in item["name"]]
    for rat in rats:
        echo(rat)
add_gmcp_handler("Char.Items.List", find_rats_in_room)
"""

"""
    def handleGmcp(self, cmd, value):
        if cmd == "Char.Items.List":
            if value["location"] == "room":
                self.client.v.mobs_in_room = {(item["name"], item["id"]) for item in value["items"] if item.get("attrib") == "m"}
                self.display_status_info()
        elif cmd == "Char.Items.Add":
            # make sure it was an "item" in the room
            if value['location'] == 'room':
                name = value['item']['name']
                eid = value['item']['id']
                self.client.v.mobs_in_room.add((name, eid))
                self.display_status_info()
                #print("{} {} entered the room!".format(name, eid), end="")
        elif cmd == "Char.Items.Remove":
            # make sure it was an "item" in the room
            if value['location'] == 'room':
                name = value['item']['name']
                eid = value['item']['id']
                # sometimes, this is a mob we have just killed
                # but it shows as a corpse having been removed by
                # me picking it up
                # KeyError: ('the corpse of a black rat', '502337')
                match = RE_CORPSE.match(name)
                if match:
                    name = match.groups()[0]
                self.client.v.mobs_in_room.discard((name, eid))
                self.display_status_info()
                #print("{} {} left the room!".format(name, eid), end="")
        elif cmd == "Room.Players":
            # GMCP! cmd: Room.Players value: [{'name': 'Dirus', 'fullname': "Drudge Dirus Sar'vet"}] type value: <class 'list'>
            self.client.v.players_in_room = {p["name"] for p in value if p["name"] not in {"Dirus", "Palleo"}}
            #echo("Players: {}".format(", ".join(self.client.v.players_in_room)), self.mud)
            #echo("v: {}".format(self.client.v), self.mud)
            #echo("state: {}".format(self.client.state), self.mud)
        elif cmd == "Room.AddPlayer":
            # GMCP! cmd: Room.AddPlayer value: {'name': 'Miharu', 'fullname': 'Awakened Miharu'} type value: <class 'dict'>
            player = value["name"]
            self.client.v.players_in_room.add(player)
            echo("Players: {}".format(", ".join(self.client.v.players_in_room)), self.mud)
            #echo("+{}".format(value["name"]), self.mud)
        elif cmd == "Room.RemovePlayer":
            # GMCP! cmd: Room.RemovePlayer value: Miharu type value: <class 'str'>
            player = value
            if player not in {"Palleo", "Dirus"}:
                self.client.v.players_in_room.remove(player)
            echo("Players: {}".format(", ".join(self.client.v.players_in_room)), self.mud)
            #echo("-{}".format(value), self.mud)
        elif cmd == "Room.Info":
            # check to see if we've moved into a new room:
            if self.client.v.room["num"] != value["num"]:
                # if we have, at least reset the number of rats killed in the room
                self.client.v.rats_killed_in_room = 0
                # start the timer stating that we haven't seen rats in the room
                self.client.v.rat_last_seen = datetime.now()
            self.client.v.room.update(value)

"""

