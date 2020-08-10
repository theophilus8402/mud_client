
import logging
import re

from colorama import *

from .client import c, send, echo
from .state import s, QueueStates


logger = logging.getLogger("achaea")

# this will get gmcp info about which player just authenticated
# it can be used to do a number of different things
# starting out, we'll use it to load different modules for different chars
def handle_login_info(gmcp_data):
    name = gmcp_data["name"]

    if name.lower() == "vindiconis":
        echo("Loading modules for vindiconis!")
        # magi modules
        from achaea.magi import ab_elementalism
        from achaea.magi import ab_crystalism
        from achaea.magi import ab_artificing
        from achaea.magi import fancy_attacks
        from achaea.magi import limb_counter
        from achaea.magi import affliction_tracker

    elif name.lower() == "palleo":
        echo("Loading modules for palleo!")
        # cleric modules
        from achaea.cleric import ab_spirituality
        from achaea.cleric import ab_devotion
        from achaea.cleric import ab_zeal

    elif name.lower() == "dirus":
        echo("Loading modules for dirus!")
        # occultist modules
        from achaea.occultist import ab_occultism
        from achaea.occultist import ab_tarot
        from achaea.occultist import ab_domination

    elif name.lower() == "theophilus":
        echo("Loading modules for theophilus!")
        # occultist modules
        from achaea.runewarden import ab_runelore
        from achaea.runewarden import ab_chivalry
        from achaea.runewarden import ab_weaponmastery
        from achaea.runewarden import ab_battlerage

c.add_gmcp_handler("Char.Name", handle_login_info)


def show_help(alias_group):
    lines = [f"{pattern:15.15} : {desc}" for pattern, desc in
                                            c.help_info.get(alias_group, [])]
    help_lines = "\n".join(lines)
    return echo(f"{alias_group}:\n{help_lines}")
    

base_aliases = [
    (   "#help (.*)",
        "show help",
        lambda m: show_help(m[0])
    ),
]
c.add_aliases("base", base_aliases)


def eqbal(msg):

    # TODO: is this even necessary any more?
    s.eqbal_queue.append(msg)

    for msg in s.eqbal_queue:
        send(f"queue add eqbal {msg}")
    s.eqbal_queue.clear()


def adding_eqbal_trig(matches):
    c.delete_line()


def readding_eqbal_trig(matches):
    c.delete_line()


def running_equilib_trig(matches):
    c.delete_line()


def no_eq_bal_trig(matches):
    if "Running queued" in c.current_chunk:
        c.delete_line()


def running_eqbal_trig(matches):
    c.delete_line()


queue_triggers = [
    (   r"^\[System\]: Added (.*) to your eqbal queue.",
        # catch lines for system eqbal
        adding_eqbal_trig
    ),
    (   r"(.*) was added to your equilibrium queue.$",
        # catch lines for system eqbal
        readding_eqbal_trig
    ),
    (   r"^\[System\]: Running queued equilibrium command: (.*)",
        # catch lines for system eqbal
        running_equilib_trig
    ),
    (   r"^You must regain equilibrium first.$",
        # catch lines for system eqbal
        no_eq_bal_trig
    ),
    (   r"^\[System\]: Running queued eqbal command: (.*)$",
        # catch lines for system eqbal
        running_eqbal_trig
    )
]
c.add_triggers(queue_triggers)

def curebal(cure):
    send(f"curing queue add {cure}")

def eat_herb(herb, mud=None, matches=None):
    send(f"outr {herb};eat {herb}")

def highlight_current_line(color, pattern=".*", flags=0):

    # this will highlight whatever matched the above pattern
    # it screws up any color/style that was before our highlight :(
    def replacer(match):
        return color + match.group() + Style.RESET_ALL

    line_to_highlight = c.modified_current_line or c.current_line
    line = re.sub(pattern, replacer, line_to_highlight, flags=flags)
    c.modified_current_line = line

def target(matches):
    # remove the previous target trigger
    c.remove_temp_trigger("target_trigger")

    # set the target
    s.target = matches[0]

    send(f"SETTARGET {s.target}")

    # set the target trigger
    target_trigger = (
            s.target,
            lambda m: highlight_current_line(Fore.RED, pattern=s.target, flags=re.I)
        )
    c.add_temp_trigger("target_trigger", target_trigger, flags=re.IGNORECASE)

    if s.pt_announce:
        send(f"pt Targeting: {s.target}")


basic_aliases = [
    (   "^t (.*)$",
        "target",
        target
    ),
    (   "^gg$",
        "get sovereigns",
        lambda m: eqbal("get sovereigns")
    ),
    (   "^pg$",
        "put sovereigns in pouch",
        lambda m: eqbal("put sovereigns in pouch;put sovereigns in pack")
    ),
    (   "^gp (\d+)$",
        "get # sovereigns from pouch",
        lambda m: eqbal(f"get {m[0]} sovereigns from pack")
    ),
]
c.add_aliases("basic", basic_aliases)

def random_move():
    exits = list(s.room["exits"].keys())
    exit = random.choice(exits)
    move(exit)

def move(direction):
    remember_path = getattr(s, "remember_path", False)
    if remember_path:
        s.path_to_remember.append(direction)
    send(f"queue prepend eqbal {direction}")

def handle_says(gmcp_data):
    #print(f"Comm.Channel.Text: {gmcp_data}")
    logger.says(gmcp_data['text'])
c.add_gmcp_handler("Comm.Channel.Text", handle_says)

direction_aliases = [
    (   "^n$",
        "n",
        lambda _: move("n"),
    ),
    (   "^ne$",
        "ne",
        lambda _: move("ne"),
    ),
    (   "^e$",
        "e",
        lambda _: move("e"),
    ),
    (   "^se$",
        "se",
        lambda _: move("se"),
    ),
    (   "^s$",
        "s",
        lambda _: move("s"),
    ),
    (   "^sw$",
        "sw",
        lambda _: move("sw"),
    ),
    (   "^sw$",
        "sw",
        lambda _: move("sw"),
    ),
    (   "^w$",
        "w",
        lambda _: move("w"),
    ),
    (   "^nw$",
        "nw",
        lambda _: move("nw"),
    ),
    (   "^u$",
        "u",
        lambda _: move("u"),
    ),
    (   "^d$",
        "d",
        lambda _: move("d"),
    ),
    (   "^in$",
        "in",
        lambda _: move("in"),
    ),
    (   "^out$",
        "out",
        lambda _: move("out"),
    ),
    (   "^sout$",
        "simple out",
        lambda _: send("out"),
    ),
    (   "^rdir$",
        "rdir",
        lambda _: random_move(),
    ),
]
c.add_aliases("moving", direction_aliases)
