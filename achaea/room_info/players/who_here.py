from achaea.fighting_log import fighting
from achaea.state import s
from client import c, echo
from telnet_manager import strip_ansi


def parse_who_here(current_chunk):
    current_chunk = strip_ansi(current_chunk)
    found_start = False
    for line in current_chunk.split("\r\n"):
        if "You see the following people here:" in line:
            found_start = True
        elif found_start:
            people_here = line.split(", ")
            break
    echo(f"people here: {people_here}")


who_here_triggers = [
    (
        r"^You see the following people here:$",
        # who here
        lambda _: parse_who_here(c.current_chunk),
    ),
]
c.add_triggers(who_here_triggers)

who_here_aliases = [
    (
        "^wh$",
        "who here",
        lambda _: c.send("who here"),
    ),
]
c.add_aliases("who_here", who_here_aliases)
