
import re

from datetime import datetime

from .client import send, add_gmcp_handler, echo
from .variables import v


def find_mobs_in_room(gmcp_data):
    if gmcp_data["location"] != "room":
        return False
    mobs = [item for item in gmcp_data["items"] if "m" in item.get("attrib", "")]
    v.mobs_in_room = mobs
add_gmcp_handler("Char.Items.List", find_mobs_in_room)

def mob_entered_room(gmcp_data):
    try:
        if (gmcp_data["location"] == "room" and
            "m" in gmcp_data["item"].get("attrib")):
            v.mobs_in_room.append(gmcp_data["item"])
    except TypeError:
        print(f"GMCP data, mob_entered_room <{gmcp_data}> None!!")
add_gmcp_handler("Char.Items.Add", mob_entered_room)


def mob_left_room(gmcp_data):
    if gmcp_data["location"] != "room":
        return None

    item = gmcp_data["item"]
    # see if we can find that mob in the list
    mob_to_remove = None
    for i in range(len(v.mobs_in_room)):
        mob = v.mobs_in_room[i]
        if mob["id"] == item["id"]:
            print(f"found mob to remove: {mob}")
            mob_to_remove = i
            break
    if mob_to_remove is not None:
        v.mobs_in_room.pop(mob_to_remove)
add_gmcp_handler("Char.Items.Remove", mob_left_room)

