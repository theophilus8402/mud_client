
from copy import copy

from ..client import send, add_gmcp_handler, echo, add_aliases
from .db import Session
from .models import RoomInfo
from ..variables import v

session = Session()

def room_in_db(room_num):
    return session.query(RoomInfo).filter(RoomInfo.num==room_num).one_or_none()

def store_room(gmcp_data):
    room_num = gmcp_data["num"]
    if not room_in_db(room_num):
        echo(f"Egads!  {room_num} hasn't been stored!  Adding it now!")
        echo(f"{gmcp_data}")
        room_info = copy(gmcp_data)
        room_info["details"] = str(gmcp_data["details"])
        room_info["exits"] = str(gmcp_data["exits"])
        try:
            room = RoomInfo(**room_info)
            session.add(room)
            session.commit()
        except:
            echo("eep!  Something is happening")
add_gmcp_handler("Room.Info", store_room)

