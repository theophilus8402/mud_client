
from ..client import c, send, echo
from ..state import s

"""
Three different numbers
1) type of staffstrike
    8 - earth (head / break things?)
    4 - water (left cold kill path)
    5 - air (low / trip)
    6 - fire (right fire kill path)
2) limb to attack
    8 - head
    4 - left arm
    5 - torso
    6 - right arm
    1 - left leg
    3 - right leg
    7 - nothing
3) golem attack
    7 - hypothermia (left cold path)
    4 - pummel      (left cold path)
    9 - scorch      (right fire path)
    6 - dehydrate   (right fire path)
    8 - flux
    5 - smash arms
    2 - smash legs
    1 - scald
    3 - impurity stupidity
"""

strike_map = {
    8: "staffstrike {target} with earth",
    4: "staffstrike {target} with water",
    5: "staffstrike {target} with air",
    6: "staffstrike {target} with fire",
}


limb_map = {
    8: " head",
    4: " left arm",
    5: " torso",
    6: " right arm",
    1: " left leg",
    3: " right leg",
    7: "",
}


golem_map = {
    7: "golem hypothermia {target}",
    4: "golem pummel {target}",
    9: "golem scorch {target}",
    6: "golem dehydrate {target}",
    8: "golem timeflux {target}",
    5: "golem smash {target} arms",
    2: "golem smash {target} legs",
    1: "golem scald {target}",
    3: "golem impurity {target} stupidity",
}


def parse_number_attack(matches):

    if matches[2] == None:
        strike_type_num = int(matches[0])
        limb_num = 7
        golem_attack_num = int(matches[1])
    else:
        strike_type_num = int(matches[0])
        limb_num = int(matches[1])
        golem_attack_num = int(matches[2])

    if strike_type_num not in strike_map:
        echo("Not a valid strike num!")
        return
    if limb_num not in limb_map:
        echo("Not a valid limb num!")
        return
    if golem_attack_num not in golem_map:
        echo("Not a valid golem num!")
        return

    strike_attack = strike_map[strike_type_num]
    limb = limb_map[limb_num]
    golem_attack = golem_map[golem_attack_num]

    attack = f"stand;{strike_attack}{limb};{golem_attack}".format(target=s.target)
    echo(attack)
    send(attack)


fancy_attack_aliases = [
    (   "^(\d)(\d)(\d)?$",
        "(staffstrike)(limb)(golem)",
        parse_number_attack
    ),
]
c.add_aliases("fancy_attacks", fancy_attack_aliases)
