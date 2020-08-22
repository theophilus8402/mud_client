
import json
import logging
import re

from datetime import datetime

from ..client import c, send, echo
from .name import get_mob_id, get_mobs_from_items, figure_out_unknown_mobs
from ..state import s


logger = logging.getLogger("achaea")


room_aliases = [
    (   "^cir$",
        "Char.Items.Room",
        lambda matches: c.gmcp_send("Char.Items.Room \"\"")
    ),
]
c.add_aliases("room_info", room_aliases)


def find_mobs_in_room(gmcp_data):
    #echo(gmcp_data)

    # make sure we're getting room info
    if gmcp_data["location"] != "room":
        return False

    # find all the mobs
    try:
        items = gmcp_data["items"]
        mobs = get_mobs_from_items(gmcp_data["items"])
    except Exception as e:
        echo(f"find_mobs_in_room: {e}")
        echo(f"gmcp_data: {gmcp_data}")
        return False

    # update the mobs_in_room set
    s.mobs_in_room = tuple(mobs)
#c.add_gmcp_handler("Char.Items.List", find_mobs_in_room)


def mob_entered_room(gmcp_data):
    #Char.Items.Add { "location": "room", "item": { "id": "118764", "name": "a young rat", "icon": "animal", "attrib": "m" } }
    #echo(gmcp_data)

    if (gmcp_data["location"] == "room" and
        "m" in gmcp_data["item"].get("attrib")):
        item = gmcp_data["item"]
        mob_id = get_mob_id(item)
        s.mobs_in_room = (*s.mobs_in_room, (mob_id, item))
#c.add_gmcp_handler("Char.Items.Add", mob_entered_room)


def mob_left_room(gmcp_data):
    # Char.Items.Remove { "location": "room", "item": { "id": "118764", "name": "a young rat" } }
    #echo(gmcp_data)

    # make sure we're getting room info
    if gmcp_data["location"] != "room":
        return None

    # see if we can find that mob in the list
    item = gmcp_data["item"]
    mobs = set(s.mobs_in_room)
    for mob_info in mobs:
        mob_id, mob = mob_info
        if mob_id.endswith(item["id"]):
            #echo(f"found mob to remove: {item['id']}")
            s.mobs_in_room = tuple(mobs.remove(mob_id))
            break
#c.add_gmcp_handler("Char.Items.Remove", mob_left_room)


def add_player(gmcp_data):
    # {"name": "Adrik", "fullname": "Adrik Bergson, the Crystalline Song"}
    player = gmcp_data["name"]
    echo(f"+{player}")
    logger.fighting(f"+{player}")
    s.players_in_room = (*s.players_in_room, player)
#c.add_gmcp_handler("Room.AddPlayer", add_player)


def remove_player(gmcp_data):
    # "Farrah"
    echo(f"-{gmcp_data}")
    logger.fighting(f"-{gmcp_data}")
    players = set(s.players_in_room).discard(gmcp_data)
    s.players_in_room = tuple(players)
#c.add_gmcp_handler("Room.RemovePlayer", remove_player)


def room_players(gmcp_data):
    # [{"name": "Vhaith", "fullname": "Shield Curator Vhaith Rian-Moonshadow"}, {"name": "Vindiconis", "fullname": "Volunteer Vindiconis"}]
    me = {"Vindiconis", "Dirus", "Palleo", "Sarmenti"}
    players = {player["name"] for player in gmcp_data}
    players.difference_update(me)
    echo(f"+{', '.join(players)}")
    s.players_in_room = tuple(players)
#c.add_gmcp_handler("Room.Players", room_players)
