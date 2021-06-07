from colorama import Fore

from client import c, echo, send

from achaea.basic import highlight_current_line
from achaea.fighting_log import fighting
from achaea.state import s


def run_from_room(matches):
    highlight_current_line(Fore.YELLOW)
    echo("RUN!!!")
    echo("RUN!!!")
    echo("RUN!!!")
    echo("RUN!!!")


def someone_shielded(matches):
    highlight_current_line(Fore.YELLOW)
    if matches[0].lower() == s.target.lower():
        echo("TARGET SHIELDED!!")
        echo("TARGET SHIELDED!!")
        fighting(f"{s.target} SHIELDED!!")
    else:
        fighting(f"{matches[0]} shielded!!")


def someone_rebounding(matches):
    highlight_current_line(Fore.YELLOW)
    if matches[0].lower() == s.target.lower():
        echo("TARGET REBOUNDING!!")
        echo("TARGET REBOUNDING!!")
        fighting(f"{s.target} REBOUNDING!!")


def someone_stopped_rebounding(matches):
    highlight_current_line(Fore.YELLOW)
    if matches[0].lower() == s.target.lower():
        echo("TARGET STOPPED REBOUNDING!!")
        echo("TARGET STOPPED REBOUNDING!!")
        fighting(f"{s.target} STOPPED REBOUNDING!!")
    else:
        fighting(f"{matches[0]} stopped rebounding!!")


# ["2020/03/24 22:47:43.405603", "server_text", "Kog has been slain by Atalkez.\r"]
def someone_died(matches):
    victim = matches[0]
    killer = matches[1]
    echo(f"{killer} killed {victim}!")
    fighting(f"{killer} killed {victim}!")
    send("queue prepend eqbal grab body")


def rakia():
    echo("STOP STOP STOP!!")
    echo("STOP STOP STOP!!")
    echo("STOP STOP STOP!!")
    echo("STOP STOP STOP!!")


# ["2020/03/24 22:47:47.882336", "server_text", "You suddenly perceive the vague outline of an aura of rebounding around Iocun.\r"]

generic_triggers = [
    (
        r"^Ra'mah, the Corrupted trains its eyes upon you and begins to growl",
        # room attack soon! run!!
        run_from_room,
    ),
    (
        r"^A nearly invisible magical shield forms around (.*?).$",
        # someone just shielded!
        someone_shielded,
    ),
    (
        r"^A dizzying beam of energy strikes you as your attack rebounds off of (.*)'s shield.$",
        # someone (probably my target) is shielded!
        someone_shielded,
    ),
    (
        r"^You suddenly perceive the vague outline of an aura of rebounding around (\w+?).$",
        # someone (probably my target) is shielded!
        someone_rebounding,
    ),
    (
        r"^You call upon Whiirh to empower your staff and strike (\w+), the power of air dispersing \w+ aura of rebounding.$",
        # someone (probably my target) is shielded!
        someone_stopped_rebounding,
    ),
    (
        r"^(.*)'s aura of weapons rebounding disappears.$",
        # someone (probably my target) is shielded!
        someone_stopped_rebounding,
    ),
    (
        r"exhales loudly.$",
        # don't need to see this!
        lambda m: c.delete_line(),
    ),
    (
        r"inhales and begins holding (\w+) breath.$",
        # don't need to see this!
        lambda m: c.delete_line(),
    ),
    (
        r"has been slain by",
        # don't need to see this!
        lambda m: someone_died,
    ),
    (
        r"You begin to tumble agilely to the (.*).$",
        # tumbling!
        lambda m: fighting(f"tumbling {m[0]}"),
    ),
    (
        r"The barrier around Torrid Rakia, the magma wyvern melts through the ground, and she rushes through to attack.$",
        # tumbling!
        lambda m: rakia(),
    ),
    (
        r"^You are already wielding that.$",
        lambda m: c.delete_line(),
    ),
]
c.add_triggers(generic_triggers)
