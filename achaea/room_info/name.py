
import json

from ..client import c, send


DEFAULT_NAME_MAP_PATH = "achaea/room_info/long_short_name_map.json"


def load_name_map(name_map_path):
    with open(name_map_path) as f:
        return json.load(f)


def save_name_map(name_map_path):
    with open(name_map_path, "w") as f:
        json.dump(long_short_name_map, f, indent=2)


long_short_name_map = load_name_map(DEFAULT_NAME_MAP_PATH)


def update_name_map(long_name, short_name):
    if long_name in long_short_name_map:
        old_short_name = long_short_name_map[long_name]
        if old_short_name != short_name:
            print(f"name_map conflict: {long_name} => {short_name} / {old_short_name}")
    else:
        print(f"Adding: {long_name} -> {short_name}")
        long_short_name_map[long_name] = short_name
        save_name_map(DEFAULT_NAME_MAP_PATH)


def figure_out_unknown_mobs(mobs):
    trigger_names = []
    print(f"trying to figure out: {mobs}")
    for mob_id, long_name in mobs:

        trigger_name = f"mob_id{mob_id}"
        trigger_names.append(trigger_name)
        print(f"creating trig for: {mob_id} / {long_name}")

        mob_trigger = (
            f"^(\w+){mob_id}\s+{long_name}$",
            lambda m: update_name_map(long_name, m[0])
            )
        c.add_temp_trigger(trigger_name, mob_trigger)

    send("ih")
    trigger_names.append("info_here")
    info_here_trigger = (
        f"^Number of objects: \d+$",
        lambda m: [c.remove_temp_trigger(tn) for tn in trigger_names]
        )
    c.add_temp_trigger("info_here", info_here_trigger)
    


def get_mob_id(gmcp_data):
    #'106482': {'id': '106482', 'name': 'a young rat', 'icon': 'animal', 'attrib': 'm'}
    long_name = gmcp_data["name"]
    mob_id = gmcp_data["id"]
    if long_name not in long_short_name_map:
        print(f"didn't find: {long_name}")
        return mob_id
    short_name = long_short_name_map[long_name]
    return f"{short_name}{mob_id}"


def is_alive_mob(gmcp_data):
    # "d" in attrib means it's dead so we don't care
    return ("m" in gmcp_data.get("attrib", "")
            and "d" not in gmcp_data.get("attrib", ""))


def get_mobs_from_items(items):
    unknown_mobs = []
    mobs = {}

    for item in items:
        if not is_alive_mob(item):
            continue

        mob_id = get_mob_id(item)
        mobs[mob_id] = item

        if mob_id.isdigit():
            unknown_mobs.append((mob_id, item["name"]))

    if unknown_mobs:
        figure_out_unknown_mobs(unknown_mobs)

    return mobs
