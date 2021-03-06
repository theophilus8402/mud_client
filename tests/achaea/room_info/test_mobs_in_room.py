from achaea.room_info.mobs_in_room import *
from achaea.state import get_state_changes, s


class TestMobsInRoom:
    def test_is_alive_mob(self):
        totem_info = {"id": "113519", "name": "a runic totem", "icon": "rune"}
        assert is_alive_mob(totem_info) == False

        mob_info = {
            "id": "293949",
            "name": "Jodri, Shepherd of the Devout",
            "icon": "humanoid",
            "attrib": "m",
        }
        assert is_alive_mob(mob_info) == True

        dead_info = {
            "id": "293949",
            "name": "Jodri, Shepherd of the Devout",
            "icon": "humanoid",
            "attrib": "md",
        }
        assert is_alive_mob(dead_info) == False

    def test_get_mobs_from_items(self):
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

        mobs = get_mobs_from_items(gmcp_data.get("items"))
        assert len(mobs) == 1
        assert type(mobs) == type(list())

    def test_find_mobs_in_room(self):
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
        # changes_index = len(s._changes)
        find_mobs_in_room(gmcp_data)
        # changes = get_state_changes(s, changes_index)
        assert len(s.mobs_in_room) == 1
        assert s.mobs_in_room[0][0] == "jodri293949"

    def test_mob_entered_room(self):
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
        assert len(s.mobs_in_room) == 1
        assert s.mobs_in_room[0][0] == "jodri293949"

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
        assert s.mobs_in_room[1][0] == "rat118764"

    def test_mob_left_room(self):
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
        assert s.mobs_in_room[1][0] == "rat118764"

        gmcp_data = {
            "location": "room",
            "item": {"id": "118764", "name": "a young rat"},
        }
        mob_left_room(gmcp_data)
        assert len(s.mobs_in_room) == 1
