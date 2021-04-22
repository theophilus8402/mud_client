from client import c, send

from achaea.basic import eqbal

#Syntax:            TIE CHEESE TO ROPE
#                   FISH FOR MICE
#                   REEL IN MOUSE
#                   EDUCATE MOUSE
#                   STRAP <bomb> TO <mouse>
#                   ORDER MOUSE KILL <target>
#                   CALL MICE
#Extra Information: Educate cooldown: 5.00 seconds of balance
#                   Strap cooldown: 4.00 seconds of balance
#
#Works on/against:  Adventurers
#Cooldown:          Balance
#Details:
#Brainwash mice until they are willing to sacrifice their lives for you. First, get a rope and cheese, and then tie the rope to the cheese. Then, you have to fish for the mice in a city area. Reel the mouse in when one bites. Once you've caught one, you may educate him, which will prepare the mouse for use. Just strap a bomb onto his back, drop him, and ORDER MOUSE KILL <whoever>. If you are within approximately 10 rooms of your target, the mouse will immediately take off chasing your unlucky victim, and, upon finding the person, detonate the bomb.
#
#(OOC Note: These predated any of the recent, very regrettable terrorist acts, and are not intended to make light of them in any way.)


BOMB_HELP = """
BOMB INFO
con concussion - stuns, 1 iron
but butterfly - knock out of trees/sky, 1 iron
smo smoke - makes hungry, 1 iron
web web - web, 1 rope
dus dust - "knockout"?, 1 diamond dust
"""


def make_bomb(bomb_type=""):

    if bomb_type == "":
        c.echo(BOMB_HELP)
    elif "concussion".startswith(bomb_type.lower()):
        eqbal(f"stand;outr 1 iron;construct concussion bomb")
    elif "butterfly".startswith(bomb_type.lower()):
        eqbal(f"stand;outr 1 iron;construct butterfly bomb")
    elif "smoke".startswith(bomb_type.lower()):
        eqbal(f"stand;outr 1 iron;construct smoke bomb")
    elif "web".startswith(bomb_type.lower()):
        eqbal(f"stand;outr 1 rope;construct web bomb")
    elif "dust".startswith(bomb_type.lower()):
        eqbal(f"stand;outr 1 diamonddust;construct dust bomb")


THROW_BOMB_HELP = """
THROW BOMB HELP
b   - THROW_BOMB_HELP
bc  - throw concussionbomb dir/at ground
bb  - throw butterflybomb dir/at ground
bs  - throw smokebomb dir/at ground
bw  - throw webbomb dir/at ground
bd  - throw dustbomb dir/at ground
"""
bomb_aliases = [
    (
        "^b$",
        "throw bombs!",
        lambda matches: throw_bomb("", "")
    ),
    (
        "^bc(?: (.*))?$",
        "throw bombs!",
        lambda matches: throw_bomb("concussion", matches[0] or ""),
    ),
    (
        "^bb(?: (.*))?$",
        "throw bombs!",
        lambda matches: throw_bomb("butterfly", matches[0] or ""),
    ),
    (
        "^bs(?: (.*))?$",
        "throw bombs!",
        lambda matches: throw_bomb("smoke", matches[0] or ""),
    ),
    (
        "^bw(?: (.*))?$",
        "throw bombs!",
        lambda matches: throw_bomb("web", matches[0] or ""),
    ),
    (
        "^bd(?: (.*))?$",
        "throw bombs!",
        lambda matches: throw_bomb("dust", matches[0] or ""),
    ),
    (
        "^mb(?: (.+))?$",
        "make bombs!",
        lambda matches: make_bomb(matches[0] or "")
    ),
]
c.add_aliases("bombs", bomb_aliases)


def _throw_bomb(bomb_type, direction=""):
    return f"stand;unwield left;wield {bomb_type} left;throw {bomb_type} {direction}"


def throw_bomb(bomb_type, direction):

    if direction == "":
        direction = "at ground"

    c.echo(f"throw_bomb type: {bomb_type} dir: {direction}")

    if bomb_type == "":
        c.echo(THROW_BOMB_HELP)
    elif bomb_type.startswith("c"):
        eqbal(_throw_bomb("concussionbomb", direction))
    elif bomb_type.startswith("b"):
        eqbal(_throw_bomb("butterflybomb", direction))
    elif bomb_type.startswith("s"):
        eqbal(_throw_bomb("smokebomb", direction))
    elif bomb_type.startswith("w"):
        eqbal(_throw_bomb("webbomb", direction))
    elif bomb_type.startswith("d"):
        eqbal(_throw_bomb("dustbomb", direction))
    else:
        c.echo(f"HMMMMM???? throw_bomb type: {bomb_type} dir: {direction}")


bomb_triggers = [
    (
        "^The mouse sees the cheese and cautiously approaches it, taking a little nibble at first, but increasingly taking larger bites.$",
        # get that mouse!
        lambda m: send("reel in mouse;educate mouse"),
    ),
]
c.add_triggers(bomb_triggers)
