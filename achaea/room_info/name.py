
import json

from client import c, send, echo


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
            echo(f"name_map conflict: {long_name} => {short_name} / {old_short_name}")
    else:
        echo(f"Adding: {long_name} -> {short_name}")
        long_short_name_map[long_name] = short_name
        save_name_map(DEFAULT_NAME_MAP_PATH)


def figure_out_unknown_mobs(mobs):
    trigger_names = []
    echo(f"trying to figure out: {mobs}")
    for mob_id, long_name in mobs:

        trigger_name = f"mob_id{mob_id}"
        trigger_names.append(trigger_name)
        echo(f"creating trig for: {mob_id} / {long_name}")

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
