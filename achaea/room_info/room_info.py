
import re

from datetime import datetime

from ..client import c, send, echo
from ..state import s


def find_mobs_in_room(gmcp_data):
    #echo(gmcp_data)

    # make sure we're getting room info
    if gmcp_data["location"] != "room":
        return False

    # find all the mobs
    mobs = {item["id"] : item for item in gmcp_data["items"]
                                if "m" in item.get("attrib", "")}

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
            s.mobs_in_room[item["id"]] = item
    except TypeError:
        echo(f"GMCP data, mob_entered_room <{gmcp_data}> None!!")
c.add_gmcp_handler("Char.Items.Add", mob_entered_room)


def mob_left_room(gmcp_data):
    # Char.Items.Remove { "location": "room", "item": { "id": "118764", "name": "a young rat" } }
    echo(gmcp_data)

    # make sure we're getting room info
    if gmcp_data["location"] != "room":
        return None

    # see if we can find that mob in the list
    item = gmcp_data["item"]
    if item["id"] in s.mobs_in_room.keys():
        #echo(f"found mob to remove: {item['id']}")
        s.mobs_in_room.pop(item["id"])
c.add_gmcp_handler("Char.Items.Remove", mob_left_room)

