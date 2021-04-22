import re

from client import c
from telnet_manager import strip_ansi


class FrenemyWatcher():

    def __init__(self):
        self._observers = []

    def attach(self, observer, frenemy_type):
        self._observers.append((observer, frenemy_type))

    def detach(self, observer):
        for obs in self._observers:
            _observer, frenemy_type = obs
            if _observer == observer:
                self._observers.remove(obs)

    def notify(self, frenemy_type, frenemy_list):
        for observer in self._observers:
            observer.update(frenemy_type, frenemy_list)

frenemy = FrenemyWatcher()
allies = []
enemies = []


re_allies = re.compile(r"(\w+) is an ally", re.MULTILINE)

def parse_allies(current_chunk):
    """
    You have the following allies:
    Ada is an ally (M).
    Aina is an ally.
    Rhogan is an ally.
    You have currently used 5 ally slots of your 20 maximum.
    """
    global allies
    global frenemy
    current_chunk = strip_ansi(current_chunk)
    allies = re_allies.findall(current_chunk)
    c.echo(f"allies: {' '.join(allies)}")
    frenemy.notify("allies", allies)


re_enemies = re.compile("You have the following enemies:\r\n(.*)\r\nYou have currently used \\d+ enemy slots of your \\d+ maximum.", flags=re.MULTILINE|re.DOTALL)

def parse_enemies(current_chunk):
    """
    You have the following enemies:
    Farrah
    Mezghar
    You have currently used 2 enemy slots of your 20 maximum.
    """
    global enemies
    global frenemy
    current_chunk = strip_ansi(current_chunk)
    m = re_enemies.search(current_chunk)
    enemies = m.groups()[0].split("\r\n")
    c.echo(f"enemies: {' '.join(enemies)}")
    frenemy.notify("enemies", enemies)


frenemy_triggers = [
    (
        r"^You have the following allies:$",
        lambda _: parse_allies(c.current_chunk),
    ),
    (
        r"^You have the following enemies:$",
        lambda _: parse_enemies(c.current_chunk),
    ),
]
c.add_triggers(frenemy_triggers)
