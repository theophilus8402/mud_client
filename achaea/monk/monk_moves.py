import re

from client import c, echo, send
from telnet_manager import strip_ansi

# legs
snap_kick = "^You let fly at (.*) with a snap kick.$"
re_snap_kick = re.compile(snap_kick)
side_kick = "^You pump out at (.*) with a powerful side kick.$"
re_side_kick = re.compile(side_kick)
moon_kick = "^You hurl yourself towards (.*) with a lightning-fast moon kick.$"
re_moon_kick = re.compile(moon_kick)
axe_kick = "^You kick your leg high and scythe downwards at (.*).$"
re_axe_kick = re.compile(axe_kick)
whirlwind_kick = "^You spin into the air and throw a whirlwind kick towards (.*)."
re_whirlwind_kick = re.compile(whirlwind_kick)
sweep_kick = "^You drop to the floor and sweep your legs round at (.*).$"
re_sweep_kick = re.compile(sweep_kick)
jump_kick = "^Your foot slams into (.*), knocking (him|her) off (his|her) feet.$"
re_jump_kick = re.compile(jump_kick)

# hands
hammerfist = "^You ball up one fist and hammerfist (.*).$"
re_hammerfist = re.compile(hammerfist)
uppercut = "^You launch a powerful uppercut at (.*).$"
re_uppercut = re.compile(uppercut)
spearhand = "^You form a spear hand and stab out towards (.*).$"
re_spearhand = re.compile(spearhand)
hook = "^You unleash a powerful hook towards (.*).$"
re_hook = re.compile(hook)
palmstrike = "^You throw your force behind a forward palmstrike at (.*)'s face.$"
re_palmstrike = re.compile(palmstrike)

# throws
bbt = "^You move in towards (.*) for the backbreaker."
re_bbt = re.compile(bbt)

# connects
connect = "^You connect to the (.*)!$"
re_connect = re.compile(connect)
sweep_connect = "^You knock the legs out from under (.*) and send (him|her) sprawling.$"
re_sweep_connect = re.compile(sweep_connect)
bbt_connect = "^You lift (.*) triumphantly into the air, then yank (him|her) down"
re_bbt_connect = re.compile(bbt_connect)
# The palmstrike smashes into the temple of Mercer.
# Your palm smashes into the bridge of Mercer's nose.

# misses
dodge_miss = "^(.*) dodges nimbly out of the way.$"
re_dodge_miss = re.compile(dodge_miss)
twist_miss = "^(.*) twists (his|her) body out of harm's way.$"
re_twist_miss = re.compile(twist_miss)
avoid_miss = "^(.*) quickly jumps back, avoiding the attack.$"
re_avoid_miss = re.compile(avoid_miss)
parry_miss = "^(.*) parries the attack with a deft manoeuvre.$"
re_parry_miss = re.compile(parry_miss)
hit_guard = "^(.*) moves into your attack, knocking your blow aside before"
re_hit_guard = re.compile(hit_guard)


#######
# todo
#######
# With deadly precision, you quickly jab the nerve cluster in the left shoulder of
# Mercer.
# With deadly precision, you quickly jab the nerve cluster in the left shoulder of
# Mercer.
#
# You have recovered balance on your left arm.
# You have recovered balance on your right arm.
#
# With deadly precision, you quickly jab the nerve cluster in the left shoulder of
# Mercer.
# You expertly jab your fingers into the nerve cluster behind the ear of Mercer.


from pprint import pformat, pprint


def process_tekura_actions(matches):

    if c.processed_tekura_combo is True:
        return

    c.processed_tekura_combo = True
    combo = []

    for line in c.current_chunk.split("\r\n"):

        line = strip_ansi(line)

        #############
        # attacks
        #############
        attacks = [
            # kicks
            (re_axe_kick, "axekick"),
            (re_whirlwind_kick, "whirlwindkick"),
            (re_snap_kick, "snapkick"),
            (re_side_kick, "sidekick"),
            (re_moon_kick, "moonkick"),
            (re_sweep_kick, "sweepkick"),
            (re_jump_kick, "jumpkick"),
            # hand attacks
            (re_hammerfist, "hammerfist"),
            (re_uppercut, "uppercut"),
            (re_spearhand, "spearhand"),
            (re_hook, "hook"),
            (re_palmstrike, "palmstrike"),
            # throws
            (re_bbt, "bbt"),
        ]
        found_attack = False
        for re_attack, attack_type in attacks:
            match = re_attack.match(line)
            if match:
                attack_info = {"attack": attack_type, "target": match.groups()[0]}
                combo.append(attack_info)
                found_attack = True
                break

        if found_attack:
            continue

        #############
        # connect
        #############
        connects = [
            (re_connect, "connect"),
            (re_sweep_connect, "knocked down"),
        ]
        found_connect = False
        for re_conn, connect_type in connects:
            match = re_conn.match(line)
            if match:
                last_action = combo[-1]
                if "connect" not in last_action:
                    last_action["connect"] = True
                    last_action["limb"] = match.groups()[0]
            continue

        # miss
        misses = [
            re_dodge_miss.match(line),
            re_twist_miss.match(line),
            re_avoid_miss.match(line),
        ]
        if any(misses):
            last_action = combo[-1]
            if "connect" not in last_action:
                last_action["connect"] = False
            continue

    echo(pformat(combo))


tekura_triggers = [
    (
        "^You let fly at (.*) with a snap kick.$",
        # kicked someone!
        process_tekura_actions,
    ),
    (
        side_kick,
        process_tekura_actions,
    ),
    (
        moon_kick,
        process_tekura_actions,
    ),
    (
        hammerfist,
        process_tekura_actions,
    ),
    (
        uppercut,
        process_tekura_actions,
    ),
    (
        spearhand,
        process_tekura_actions,
    ),
]
c.add_triggers(tekura_triggers)
