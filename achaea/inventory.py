from achaea.basic import eqbal
from client import c

left_hand = ("", "")
right_hand = ("", "")


def wield(hand_name, item_name):
    eqbal(f"wield {hand_name} {item_name}")


def wielding(hand, item_name, long_name):
    if hand == "left":
        global left_hand
        left_hand = (item_name, long_name)
        c.echo(f"{hand} now wielding: {left_hand}")
    elif hand == "right":
        global right_hand
        right_hand = (item_name, long_name)
        c.echo(f"{hand} now wielding: {right_hand}")
    else:
        c.echo(f"Which hand is this? {hand}")


wielding_triggers = [
    (
        r"^(\w+\d+): (.*) in your left hand.$",
        # getting what's being wielded
        lambda m: wielding("left", m[0], m[1]),
    ),
    (
        r"^(\w+\d+): (.*) in your right hand.$",
        # getting what's being wielded
        lambda m: wielding("right", m[0], m[1]),
    ),
    (
        r"^(Left|Right) hand:\s+(\w+\d+)\s+(\w.*)$",
        # getting what's being wielded
        lambda m: wielding(m[0].lower(), m[1], m[2]),
    ),
    # You cease wielding a puppet roughly resembling Lynair in your left hand.
    # You begin to wield a small blackjack in your left hand.
]
c.add_triggers(wielding_triggers)


inventory_aliases = [
    # (   "^i$",
    #    "get inventory from achaea",
    #    lambda m: c.gmcp_send("Char.Items.Inv \"\"")
    # ),
    ("^wl (.*)$", "wield left item", lambda m: wield("left", m[0])),
    ("^wr (.*)$", "wield right item", lambda m: wield("right", m[0])),
]
c.add_aliases("inventory", inventory_aliases)
