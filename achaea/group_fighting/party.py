from colorama import Fore

from client import c, echo, send

#pan config
#pan target on/off
#pan mindlock on/off
#pan assessments on/off

_party_announce = {
}

def register_announce_type(announce_type):
    global _party_announce
    _party_announce[announce_type] = "off"


def handle_pan_config(line):
    pieces = line.split(" ")
    cmd = pieces[0]
    echo(f"cmd: {cmd}")
    global _party_announce

    if cmd == "config":
        echo("Party Announce Config:")
        for key, value in _party_announce.items():
            echo(f"{key}: {value}")
        return

    if len(pieces) != 2:
        echo(f"incorrect config: {line}")

    status = pieces[1]

    if cmd in _party_announce.keys() and status in {"on", "off"}:
        echo(f"setting {cmd} = {status}")
        _party_announce[cmd] = status
    else:
        echo(f"incorrect config: {line}")
        echo("pan config status should be on/off")


def party_announce(msg, pan_type):
    global _party_announce
    if _party_announce[pan_type] == "on":
        send(f"pt {msg}")


party_aliases = [
    ("^pan (.*)$", "party announcment config", lambda m: handle_pan_config(m[0])),
]
c.add_aliases("party", party_aliases)


# (Party): Nephiny says, "Target: Axios."
