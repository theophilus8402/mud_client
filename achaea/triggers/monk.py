from colorama import Fore

from achaea.basic import highlight_current_line
from achaea.fighting_log import fighting
from achaea.state import s
from client import c, echo, send


def being_radianced(matches):
    highlight_current_line(Fore.RED)
    echo("YOU'RE BEING RADIANCED!! GET OUT OF HERE!!!")
    fighting(f"YOU'RE BEING RADIANCED!! GET OUT OF HERE!!!")


def got_blackout(matches):
    echo("Got BLACKOUT!!! Concentrate, soonish??")


monk_triggers = [
    (
        r"^A shimmering image of the face of (.*) appears fleetingly before you, frowning in concentration.$",
        # you're being radianced!
        being_radianced,
    ),
    (
        r"^Sparks of multicoloured light begin to dance in your mind.$",
        # you're being radianced!
        being_radianced,
    ),
    (
        r"^An odd sensation of warmth begins to fill your body.$",
        # you're being radianced!
        being_radianced,
    ),
    (
        r"^Arcs of white light begin to flash across your vision, radiant and bright.$",
        # you're being radianced!
        being_radianced,
    ),
    (
        r"^Your heart thumps as you realise that you have but seconds left to escape whatever fate awaits you.$",
        # you're being radianced!
        being_radianced,
    ),
    (
        r"^A devastating blast of telepathic energy strikes you and your senses black out completely...$",
        # blackout
        got_blackout,
    ),
]
c.add_triggers(monk_triggers)
