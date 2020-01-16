
from datetime import datetime

from .client import add_temp_trigger, remove_temp_trigger

class Variable():

    def __init__(self):
        self.target = "rat"
        self.last_rat_call = datetime.now()
        self._rat_last_seen = datetime.now()
        self.ratting_room = 0
        self.players_in_room = set()
        self.rats_killed_in_room = 0
        self.mobs_in_room = set()
        self.defences = set()
        self.wanted_defences = set()
        add_temp_trigger("target_trigger", ("target_trigger", lambda m: False))
        self.handles = {}
        self.open_handle("says", "says.log")
        self.says_handle = self.handles["says"]
        self.pt_announce = False
        self.enemies = set()

    def open_handle(self, name, file_path):
        self.handles[name] = open(file_path, "a")

    @property
    def rat_last_seen(self):
        for mob in self.mobs_in_room:
            if "rat" in mob["name"]:
                self._rat_last_seen = datetime.now()
                break
        return self._rat_last_seen

v = Variable()

