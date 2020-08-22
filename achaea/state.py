
import re

from datetime import datetime
from enum import Enum

class QueueStates(Enum):
    nothing_queued = 0
    attempting_queue = 1
    command_queued = 2


def name_exists(state, name):
    return name in object.__getattribute__(state, "__dict__")

def value_type_unchanged(state, name, value):
    old_type = type(object.__getattribute__(state, name))
    new_type = type(value)

    if old_type == new_type:
        return True
    else:
        raise AttributeError(f"{name} changing type from {old_type} to {new_type}!")

def is_immutable(value):
    mutable_attributes = ["__setitem__", "__delitem__", "insert", "add", "discard"]
    return not any(map(lambda attr: hasattr(value, attr), mutable_attributes))

def get_state_changes(state, last_index):
    return object.__getattribute__(state, "_changes")[last_index-1:]


class State():

    _changes_max_size = 10

    def __init__(self):
        # need to handle _changes outside because we want this to be a list
        # and we're making sure other things are immutable
        object.__setattr__(self, "_changes", list())

        self.target = "rat"
        self.hp = 4000
        self.mp = 5000
        self.players_in_room = tuple()
        self.mobs_in_room = tuple()
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

        # from afflictions.py
        self.new_afflictions = set()
        self.cured_afflictions = set()
        self.current_afflictions = set()

    def __setattr__(self, name, value):

        # check to see if the name already exists
        if name_exists(self, name):
            # make sure the new value's type doesn't change
            value_type_unchanged(self, name, value)

        # make sure the new value is immutable
        #if not is_immutable(value):
        #    raise ValueError(f"{name} type: {type(value)} is mutable!")

        object.__setattr__(self, name, value)

        # append changes to _changes... would get in a cycle if we let it
        # do stuff to _changes... so have to call lower stuff on it?
        changes = object.__getattribute__(self, "_changes")
        if len(changes) >= State._changes_max_size:
            changes.pop(0)
        changes.append((name, value))

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)


s = State()

