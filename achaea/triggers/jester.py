from achaea.state import s
from client import c, echo, send
from client.timers import timers


def reject_lust(luster):
    echo(f"{luster} LUSTED YOU!!! REJECT {luster}")
    timers.add(
        f"reject_{luster}1",
        lambda luster: echo(f"{luster} LUSTED YOU!!! REJECT {luster}"),
        1,
    )
    timers.add(
        f"reject_{luster}2",
        lambda luster: echo(f"{luster} LUSTED YOU!!! REJECT {luster}"),
        3,
    )
    timers.add(
        f"reject_{luster}3",
        lambda luster: echo(f"{luster} LUSTED YOU!!! REJECT {luster}"),
        6,
    )


jester_triggers = [
    (
        r"^(\w+) quickly flings a tarot card at you, and you feel unreasonable lust for \w+.",
        lambda m: reject_lust(m[0]),
    ),
]
c.add_triggers(jester_triggers)
