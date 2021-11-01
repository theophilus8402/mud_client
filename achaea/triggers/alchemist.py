from client import c, echo, send

alchemist_triggers = [
    (
        r"^You feel a sudden jerk, and the air immediately surrounding you comes",
        # EEK about to be summoned!
        lambda m: echo("Eek! ALCHEMIST DISPLACE!!!\nMOVE!\nMOVE!"),
    ),
    (
        r"^The etheric light around you abruptly fades, and you feel a sudden release of",
        lambda m: echo("Phew! ALCHEMIST DISPLACE is over!!!\nYou can go back in!"),
    ),
]
c.add_triggers(alchemist_triggers)
