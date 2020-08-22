
import json
import logging
import re

from datetime import datetime

from ..client import c, send, echo
from ..state import s


logger = logging.getLogger("achaea")


room_aliases = [
    (   "^cir$",
        "Char.Items.Room",
        lambda matches: c.gmcp_send("Char.Items.Room \"\"")
    ),
]
c.add_aliases("room_info", room_aliases)


def add_player(gmcp_data):
    # {"name": "Adrik", "fullname": "Adrik Bergson, the Crystalline Song"}
    player = gmcp_data["name"]
    echo(f"+{player}")
    logger.fighting(f"+{player}")
    s.players_in_room = (*s.players_in_room, player)
#c.add_gmcp_handler("Room.AddPlayer", add_player)


def remove_player(gmcp_data):
    # "Farrah"
    echo(f"-{gmcp_data}")
    logger.fighting(f"-{gmcp_data}")
    players = set(s.players_in_room).discard(gmcp_data)
    s.players_in_room = tuple(players)
#c.add_gmcp_handler("Room.RemovePlayer", remove_player)


def room_players(gmcp_data):
    # [{"name": "Vhaith", "fullname": "Shield Curator Vhaith Rian-Moonshadow"}, {"name": "Vindiconis", "fullname": "Volunteer Vindiconis"}]
    me = {"Vindiconis", "Dirus", "Palleo", "Sarmenti"}
    players = {player["name"] for player in gmcp_data}
    players.difference_update(me)
    echo(f"+{', '.join(players)}")
    s.players_in_room = tuple(players)
#c.add_gmcp_handler("Room.Players", room_players)
