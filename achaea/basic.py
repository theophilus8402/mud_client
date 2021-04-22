import re

from colorama import Fore, Style

from client import c, echo, send
from achaea.state import QueueStates, s


# this will get gmcp info about which player just authenticated
# it can be used to do a number of different things
# starting out, we'll use it to load different modules for different chars
def handle_login_info(gmcp_data):
    name = gmcp_data["name"]

    if name.lower() == "vindiconis":
        echo("Loading modules for vindiconis!")
        # magi modules
        from achaea.magi import (
            ab_artificing,
            ab_crystalism,
            ab_elementalism,
            affliction_tracker,
            fancy_attacks,
            limb_counter,
        )

    elif name.lower() == "palleo":
        echo("Loading modules for palleo!")
        # cleric modules
        from achaea.cleric import ab_devotion, ab_spirituality, ab_zeal

    elif name.lower() == "dirus":
        echo("Loading modules for dirus!")
        # occultist modules
        from achaea.occultist import ab_domination, ab_occultism, ab_tarot

    elif name.lower() == "sylvus":
        echo("Loading modules for sylvus!")
        # runewarden modules
        from achaea.runewarden import (
            ab_battlerage,
            ab_chivalry,
            ab_runelore,
            ab_weaponmastery,
        )

    elif name.lower() == "sarmenti":
        echo("Loading modules for sarmenti!")
        # jester modules
        from achaea.jester import (
            jester_battlerage,
            ab_pranks,
            ab_puppetry,
            ab_tarot,
            jester_actions,
            misc,
            run_away,
            throw_dagger,
        )

    elif name.lower() == "veredus":
        echo("Loading modules for veredus!")
        # monk modules
        from achaea.monk import (
            ab_kaido,
            ab_tekura,
            ab_telepathy,
            monk_battlerage,
            monk_misc,
            monk_moves,
        )

    """
    elif name.lower() == "sylvus":
        echo("Loading modules for sylvus!")
        from achaea import serpent
    """
c.add_gmcp_handler("Char.Name", handle_login_info)


def show_help(alias_group):
    lines = [
        f"{pattern:15.15} : {desc}"
        for pattern, desc in c.help_info.get(alias_group, [])
    ]
    help_lines = "\n".join(lines)
    return echo(f"{alias_group}:\n{help_lines}")


base_aliases = [
    ("#help (.*)", "show help", lambda m: show_help(m[0])),
]
c.add_aliases("base", base_aliases)


def eqbal(msg, prepend=False):

    # TODO: is this even necessary any more?
    s.eqbal_queue.append(msg)

    for msg in s.eqbal_queue:
        if prepend:
            send(f"queue prepend eqbal {msg}")
        else:
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
    (
        r"^\[System\]: Added (.*) to your eqbal queue.",
        # catch lines for system eqbal
        adding_eqbal_trig,
    ),
    (
        r"(.*) was added to your equilibrium queue.$",
        # catch lines for system eqbal
        readding_eqbal_trig,
    ),
    (
        r"^\[System\]: Running queued equilibrium command: (.*)",
        # catch lines for system eqbal
        running_equilib_trig,
    ),
    (
        r"^You must regain equilibrium first.$",
        # catch lines for system eqbal
        no_eq_bal_trig,
    ),
    (
        r"^\[System\]: Running queued eqbal command: (.*)$",
        # catch lines for system eqbal
        running_eqbal_trig,
    ),
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


basic_aliases = [
    (
        "^gg$",
        "get sovereigns",
        lambda m: eqbal(
            "get sovereigns;put sovereigns in kitbag;put sovereigns in pack"
        ),
    ),
    (
        "^pg$",
        "put sovereigns in pouch",
        lambda m: eqbal("put sovereigns in kitbag;put sovereigns in pack"),
    ),
    (
        r"^gp (\d+)$",
        "get # sovereigns from pouch",
        lambda m: eqbal(f"get {m[0]} sovereigns from pack; get {m[0]} sovereigns from kitbag"),
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


direction_aliases = [
    (
        "^n$",
        "n",
        lambda _: move("n"),
    ),
    (
        "^ne$",
        "ne",
        lambda _: move("ne"),
    ),
    (
        "^e$",
        "e",
        lambda _: move("e"),
    ),
    (
        "^se$",
        "se",
        lambda _: move("se"),
    ),
    (
        "^s$",
        "s",
        lambda _: move("s"),
    ),
    (
        "^sw$",
        "sw",
        lambda _: move("sw"),
    ),
    (
        "^sw$",
        "sw",
        lambda _: move("sw"),
    ),
    (
        "^w$",
        "w",
        lambda _: move("w"),
    ),
    (
        "^nw$",
        "nw",
        lambda _: move("nw"),
    ),
    (
        "^u$",
        "u",
        lambda _: move("u"),
    ),
    (
        "^d$",
        "d",
        lambda _: move("d"),
    ),
    (
        "^in$",
        "in",
        lambda _: move("in"),
    ),
    #(
    #    "^out$",
    #    "out",
    #    lambda _: move("out"),
    #),
    (
        "^sout$",
        "simple out",
        lambda _: send("out"),
    ),
    (
        "^rdir$",
        "rdir",
        lambda _: random_move(),
    ),
]
c.add_aliases("moving", direction_aliases)
