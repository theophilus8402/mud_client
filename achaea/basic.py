
import re

from colorama import *

from enum import Enum
from collections import deque
from queue import Queue, Empty

from .client import client, send, add_aliases, add_triggers, remove_trigger, delete_line, echo, add_temp_trigger, remove_temp_trigger, add_gmcp_handler
from .variables import v

class QueueStates(Enum):
    nothing_queued = 0
    attempting_queue = 1
    command_queued = 2

v.eqbal_queue_state = QueueStates.nothing_queued
v.eqbal_queue = deque()

def eqbal(msg):

    #echo("Adding to internal queue: {}".format(msg))
    v.eqbal_queue.append(msg)

    if v.eqbal_queue_state == QueueStates.nothing_queued:
        msg = v.eqbal_queue.popleft()
        send("queue add eqbal {}".format(msg))
        v.eqbal_queue_state = QueueStates.attempting_queue

    # to do a better queueing system than achaea...
    # (achaea tries to run everything in the queue all at once... ignoring balance)
    # I need to keep a queue
    # three states:
    #   nothing queued
    #       if in this state, check my queue for commands to send or wait for one
    #       ... move to v ... when I send a command to eqbal
    #   attempting to queue
    #       if in this state, any commands to eqbal go into my queue
    #       ... move to v .... when I get the message showing the command has been queued
    #   command queued
    #       if in this state, any commands go into my queue
    #       ... move to v ... when I get the message stating the command has been run
    #   nothing queued


def adding_eqbal_trig(matches):
    #echo("Adding: {}".format(matches[0]))
    v.eqbal_queue_state = QueueStates.command_queued
    delete_line()


def running_eqbal_trig(matches):
    #echo("Running: {}".format(matches[0]))
    echo("Queue: {}".format(v.eqbal_queue))
    v.eqbal_queue_state = QueueStates.nothing_queued
    try:
        msg = v.eqbal_queue.popleft()
        send("queue add eqbal {}".format(msg))
    except IndexError:
        pass
    delete_line()


queue_triggers = [
    (   "\[System\]: Added (.*) to your eqbal queue.",
        # catch lines for system eqbal
        adding_eqbal_trig
    ),
    (   "^\[System\]: Running queued eqbal command: (.*)$",
        # catch lines for system eqbal
        running_eqbal_trig
    )
]
add_triggers(queue_triggers)

def curebal(cure):
    send("curing queue add {}".format(cure))

def eat_herb(herb, mud=None, matches=None):
    send("outr {herb}\neat {herb}".format(herb=herb))

def highlight_current_line(color, pattern=".*", flags=0):

    # this will highlight whatever matched the above pattern
    # it screws up any color/style that was before our highlight :(
    def replacer(match):
        return color + match.group() + Style.RESET_ALL

    line = re.sub(pattern, replacer, client.current_line, flags=flags)
    client.modified_current_line = line

def target(matches):
    # remove the previous target trigger
    remove_temp_trigger("target_trigger")

    # set the target
    v.target = matches[0]

    # set the target trigger
    target_trigger = (
            v.target,
            lambda m: highlight_current_line(Fore.RED, pattern=v.target, flags=re.I)
        )
    add_temp_trigger("target_trigger", target_trigger, flags=re.IGNORECASE)

    echo("now targeting: {}".format(v.target))


basic_aliases = [
    (   "^t (.*)$",
        "target",
        target
    ),
    (   "^gg$",
        "get gold",
        lambda m: eqbal("get gold")
    ),
    (   "^pg$",
        "put gold in pack",
        lambda m: eqbal("put gold in pack")
    ),
    (   "^gp (\d+)$",
        "get # gold from pack",
        lambda m: eqbal("get {} gold from pack".format(m[0]))
    ),
]
add_aliases("basic", basic_aliases)

def random_move():
    exits = list(v.room["exits"].keys())
    exit = random.choice(exits)
    move(exit)

def move(direction):
    remember_path = getattr(v, "remember_path", False)
    if remember_path:
        v.path_to_remember.append(direction)
    send("queue prepend eqbal {}".format(direction))

def handle_says(gmcp_data):
    #with open(
    # TODO write stuff!
    print("<{}>".format(gmcp_data["text"]))
    #pass
add_gmcp_handler("Comm.Channel.Text", handle_says)

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
    (   "^rdir$",
        "rdir",
        lambda _: random_move(),
    ),
]
add_aliases("moving", direction_aliases)


