
from collections import namedtuple

from client import c, send, echo


"""
Char.Items.Remove {"location": "room", "item": {"id": "54532", "name": "a large wall of ice"}}
The icewall quickly melts into nothingness.

# this in the room description
An icewall is here, blocking passage to the north.

Char.Items.Add {"location": "room", "item": {"id": "550634", "name": "a large wall of ice"}}
Isaiah raises his hands dramatically and summons an icewall to the north.

Char.Items.Add {"location": "room", "item": {"id": "54532", "name": "a large wall of ice"}}
Isaiah raises his hands dramatically and summons an icewall to the west.

An icewall suddenly forms to the north.

An icewall is here, blocking passage to the west.

Char.Items.Add {"location": "room", "item": {"id": "467010", "name": "a lightwall"}}
Isaiah forms a ball of light in his palm and hurls it northeastwards.

Char.Items.List {"location": "room", "items": [{"id": "176739", "name": "a sewer grate", "icon": "door"}, {"id": "183679", "name": "a shrine of Sartan", "icon": "shrine"}, {"id": "538360", "name": "a flail-wielding knight", "icon": "guard", "attrib": "mx"}, {"id": "169411", "name": "a monolith sigil", "icon": "rune", "attrib": "t"}, {"id": "54532", "name": "a large wall of ice"}, {"id": "467010", "name": "a lightwall"}, {"id": "480209", "name": "a large wall of ice"}]}}
# a large wall of ice
# a lightwall
"""

RoomHindrance = namedtuple("RoomHindrance", "name short_name id direction")

def add_room_hindrance(gmcp_data):
    # Char.Items.Add
    # {"location": "room", "item": {"id": "550634", "name": "a large wall of ice"}}

    # make sure it's for the room
    if gmcp_data.get("location") != "room":
        return

    item = gmcp_data.get("item", {})
    name = item.get("name", "")

    if name in ROOM_HINDRANCE_NAMES:
        new_hindrance = RoomHindrance(name=name,
                                      short_name=SHORT_NAMES[name],
                                      id=item.get("id", "")
                                      direction="?"
                                    )

        # store it in the state
        s.room_hindrance = (*s.room_hindrance, new_hindrance)
c.add_gmcp_handler("Char.Items.Add", add_room_hindrance)
