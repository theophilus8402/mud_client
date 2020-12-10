import re

from client import c, echo, send

# legs
snap_kick = "^You let fly at (.*) with a snap kick.$"
re_snap_kick = re.compile(snap_kick)
# > You pump out at Belatu with a powerful side kick.
# > You hurl yourself towards Belatu with a lightning-fast moon kick.

# hands
hammerfist = "^You ball up one fist and hammerfist (.*).$"
re_hammerfist = re.compile(hammerfist)
# > You launch a powerful uppercut at Belatu.
# > You form a spear hand and stab out towards Belatu.

# connect/miss
connect = "^You connect to the (.*)!$"
re_connect = re.compile(connect)
dodge_miss = "^(.*) dodges nimbly out of the way.$"
re_dodge_miss = re.compile(dodge_miss)
twist_miss = "^(.*) twists (his|her) body out of harm's way.$"
re_dodge_miss = re.compile(dodge_miss)
avoid_miss = "^(.*) quickly jumps back, avoiding the attack.$"
re_avoid_miss = re.compile(avoid_miss)
parry_miss = "^(.*) parries the attack with a deft manoeuvre.$"
re_parry_miss = re.compile(avoid_miss)
# > You let fly at Ovis with a snap kick.
# > Ovis moves into your attack, knocking your blow aside before viciously

# > [System]: Added COMBO &TAR SDK UCP UCP to your eqbal queue.
# > You pump out at Belatu with a powerful side kick.
# > You launch a powerful uppercut at Belatu.
# > Belatu dodges nimbly out of the way.
# > You launch a powerful uppercut at Belatu.
# > You connect to the head!

# > You pump out at Belatu with a powerful side kick.
# > You launch a powerful uppercut at Belatu.
# > You connect to the head!
# > You launch a powerful uppercut at Belatu.
# > Belatu twists his body out of harm's way.

# > You pump out at Belatu with a powerful side kick.
# > You connect to the torso!
# > You launch a powerful uppercut at Belatu.
# > You connect to the head!
# > You launch a powerful uppercut at Belatu.
# > Belatu quickly jumps back, avoiding the attack.

# > Belatu, riding a stone gargoyle, leaves to the south.
# >
# > You have recovered balance on all limbs.
# > Ahh, I am truly sorry, but I do not see anyone by that name here.
# > Nothing can be seen here by that name.
# > You cannot see that being here.
# > Nothing can be seen here by that name.
# > Ahh, I am truly sorry, but I do not see anyone by that name here.
# > You cannot see that being here.

# > You pump out at Belatu with a powerful side kick.
# > Belatu twists his body out of harm's way.
# > You launch a powerful uppercut at Belatu.
# > Belatu parries the attack with a deft manoeuvre.
# > You launch a powerful uppercut at Belatu.
# > Belatu parries the attack with a deft manoeuvre.

# > [System]: Added COMBO &TAR MNK LEFT SPP LEFT SPP LEFT to your eqbal queue.
# > You hurl yourself towards Belatu with a lightning-fast moon kick.
# > You connect to the right arm!
# > You form a spear hand and stab out towards Belatu.
# > You connect to the right arm!
# > You form a spear hand and stab out towards Belatu.
# > You connect to the left arm!

# > [System]: Added COMBO &TAR SNK LEFT HFP LEFT HFP LEFT to your eqbal queue.
# > You let fly at Ovis with a snap kick.
# > Ovis moves into your attack, knocking your blow aside before viciously
# > countering with a strike to your head.
# > You are too stunned to be able to do anything.
# > You are too stunned to be able to do anything.


def process_tekura_actions(matches):

    info = []

    for line in c.current_chunk.split("\r\n"):
        # print(line)
        pass


tekura_triggers = [
    (
        "^You let fly at (.*) with a snap kick.$",
        # kicked someone!
        process_tekura_actions,
    ),
]
c.add_triggers(tekura_triggers)
