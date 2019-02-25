
import re

from .client import send, add_gmcp_handler, echo
from .variables import v

def slain(client, matches):

    # this can be used for a number of things

    # check to see if we kill a rat for our ratting counter
    if "rat" in matches[0]:
        client.v.rats_killed_in_room += 1
        print("Rats killed in room: {}".format(client.v.rats_killed_in_room))

RE_CORPSE = re.compile("the corpse of (.*)")

def find_mobs_in_room(gmcp_data):
    if gmcp_data["location"] != "room":
        return False
    mobs = [item for item in gmcp_data["items"] if "m" in item.get("attrib", "")]
    v.mobs_in_room = mobs
add_gmcp_handler("Char.Items.List", find_mobs_in_room)

def mob_entered_room(gmcp_data):
    if (gmcp_data["location"] == "room" and
        "m" in gmcp_data["item"].get("attrib")):
        v.mobs_in_room.append(gmcp_data["item"])
    echo(v.mobs_in_room)
add_gmcp_handler("Char.Items.Add", mob_entered_room)

def mob_left_room(gmcp_data):
    if gmcp_data["location"] == "room":
        v.mobs_in_room.append(gmcp_data["item"])
    echo(v.mobs_in_room)
add_gmcp_handler("Char.Items.Add", mob_entered_room)

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

