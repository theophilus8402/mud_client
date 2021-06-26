from client import c, echo, send

# shimmering orb?
# selfishness
# coins/sovereigns instead of gold
# put gold bar in rift?
# re-wear items
# watch out for fingersnapping

# A feeling of generosity spreads throughout you.
# You rub your hands together greedily.


# Profit snaps his fingers in front of you.
# inr all;inr all;inr all;pg
#
# A soft tug upon your apparel grabs at your attention, and in an instant you realise that your inventory is lighter.
#
# As Profit rubs one hand over a petite ceramic urn, the air in front of him warps and changes as a giant spectral owl coalesces.
# Profit easily vaults onto the back of a giant spectral owl.
# Profit hunches his shoulders and lets out a soft hiss.
# Profit gives a sharp whistle to a giant spectral owl, and is carried away in a mad dash.
#
# You suddenly realise that you have been mesmerised!
#
#
# You already are a selfish bastard.
#
# You remove a canvas backpack.
#
# You are now wearing a canvas backpack.
#
# You get 100 gold sovereigns from a canvas backpack.
#
# You put 100 gold sovereigns in a canvas backpack.


def ive_been_snapped(matches):
    echo("EEEP!!!")
    send("inr all;inr all;inr all;put sovereigns in kitbag;put sovereigns in pack;selfishness")


anti_theft_triggers = [
    (
        r"^(\w+) snaps \w+ fingers in front of you.$",
        # eep!
        ive_been_snapped,
    ),
    (
        r"^You remove a tribal leather kitbag.$",
        # rewear it!
        lambda m: send("wear kitbag;put kitbag in kitbag;put sovereigns in kitbag;selfishness"),
    ),
    (
        r"^You remove a canvas backpack.$",
        # rewear it!
        lambda m: send("wear pack;put pack in pack;put coins in pouch;selfishness"),
    ),
    (
        r"^You remove a gour-hide pouch.$",
        # rewear it!
        lambda m: send("wear pouch;put pouch in pouch;put coins in pouch;selfishness"),
    ),
    (
        r"^You remove a suit of Mhaldorian scale mail.$",
        # rewear it!
        lambda m: send(
            "wear scalemail;put scalemail in pack;put coins in pack;selfishness"
        ),
    ),
    (
        r"^You remove a suit of scale mail.$",
        # rewear it!
        lambda m: send(
            "wear scalemail;put scalemail in pack;put coins in pack;selfishness"
        ),
    ),
    (
        r"^You remove a polished suit of Hashani splintmail.$",
        # rewear it!
        lambda m: send(
            "wear splintmail;put splintmail in pack;put coins in pack;selfishness"
        ),
    ),
    (
        r"^You remove a blackened suit of Hashani full plate.$",
        # rewear it!
        lambda m: send(
            "wear fullplate;put fullplate in kitbag;put sovereigns in kitbag;selfishness"
        ),
    ),
    # (   r"^You cease wielding a small blackjack",
    #    # rewear it!
    #    lambda m: send("wield blackjack;selfishness")
    # ),
    # (   r"^You cease wielding a lightweight barbed banded shield",
    #    # rewear it!
    #    lambda m: send("wield shield;put shield in pack;selfishness")
    # ),
    # (   r"^You cease wielding a Mhaldorian banded shield",
    #    # rewear it!
    #    lambda m: send("wield shield;put shield in pack;selfishness")
    # ),
    # (   r"^You remove a simple suit of lightweight field plate.$",
    #    # rewear it!
    #    lambda m: send("wear fieldplate;put fieldplate in pack;put coins in pouch;selfishness")
    # ),
]
c.add_triggers(anti_theft_triggers)
