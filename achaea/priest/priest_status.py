from client import c, send

from achaea.basic import eqbal
from achaea.state import s


angel_power = 0
devotion = 0
conviction = 0
prayer_length = 0
prayer = ""


def gmcp_priest_status(gmcp_data):
    # {"type": "Char.Vitals", "data": {"hp": "4843", "maxhp": "4843", "mp": "4150", "maxmp": "4150", "ep": "19265", "maxep": "19265", "wp": "15800", "maxwp": "15800", "nl": "49", "bal": "1", "eq": "1", "string": "H:4843/4843 M:4150/4150 E:19265/19265 W:15800/15800 NL:49/100 ", "charstats": ["Bleed: 0", "Rage: 0", "Angelpower: 4767", "Devotion: 97%", "conviction: 10", "prayer_length: 0", "Prayer: Yes"]}}
    char_stats = gmcp_data.get("charstats", [])
    for stat in char_stats:
        name, value = stat.split(": ")

        if name.lower() == "angelpower":
            global angel_power
            angel_power = int(value)
            #c.echo(f"angel_power: {angel_power}")

        elif name.lower() == "devotion":
            global devotion
            devotion = int(value.rstrip("%"))
            #c.echo(f"devotion: {devotion}")

        elif name.lower() == "conviction":
            global conviction
            conviction = int(value)
            #c.echo(f"conviction: {conviction}")

        elif name.lower() == "prayer_length":
            global prayer_length
            prayer_length = int(value)
            #c.echo(f"prayer_length: {prayer_length}")

        elif name.lower() == "prayer":
            global prayer
            prayer = value
            #c.echo(f"prayer: {prayer}")

c.add_gmcp_handler("Char.Vitals", gmcp_priest_status)
