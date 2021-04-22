from achaea.basic import eqbal
from achaea.state import s
from client import c, send

weaponmastery_aliases = [
    (
        "^m$",
        "dsl t",
        lambda matches: eqbal(f"stand;combination &tar slice smash")
    ),
    (
        "^tp$",
        "trip t",
        lambda matches: eqbal(f"stand;combination &tar slice trip")
    ),
]
c.add_aliases("ab_weaponmastery", weaponmastery_aliases)

#raze target;smash mid
#impale
#cleave
#
## shield
#smash high/mid/low
#drive
#concuss
#trip
#club (stun)
#*shieldstrike high/mid/low
#disembowel
#
#
#venom
#
#cah
#combination target slice aconite smash high
#cam
#combination target slice aconite smash mid
#cal
#combination target slice aconite smash low
#cad
#combination target slice aconite drive
#cac
#combination target slice aconite concuss
#cat
#combination target slice aconite trip
#cab
#combination target slice aconite club
