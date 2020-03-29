
from ..client import c, send, echo

"""
cure timeloop more
You have been afflicted with timeloop.
bellwort

Naoko says in a poised, euphonious voice, "You can CURING PRIORITY TIMELOOP 1 (or 2) in order to guard versus it. Or, use CURING PRIOAFF TIMELOOP whenever you feel pressured by timeloop. Which is generally as soon as you get it."

# growing old let's the depthswalker do this:
Naoko says in a poised, euphonious voice, "It could mean I healed myself, I healed my afflictions, I distorted time around you to stop you from moving, I distorted time around me to make it so I am always where you are, and it could also mean I've powered up my scythe."


A grey distortion coalesces about the blade of a scythe of shadows, held by Naoko.
Naoko delivers a lightning-fast strike to you with a scythe of shadows.
As the weapon strikes you, it burns with a sickly yellow light.
You have been afflicted with hypochondria.
A terrible sense of unease comes over you.
You have been afflicted with timeloop.
The world seems to grow distorted around you, as if through a thick fog.


Char.Afflictions.Add { "name": "sleeping", "cure": "", "desc": "While asleep, you can do little but dream, and wake up." }
You have been afflicted with prone.
Char.Afflictions.Add { "name": "prone", "cure": "STAND", "desc": "Being knocked prone can cause a lot of your options to be limited." }

Char.Afflictions.Remove [ "prone" ]


Readying an insubstantial dagger, Grouulthuun begins to prowl towards Cassari.

Grouulthuun lowers his dagger, a frown of irritation evident upon his face.
Readying an insubstantial dagger, Grouulthuun begins to prowl towards you.

As an insubstantial dagger begins to pulse with a sinister glow, Grouulthuun
begins to close in on you.

Grouulthuun strikes out with incredible speed, the blade of an insubstantial
dagger hissing scant inches from your face. For a moment you feel nothing, then
a soul-rending agony pervades every fibre of your being, and your body collapses
bonelessly to the ground.
You have been afflicted with prone.

it stuns, drops to 1 hp, prones


As you leave the location, you find yourself back where you started.
is this chrono distort?


"""

depthswalker_triggers = [
    (   r"^You have been afflicted with timeloop.$",
        # timeloop is bad!
        lambda m: echo("Eek! Timeloop!")
    ),
]
c.add_triggers(depthswalker_triggers)
