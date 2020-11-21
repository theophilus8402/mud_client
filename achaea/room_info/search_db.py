from copy import copy

from .db import Session
from .models import RoomInfo

session = Session()

# q.filter(models.RoomInfo.name.ilike("%stone%"), models.RoomInfo.area.ilike("cyrene")).all()


def find_rooms(parameters, ilike=True):
    filter_terms = []
    for col_name, search_term in parameters.items():
        col = getattr(RoomInfo, col_name)
        filter_terms.append(col.ilike(f"%{search_term}%"))

    results = []
    wanted_keys = ["area", "name", "num", "exits", "environment", "desc", "details"]
    for room in session.query(RoomInfo).filter(*filter_terms).all():
        room_dict = {key: getattr(room, key) for key in wanted_keys}
        results.append(room_dict)
    return results
