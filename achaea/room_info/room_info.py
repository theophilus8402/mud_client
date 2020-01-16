
import re

from datetime import datetime

from ..client import send, add_gmcp_handler, echo
from ..variables import v


def find_mobs_in_room(gmcp_data):
    echo(gmcp_data)

    # make sure we're getting room info
    if gmcp_data["location"] != "room":
        return False

    # find all the mobs
    mobs = {item for item in gmcp_data["items"] if "m" in item.get("attrib", "")}

    # update the mobs_in_room set
    v.mobs_in_room.clear()
    v.mobs_in_room.update(mobs)
add_gmcp_handler("Char.Items.List", find_mobs_in_room)


def mob_entered_room(gmcp_data):
    #Char.Items.Add { "location": "room", "item": { "id": "118764", "name": "a young rat", "icon": "animal", "attrib": "m" } }
    echo(gmcp_data)

    try:
        if (gmcp_data["location"] == "room" and
            "m" in gmcp_data["item"].get("attrib")):
            v.mobs_in_room.add(gmcp_data["item"])
    except TypeError:
        echo(f"GMCP data, mob_entered_room <{gmcp_data}> None!!")
add_gmcp_handler("Char.Items.Add", mob_entered_room)


def mob_left_room(gmcp_data):
    # Char.Items.Remove { "location": "room", "item": { "id": "118764", "name": "a young rat" } }
    echo(gmcp_data)

    # make sure we're getting room info
    if gmcp_data["location"] != "room":
        return None

    # see if we can find that mob in the list
    item = gmcp_data["item"]
    mob_to_remove = None
    for mob in v.mobs_in_room:
        if mob["id"] == item["id"]:
            echo(f"found mob to remove: {mob}")
            mob_to_remove = mob
            break
    if mob_to_remove is not None:
        v.mobs_in_room.remove(mob_to_remove)
add_gmcp_handler("Char.Items.Remove", mob_left_room)

