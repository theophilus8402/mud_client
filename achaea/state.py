
import re

from datetime import datetime
from achaea.client import echo

class State():

    def __init__(self):
        self.target = "rat"
        self.players_in_room = set()
        self.mobs_in_room = {}
        self.defences = set()
        self.wanted_defences = set()
        self.pt_announce = False
        self.enemies = set()
        self.ratting_room = 0


s = State()

