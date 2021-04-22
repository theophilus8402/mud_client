from achaea.fighting_log import fighting
from client import c, echo, send

#"""
#cure timeloop more
#You have been afflicted with timeloop.
#bellwort
#
#Naoko says in a poised, euphonious voice, "You can CURING PRIORITY TIMELOOP 1 (or 2) in order to guard versus it. Or, use CURING PRIOAFF TIMELOOP whenever you feel pressured by timeloop. Which is generally as soon as you get it."
#
## growing old let's the depthswalker do this:
#Naoko says in a poised, euphonious voice, "It could mean I healed myself, I healed my afflictions, I distorted time around you to stop you from moving, I distorted time around me to make it so I am always where you are, and it could also mean I've powered up my scythe."
#
#
#A grey distortion coalesces about the blade of a scythe of shadows, held by Naoko.
#Naoko delivers a lightning-fast strike to you with a scythe of shadows.
#As the weapon strikes you, it burns with a sickly yellow light.
#You have been afflicted with hypochondria.
#A terrible sense of unease comes over you.
#You have been afflicted with timeloop.
#The world seems to grow distorted around you, as if through a thick fog.
#
#
#Char.Afflictions.Add { "name": "sleeping", "cure": "", "desc": "While asleep, you can do little but dream, and wake up." }
#You have been afflicted with prone.
#Char.Afflictions.Add { "name": "prone", "cure": "STAND", "desc": "Being knocked prone can cause a lot of your options to be limited." }
#
#Char.Afflictions.Remove [ "prone" ]
#
#
#Readying an insubstantial dagger, Grouulthuun begins to prowl towards Cassari.
#
#Grouulthuun lowers his dagger, a frown of irritation evident upon his face.
#Readying an insubstantial dagger, Grouulthuun begins to prowl towards you.
#
#As an insubstantial dagger begins to pulse with a sinister glow, Grouulthuun
#begins to close in on you.
#
#Grouulthuun strikes out with incredible speed, the blade of an insubstantial
#dagger hissing scant inches from your face. For a moment you feel nothing, then
#a soul-rending agony pervades every fibre of your being, and your body collapses
#bonelessly to the ground.
#You have been afflicted with prone.
#
#it stuns, drops to 1 hp, prones
#
#
#As you leave the location, you find yourself back where you started.
#is this chrono distort?
#
#
#
#
#You say, "Oh?"
#Naoko says in a poised, euphonious voice, "How you died just now. Your shadow snapped your neck."
#You say, "I'm not good at seeing much of anything."
#You say, "That wasn't very nice."
#You say, "How do I stop that?"
#Grouulthuun says in a deep and guttural voice, "Keep your mana up."
#Grouulthuun says in a deep and guttural voice, "Erm.."
#Grouulthuun says in a deep and guttural voice, "Don't lose your shadow."
#Naoko says in a poised, euphonious voice, "Don't let your shadow get a crush on the flesh-ripping siren."
#Naoko says in a poised, euphonious voice, "If your mana is below 40%, I can command it to kill you without delay."
#Naoko says in a poised, euphonious voice, "This is increased to 50% using depression and madness."
#Naoko says in a poised, euphonious voice, "60% if you have depression, madness, retribution, and parasite."
#You say, "Ah, well, I was basically dead anyways... Everything was in super bad condition."
#Grouulthuun says in a deep and guttural voice, "Depression and madness are like progressive venoms."
#You say, "Ouch! That's crazy!"
#You say, "Other than shielding all the time, how do I not get so worked over by afflictions?"
#Naoko says in a poised, euphonious voice, "Hinder me. You have 8 seconds to do so before I pop off."
#Naoko says in a poised, euphonious voice, "If you can use your first 8 seconds to hinder me, then you have a chance. If you cannot, run."
#You say, "I don't think I have a really good way to do that, do I? I know limb breaks, but I don't get a level 2 break until I've attacked seven times."
#You say, "What's the 8 second mark that I'm watching out for?"
#Naoko says in a poised, euphonious voice, "Hypochondria."
#Naoko says in a poised, euphonious voice, "And do note that your golem can smash my limbs while you strike with earth."
#You say, "I was doing that the whole two or three times I got to attack before I died a horrible death."
#Naoko says in a poised, euphonious voice, "Use timeflux to your advantage to make those level 1 breaks into a strong hinder."
#You say, "Should I have it break arms instead of legs?"
#Naoko says in a poised, euphonious voice, "Always."
#You say, "Aye, I always forget timeflux."
#Naoko says in a poised, euphonious voice, "Almost always anyway."
#Naoko says in a poised, euphonious voice, "If you don't timeflux, you can't win."
#You say, "I'll work on it."
#Naoko says in a poised, euphonious voice, "Especially if you have lethargy at any point during your kill sequence, I will not let you kill me."
#Naoko says in a poised, euphonious voice, "And I have something that is the bane of all magi."
#You say, "Which is?"
#Naoko says in a poised, euphonious voice, "I can use my cure while prone."
#Grouulthuun says in a deep and guttural voice, "Mhmm."
#You say, "What cure?"
#Grouulthuun says in a deep and guttural voice, "It's called Acceleration."
#Grouulthuun says in a deep and guttural voice, "Like a serpents shrug."
#Grouulthuun says in a deep and guttural voice, "It's our class heal."
#Naoko says in a poised, euphonious voice, "Basically, I have more ways to thaw myself than others."
#You say, "From where does the hypochondria come? That Attune attack or something else?"
#Naoko says in a poised, euphonious voice, "My scythe."
#You say, "Do I need to run away from you after you attune or just try to stick through it?"
#Naoko says in a poised, euphonious voice, "That would be unwise, because I attune balancelessly."
#Grouulthuun says in a deep and guttural voice, "Hard to run from a Depthswalker. Can chase pretty well."
#Grouulthuun says in a deep and guttural voice, "That too."
#Naoko says in a poised, euphonious voice, "Here's the idea behind that kill."
#Naoko says in a poised, euphonious voice, "Depression deals mana and health damage every time you suffer from a mental affliction."
#You say, "Ouch!"
#Naoko says in a poised, euphonious voice, "I give you attune, madness, and hypochondria as three passive sources of affliction, and timeloop which doubles the amount of afflictions I can give."
#You say, "That's what did all that damage to me."
#Naoko says in a poised, euphonious voice, "You also have nausea and masochism hurting you."
#Naoko says in a poised, euphonious voice, "The idea is not to let me properly establish my source of passive affliction income."
#Naoko says in a poised, euphonious voice, "My momentum isn't amazing until that point."
#You say, "Sounds... easy..."
#
#
#"""


def littany(matches):
    fighting(f"Eek! {matches[0]} is !")
    echo(f"Eek! {matches[0]} is !")
    send("writhe;writhe;writhe;sit")


depthswalker_triggers = [
    (
        r"^You have been afflicted with timeloop.$",
        # timeloop is bad!
        lambda m: echo("Eek! Timeloop!"),
    ),
    (
        r"^The ominously haunting sound of (.*) suddenly fills your head, threatening to drown out all other sound.$",
        # timeloop is bad!
        lambda m: littany(m),
    ),
]
c.add_triggers(depthswalker_triggers)
