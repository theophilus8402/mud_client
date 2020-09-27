
import collections
import itertools
import json
import logging
import re

from datetime import datetime

from ..client import c, send, echo
from ..state import s
from ..room_info.mapping import store_room
from ui.core import update_frenemies_info


logger = logging.getLogger("achaea")


StateRoomInfo = collections.namedtuple("StateRoomInfo",
                    "num name desc area environment coords map details exits")


room_aliases = [
    (   "^cir$",
        "Char.Items.Room",
        lambda matches: c.gmcp_send("Char.Items.Room \"\"")
    ),
]
c.add_aliases("room_info", room_aliases)


def get_room_info(gmcp_data):
    # store the info in the db
    store_room(gmcp_data)

    if "ohmap" in gmcp_data.keys():
        # this is a wilderness map/room
        return

    # store it in the state
    s.room_info = StateRoomInfo(**gmcp_data)
c.add_gmcp_handler("Room.Info", get_room_info)

# set default room info for when we first load up
s.room_info = StateRoomInfo(num="???",
                            name="???",
                            desc="???",
                            area="???",
                            environment="???",
                            coords="???",
                            map="???",
                            details="???",
                            exits={})


def create_frenemies_text():
    mobs = [mid for mid, minfo in s.mobs_in_room]
    players = set(s.players_in_room).difference(s.enemies_in_room)
    return " ".join(itertools.chain(s.enemies_in_room, mobs, players))


def add_player(gmcp_data):
    # {"name": "Adrik", "fullname": "Adrik Bergson, the Crystalline Song"}
    player = gmcp_data["name"]
    echo(f"+{player}")
    logger.fighting(f"+{player}")
    s.players_in_room = (*s.players_in_room, player)
    frenemies_text = create_frenemies_text()
    update_frenemies_info(frenemies_text)
c.add_gmcp_handler("Room.AddPlayer", add_player)


def remove_player(gmcp_data):
    # "Farrah"
    echo(f"-{gmcp_data}")
    logger.fighting(f"-{gmcp_data}")
    players = set(s.players_in_room).discard(gmcp_data)
    if players:
        s.players_in_room = tuple(players)
    else:
        s.players_in_room = tuple()
    frenemies_text = create_frenemies_text()
    update_frenemies_info(frenemies_text)
c.add_gmcp_handler("Room.RemovePlayer", remove_player)


def room_players(gmcp_data):
    # [{"name": "Vhaith", "fullname": "Shield Curator Vhaith Rian-Moonshadow"}, {"name": "Vindiconis", "fullname": "Volunteer Vindiconis"}]
    me = {"Vindiconis", "Dirus", "Palleo", "Sarmenti"}
    players = {player["name"] for player in gmcp_data}
    players.difference_update(me)
    echo(f"+{', '.join(players)}")
    s.players_in_room = tuple(players)
    frenemies_text = create_frenemies_text()
    update_frenemies_info(frenemies_text)
c.add_gmcp_handler("Room.Players", room_players)
