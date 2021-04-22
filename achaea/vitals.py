import ui.core
from client import c, echo

from achaea.state import s


# Char.Vitals:
# {"hp": "1350", "maxhp": "1350", "mp": "1485", "maxmp": "1485", "ep": "4600", "maxep": "4600", "wp": "4600", "maxwp": "4600", "nl": "1", "bal": "1", "eq": "1", "string": "H:1350/1350 M:1485/1485 E:4600/4600 W:4600/4600 NL:1/100 ", "charstats": ["Bleed: 0", "Rage: 0"]}


def gmcp_vitals(gmcp_data):
    prompt_text = create_prompt_text(gmcp_data)
    ui.core.update_prompt_info(prompt_text)


c.add_gmcp_handler("Char.Vitals", gmcp_vitals)


def get_char_stat(prompt_info, stat_type):
    char_stats = prompt_info.get("charstats", [])
    for stat in char_stats:
        if stat.startswith(stat_type):
            s_type, amount = stat.split(" ")
            return amount
    return "???"


def create_prompt_text(prompt_info):
    hp = prompt_info.get("hp", "???")
    max_hp = prompt_info.get("maxhp", "???")
    mp = prompt_info.get("mp", "???")
    max_mp = prompt_info.get("maxmp", "???")
    rage = get_char_stat(prompt_info, "Rage")
    bleed = get_char_stat(prompt_info, "Bleed")
    exits = ", ".join(s.room_info.exits.keys())
    return f"HP:{hp}/{max_hp} MP:{mp}/{max_mp} Rage:{rage} Bleed:{bleed} Exits: {exits}"
