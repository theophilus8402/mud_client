
from colorama import Fore

from ..basic import highlight_current_line
from ..client import c, send, echo
from ..state import s


def someone_shielded(matches):
    highlight_current_line(Fore.YELLOW)
    if matches[0].lower() == s.target.lower():
        echo("TARGET SHIELDED!!")
        echo("TARGET SHIELDED!!")


def someone_rebounding(matches):
    highlight_current_line(Fore.YELLOW)
    if matches[0].lower() == s.target.lower():
        echo("TARGET REBOUNDING!!")
        echo("TARGET REBOUNDING!!")


def someone_stopped_rebounding(matches):
    highlight_current_line(Fore.YELLOW)
    if matches[0].lower() == s.target.lower():
        echo("TARGET STOPPED REBOUNDING!!")
        echo("TARGET STOPPED REBOUNDING!!")


# ["2020/03/24 22:47:43.405603", "server_text", "Kog has been slain by Atalkez.\r"]
def someone_died(matches):
    victim = matches[0]
    killer = matches[1]
    echo(f"{killer} killed {victim}!")
    echo(f"TODO: add this to the fighting log and have it affect targetting!!")
    send("queue prepend eqbal grab body")


#["2020/03/24 22:47:47.882336", "server_text", "You suddenly perceive the vague outline of an aura of rebounding around Iocun.\r"]

generic_triggers = [
    (   r"^A nearly invisible magical shield forms around (.*).$",
        # someone just shielded!
        someone_shielded
    ),
    (   r"^A dizzying beam of energy strikes you as your attack rebounds off of (.*)'s shield.$",
        # someone (probably my target) is shielded!
        someone_shielded
    ),
    (   r"^You suddenly perceive the vague outline of an aura of rebounding around (\w+).$",
        # someone (probably my target) is shielded!
        someone_rebounding
    ),
    (   r"^You call upon Whiirh to empower your staff and strike (\w+), the power of air dispersing \w+ aura of rebounding.$",
        # someone (probably my target) is shielded!
        someone_stopped_rebounding
    ),
    (   r"exhales loudly.$",
        # don't need to see this!
        lambda m: c.delete_line()
    ),
    (   r"inhales and begins holding (\w+) breath.$",
        # don't need to see this!
        lambda m: c.delete_line()
    ),
    (   r"(.*) has been slain by (.*).$",
        # don't need to see this!
        lambda m: someone_died
    ),
]
c.add_triggers(generic_triggers)
