import re

from colorama import Fore, Style

from achaea.basic import highlight_current_line
from achaea.group_fighting import party_announce, register_announce_type
from achaea.state import s
from client import c, echo, send
from achaea.frenemies import enemies


register_announce_type("target")


def target(target_name):
    # remove the previous target trigger
    c.remove_temp_trigger("target_trigger")

    # set the target
    s.target = target_name
    party_announce(f"Target: {s.target}", "target")

    send(f"SETTARGET {s.target}")

    # set the target trigger
    target_trigger = (
        s.target,
        lambda m: highlight_current_line(Fore.RED, pattern=s.target, flags=re.I),
    )
    c.add_temp_trigger("target_trigger", target_trigger, flags=re.IGNORECASE)


target_aliases = [
    ("^t (.*)$", "target", lambda m: target(m[0])),
]
c.add_aliases("target", target_aliases)


re_party_target = re.compile(r"Target[: ]+(\w+)\.")
def gmcp_party_target(gmcp_data):
    if gmcp_data["channel"] == "party":
        match = re_party_target.search(gmcp_data["text"])
        if match:
            party_target = match.groups()[0]
            if party_target in enemies:
                echo(f"PARTY TARGET: {party_target}")
                target(party_target)
            else:
                echo(f"{party_target} NOT AN ENEMY")
c.add_gmcp_handler("Comm.Channel.Text", gmcp_party_target)
