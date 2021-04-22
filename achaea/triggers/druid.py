from colorama import Fore

from achaea.basic import highlight_current_line
from achaea.fighting_log import fighting
from achaea.state import s
from client import c, echo, send


def being_grove_summoned(matches):
    highlight_current_line(Fore.RED)

    if matches:
        echo(f"{matches[0].upper()} IS BEING GROVE SUMMONED!!!!")
        fighting(f"{matches[0].upper()} IS BEING GROVE SUMMONED!!")
    else:
        echo("YOU'RE BEING GROVE SUMMONED!!!! SHIELD!!!")
        fighting(f"YOU'RE BEING GROVE SUMMONED!! SHIELD!!!")


druid_triggers = [
    (
        r"^The forest leaves rustle about you menacingly as the undergrowth appears to close in on you.$",
        # you're being grove summoned!
        being_grove_summoned,
    ),
    (
        r"^The forest undergrowth seems to move menacingly closer towards (.*).$",
        # you're being grove summoned!
        being_grove_summoned,
    ),
]
c.add_triggers(druid_triggers)
