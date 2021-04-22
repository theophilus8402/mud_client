from copy import copy

class SimpleMove():

    def __init__(self, path):
        self._orig_path = path
        self._path = copy(path)

    def next_move(self, current_room_id):
        pass
