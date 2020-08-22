
from .client import c, send, echo

def bopalopia_mult(matches):
    echo("mult")
    ans = int(matches[1]) * int(matches[2])
    send(f"say {ans}")


def bopalopia_div(matches):
    echo("div")
    ans = int(int(matches[1]) / int(matches[2]))
    send(f"say {ans}")


def bopalopia_add(matches):
    echo("add")
    ans = int(matches[1]) + int(matches[2]) + int(matches[3])
    send(f"say {ans}")


def bopalopia_sub(matches):
    echo("sub")
    ans = int(matches[1]) - int(matches[2])
    send(f"say {ans}")


bopalopia_triggers = [
    (   "^(Fernando|Junior) Moo",
        # multiply stuff
        lambda m: echo(f"bop {m[0]}")
    ),
    (   r"^(Fernando Moo|Junior Moo|Clarence Cudchew) says, \"If (.*) eggs were lain each by (.*) chickens, how many eggs would that make total?",
        # multiply stuff
        bopalopia_mult
    ),
    (   r"^(Fernando Moo|Junior Moo|Clarence Cudchew) says, \"If (.*) nuts were saved for winter storage and (.*) squirrels had to share, how many nuts would that be per squirrel?",
        # divide stuff
        bopalopia_div
    ),
    (   r"^(Fernando Moo|Junior Moo|Clarence Cudchew) says, \"If (.*) beavers and (.*) beavers got together with (.*) beavers, how many beavers would that be total?",
        # add stuff
        bopalopia_add
    ),
    (   r"^(Fernando Moo|Junior Moo|Clarence Cudchew) says, \"If (\d+) cows jumped into Runaway River and (\d+) drowned, how many cows would be left?",
        # subtract stuff
        bopalopia_sub
    ),
]
c.add_triggers(bopalopia_triggers)
