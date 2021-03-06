import logging

from achaea.room_info.name import figure_out_unknown_mobs, long_short_name_map
from achaea.room_info.room_info import create_frenemies_text
from achaea.state import s
from client import c, echo, send
from ui.core import update_frenemies_info



def find_mobs_in_room(gmcp_data):
    # Char.Items.List {"location": "room", "items": [{"id": "113519", "name": "a runic totem", "icon": "rune"}, {"id": "293949", "name": "Jodri, Shepherd of the Devout", "icon": "humanoid", "attrib": "m"}, {"id": "544262", "name": "a monolith sigil", "icon": "rune", "attrib": "t"}]}
    # echo(gmcp_data)

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

    # push to the ui
    frenemies_text = create_frenemies_text()
    update_frenemies_info(frenemies_text)


c.add_gmcp_handler("Char.Items.List", find_mobs_in_room)


def mob_entered_room(gmcp_data):
    # Char.Items.Add { "location": "room", "item": { "id": "118764", "name": "a young rat", "icon": "animal", "attrib": "m" } }

    # Char.Items.Add {"location": "room", "item": {"id": "31722", "name": "a stirge's egg"}}

    if gmcp_data["location"] == "room" and "m" in gmcp_data.get("item", {}).get(
        "attrib", []
    ):
        item = gmcp_data["item"]
        short_name, mob_id = get_mob_id(item)
        item["short_name"] = short_name
        s.mobs_in_room = (*s.mobs_in_room, (mob_id, item))

    # push to the ui
    frenemies_text = create_frenemies_text()
    update_frenemies_info(frenemies_text)


c.add_gmcp_handler("Char.Items.Add", mob_entered_room)


def mob_left_room(gmcp_data):
    # Char.Items.Remove { "location": "room", "item": { "id": "118764", "name": "a young rat" } }
    # echo(gmcp_data)

    # make sure we're getting room info
    if gmcp_data["location"] != "room":
        return None

    # see if we can find that mob in the list
    item = gmcp_data["item"]
    mobs = []
    for mob_id, mob_info in s.mobs_in_room:
        if not mob_id.endswith(item["id"]):
            mobs.append((mob_id, mob_info))
    s.mobs_in_room = tuple(mobs)

    # push to the ui
    frenemies_text = create_frenemies_text()
    update_frenemies_info(frenemies_text)


c.add_gmcp_handler("Char.Items.Remove", mob_left_room)


def get_mob_id(gmcp_data):
    #'106482': {'id': '106482', 'name': 'a young rat', 'icon': 'animal', 'attrib': 'm'}
    long_name = gmcp_data["name"]
    mob_id = gmcp_data["id"]
    if long_name not in long_short_name_map:
        echo(f"didn't find: {long_name}")
    short_name = long_short_name_map.get(long_name, "")
    return short_name, f"{short_name}{mob_id}"


def is_alive_mob(gmcp_data):
    # "d" in attrib means it's dead so we don't care
    return "m" in gmcp_data.get("attrib", "") and "d" not in gmcp_data.get("attrib", "")


def get_mobs_from_items(items):
    unknown_mobs = []
    mobs = []

    for item in items:
        if not is_alive_mob(item):
            continue

        short_name, mob_id = get_mob_id(item)
        item["short_name"] = short_name
        mobs.append((mob_id, item))

        if mob_id.isdigit():
            unknown_mobs.append((mob_id, item["name"]))

    if unknown_mobs:
        figure_out_unknown_mobs(unknown_mobs)

    return mobs
