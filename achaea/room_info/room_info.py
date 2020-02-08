
import json
import re

from datetime import datetime

from ..client import c, send, echo
from .name import long_short_name_map
from ..state import s


def add_unknown_long_name(gmcp_data):
    unknown_file = "unknown_long_names.json"
    with open(unknown_file, "r") as f:
        unknowns = json.load(f)
    unknowns[gmcp_data["name"]] = gmcp_data
    with open(unknown_file, "w") as f:
        json.dump(unknowns, f, indent=2)


def get_mobid(gmcp_data):
    #'106482': {'id': '106482', 'name': 'a young rat', 'icon': 'animal', 'attrib': 'm'}
    long_name = gmcp_data["name"]
    mob_id = gmcp_data["id"]
    if long_name not in long_short_name_map:
        print(f"didn't find: {long_name}")
        add_unknown_long_name(gmcp_data)
        return mob_id
    short_name = long_short_name_map[long_name]
    #print(f"{short_name}{mob_id}")
    return f"{short_name}{mob_id}"


def is_alive_mob(gmcp_data):
    return ("m" in gmcp_data.get("attrib", "")
            and "d" not in gmcp_data.get("attrib", ""))

def find_mobs_in_room(gmcp_data):
    #echo(gmcp_data)

    # make sure we're getting room info
    if gmcp_data["location"] != "room":
        return False

    # find all the mobs
    try:
        # "d" in attrib means it's dead so we don't care
        mobs = {get_mobid(item) : item for item in gmcp_data["items"]
                                    if is_alive_mob(item)}
    except Exception as e:
        print(f"find_mobs_in_room: {e}")
        return False

    # update the mobs_in_room set
    s.mobs_in_room.clear()
    s.mobs_in_room.update(mobs)
c.add_gmcp_handler("Char.Items.List", find_mobs_in_room)


def mob_entered_room(gmcp_data):
    #Char.Items.Add { "location": "room", "item": { "id": "118764", "name": "a young rat", "icon": "animal", "attrib": "m" } }
    #echo(gmcp_data)

    try:
        if (gmcp_data["location"] == "room" and
            "m" in gmcp_data["item"].get("attrib")):
            item = gmcp_data["item"]
            mob_id = get_mobid(item)
            s.mobs_in_room[mob_id] = item
    except TypeError:
        echo(f"GMCP data, mob_entered_room <{gmcp_data}> None!!")
c.add_gmcp_handler("Char.Items.Add", mob_entered_room)


def mob_left_room(gmcp_data):
    # Char.Items.Remove { "location": "room", "item": { "id": "118764", "name": "a young rat" } }
    #echo(gmcp_data)

    # make sure we're getting room info
    if gmcp_data["location"] != "room":
        return None

    # see if we can find that mob in the list
    item = gmcp_data["item"]
    for mob_id in s.mobs_in_room:
        if mob_id.endswith(item["id"]):
            #echo(f"found mob to remove: {item['id']}")
            s.mobs_in_room.pop(mob_id)
            break
c.add_gmcp_handler("Char.Items.Remove", mob_left_room)


def add_player(gmcp_data):
    # {"name": "Adrik", "fullname": "Adrik Bergson, the Crystalline Song"}
    player = gmcp_data["name"]
    echo(f"+{player}")
    s.players_in_room.add(player)
c.add_gmcp_handler("Room.AddPlayer", add_player)


def remove_player(gmcp_data):
    # "Farrah"
    echo(f"-{gmcp_data}")
    s.players_in_room.discard(gmcp_data)
c.add_gmcp_handler("Room.RemovePlayer", remove_player)


def room_players(gmcp_data):
    # [{"name": "Vhaith", "fullname": "Shield Curator Vhaith Rian-Moonshadow"}, {"name": "Vindiconis", "fullname": "Volunteer Vindiconis"}]
    me = {"Vindiconis", "Dirus", "Palleo"}
    players = {player["name"] for player in gmcp_data}
    players.difference_update(me)
    echo(f"+{', '.join(players)}")
    s.players_in_room.clear()
    s.players_in_room.update(players)
c.add_gmcp_handler("Room.Players", room_players)
