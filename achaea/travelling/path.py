from typing import List, Set, Dict, Tuple

from client import c, echo
from achaea.room_info.room_info import room_watcher

# paths is just a flat "name" : [(dir, room_num)]
paths: Dict[str, List[Tuple[str, str]]] = {}

# path_recording is ("name", PathRecorder())
# there should only be one active path recorder
path_recording = None


class Pather():

    def __init__(self, path):
        self.path = path

    def __next__(self):
        pass


class PathRecorder():

    def __init__(self):
        self.path = []
        self.last_room = None
        room_watcher.attach(self)

    def stop(self):
        room_watcher.detach(self)

    def update(self, room_info):
        try:
            if self.last_room.num != room_info.num:
                echo(f"PathRecorder({id(self)}): new room ({room_info.num})")

                # find the exit used pertaining to the new room
                for direction, room_num in self.last_room.exits.items():
                    if room_num == room_info.num:
                        echo(f"adding ({direction}, {room_num}) to path")
                        self.path.append((direction, room_num))
                        break
                self.last_room = room_info

                echo(f"path: {self.path}")
        except AttributeError as e:
            echo(f"PathRecorder: probably haven't seen a last_room yet")
            self.last_room = room_info


def path_list():
    echo(f"paths:")
    global paths
    for name, path in paths.items():
        echo(f"{name}: {path}")


def path_record(name):
    global paths
    global path_recording

    if name == "stop":
        if not path_recording:
            echo(f"not recording a path!")
            return

        name, path_recorder = path_recording
        path = path_recorder.path
        paths[name] = path

        echo(f"stopping path recording ({id(path_recorder)}): {name}")
        path_recording = None
        path_recorder.stop()

        echo(f"paths[\"{name}\"] = {path}")


    elif paths.get(name):
        echo(f"path {name} already exists")
        echo(f"PATH CLEAR {name.toupper()} to clear the path")

    elif path_recording:
        name, path_recorder = path_recording
        echo(f"already recording: {name}")
        echo(f"PATH RECORD STOP to stop recording and start a new one")

    else:
        echo(f"Beginning path record: {name}")
        path_recording = (name, PathRecorder())


path_aliases = [
    (
        "path list",
        "path list",
        lambda m: path_list()
    ),
    (
        "path record (.*)",
        "path record name",
        lambda m: path_record(m[0])
    ),
    (
        "path record stop",
        "path record stop",
        lambda m: path_record("stop")
    ),
]
c.add_aliases("path", path_aliases)
