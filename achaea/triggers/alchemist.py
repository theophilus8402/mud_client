from client import c, echo, send

alchemist_triggers = [
    (
        r"^You feel a sudden jerk, and the air immediately surrounding you comes",
        # EEK about to be summoned!
        lambda m: echo("Eek! You're about to be SUMMONED!\nMOVE!\nMOVE!"),
    ),
]
c.add_triggers(alchemist_triggers)
