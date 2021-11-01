from queue import Queue

from achaea.priest import priest_status # import gmcp_priest_status
from achaea.state import s
from client import c


def test_gmcp_priest_status():
    data = {"hp": "4843", "maxhp": "4843", "mp": "4150", "maxmp": "4150", "ep": "19265", "maxep": "19265", "wp": "15800", "maxwp": "15800", "nl": "49", "bal": "1", "eq": "1", "string": "H:4843/4843 M:4150/4150 E:19265/19265 W:15800/15800 NL:49/100 ", "charstats": ["Bleed: 0", "Rage: 0", "Angelpower: 4767", "Devotion: 97%", "conviction: 10", "prayer_length: 0", "Prayer: Yes"]}

    priest_status.gmcp_priest_status(data)
    assert priest_status.angel_power == 4767
    assert priest_status.devotion == 97
    assert priest_status.conviction == 10
    assert priest_status.prayer_length == 0
    assert priest_status.prayer.lower() == "yes"
