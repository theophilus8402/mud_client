from achaea.room_info.mobs_in_room import (
    find_mobs_in_room,
    mob_entered_room,
    mob_left_room,
)
from achaea.room_info.room_info import create_frenemies_text
from achaea.state import s


class TestRoomInfo:
    def test_create_frenemies_text(self):
        gmcp_data = {
            "location": "room",
            "items": [
                {"id": "113519", "name": "a runic totem", "icon": "rune"},
                {
                    "id": "293949",
                    "name": "Jodri, Shepherd of the Devout",
                    "icon": "humanoid",
                    "attrib": "m",
                },
                {
                    "id": "544262",
                    "name": "a monolith sigil",
                    "icon": "rune",
                    "attrib": "t",
                },
            ],
        }
        find_mobs_in_room(gmcp_data)

        gmcp_data = {
            "location": "room",
            "item": {
                "id": "118764",
                "name": "a young rat",
                "icon": "animal",
                "attrib": "m",
            },
        }
        mob_entered_room(gmcp_data)

        assert len(s.mobs_in_room) == 2
        assert s.mobs_in_room[0][0] == "jodri293949"

        frenemies = create_frenemies_text()
        assert frenemies == "jodri293949 rat118764 "

        gmcp_data = {
            "location": "room",
            "item": {"id": "118764", "name": "a young rat"},
        }
        mob_left_room(gmcp_data)
        assert len(s.mobs_in_room) == 1

        frenemies = create_frenemies_text()
        assert frenemies == "jodri293949 "
