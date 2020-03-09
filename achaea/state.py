
import re

from datetime import datetime
from enum import Enum

class QueueStates(Enum):
    nothing_queued = 0
    attempting_queue = 1
    command_queued = 2


class State():

    def __init__(self):
        self.target = "rat"
        self.hp = 4000
        self.mp = 5000
        self.players_in_room = set()
        self.mobs_in_room = {}
        self.defences = set()
        self.wanted_defences = set()
        self.pt_announce = False
        self.enemies = set()
        self.ratting_room = 0
        self.eqbal_queue_state = QueueStates.nothing_queued
        self.eqbal_queue = []
        self.bal = "1"
        self.eq = "1"
        self.show_balance_times = False


s = State()


class DiffState():

    def __init__(self):
        self.echo_lines = []

    def echo(self, line):
        self.echo_lines.append(line)

    def __add__(self, other):
        new_ds = DiffState()
        new_ds.echo_lines = self.echo_lines.extend(other.echo_lines)

