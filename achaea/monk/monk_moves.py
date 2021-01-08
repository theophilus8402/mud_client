import re
from pprint import pformat, pprint

from achaea.state import s
from client import c, echo, send
from telnet_manager import strip_ansi

attack_map = {
    "snapkick": "SNK",
    "sidekick": "SDK",
    "moonkick": "MNK",
    "axekick": "AXK",
    "whirlwindkick": "WWK",
    "sweepkick": "SWK",
    "jumpkick": "JPK",
    "hammerfist": "HFP",
    "uppercut": "UPC",
    "spearhand": "SPP",
    "hook": "HKP",
    "palmstrike": "PMP",
    "jab_parry": "JBPP",
    "jab_hearing": "JBPH",
    "bbt": "BBT",
}

leg_attacks = [
    ("^You let fly at (.*) with a snap kick.$", "snapkick", 2),
    ("^You pump out at (.*) with a powerful side kick.$", "sidekick", 2),
    (
        "^You hurl yourself towards (.*) with a lightning-fast moon kick.$",
        "moonkick",
        2,
    ),
    ("^You kick your leg high and scythe downwards at (.*).$", "axekick", 2),
    (
        "^You spin into the air and throw a whirlwind kick towards (.*).",
        "whirlwindkick",
        2,
    ),
    ("^You drop to the floor and sweep your legs round at (.*).$", "sweepkick", 0),
    (
        "^Your foot slams into (.*), knocking (him|her) off (his|her) feet.$",
        "jumpkick",
        0,
    ),
]

hand_attacks = [
    ("^You ball up one fist and hammerfist (.*).$", "hammerfist", 1),
    ("^You launch a powerful uppercut at (.*).$", "uppercut", 1),
    ("^You form a spear hand and stab out towards (.*).$", "spearhand", 1),
    ("^You unleash a powerful hook towards (.*).$", "hook", 1),
    (
        "^You throw your force behind a forward palmstrike at (.*)'s face.$",
        "palmstrike",
        0,
    ),
    (
        "^With deadly precision, you quickly jab the nerve cluster in the left shoulder of (.*).$",
        "jab_parry",
        0,
    ),
    (
        "^You expertly jab your fingers into the nerve cluster behind the ear of (.*).",
        "jab_hearing",
        0,
    ),
    ("^You move in towards (.*) for the backbreaker.", "bbt", 0),
]
combo_attacks = [*leg_attacks, *hand_attacks]
re_combo_attacks = [
    (re.compile(att), att_type, dmg) for att, att_type, dmg in combo_attacks
]

connects = [
    ("^You connect to the (.*)!$", "hit"),
    ("^You connect!$", "hit"),
    (
        "^You knock the legs out from under (.*) and send (him|her) sprawling.$",
        "proned",
    ),
    ("^You lift (.*) triumphantly into the air, then yank (him|her) down", "bbt'd"),
    ("^The palmstrike smashes into the temple of (.*).$", "pmp_impatience"),
    ("^Your palm smashes into the bridge of (.*)'s nose.$", "pmp_stupid"),
]
re_connects = [
    (re.compile(connect), connect_type) for connect, connect_type in connects
]

misses = [
    ("^(.*) dodges nimbly out of the way.$", "miss"),
    ("^(.*) twists (his|her) body out of harm's way.$", "miss"),
    ("^(.*) quickly jumps back, avoiding the attack.$", "miss"),
    ("^(.*) parries the attack with a deft manoeuvre.$", "PARRY"),
    ("^(.*) moves into your attack, knocking your blow aside before", "GUARD"),
]
re_misses = [(re.compile(miss), miss_type) for miss, miss_type in misses]


def echo_combo(combo):
    combo_strings = []
    for action in combo:
        att = attack_map[action.get("attack")]
        limb = action.get("limb", "")
        connect = action.get("connect")
        att_str = f"{att} {limb} ({connect})"
        combo_strings.append(att_str)
    echo(f"{combo[0]['target']}: {' '.join(combo_strings)}")


# initialize it first
s.processed_tekura_combo = False


def clear_processed_tekura_combo():
    s.processed_tekura_combo = False


c.add_after_current_chunk_process(clear_processed_tekura_combo)


def process_tekura_actions(matches):

    if s.processed_tekura_combo is True:
        return

    s.processed_tekura_combo = True
    combo = []
    lines_to_gag = []

    for line in c.current_chunk.split("\r\n"):

        line = strip_ansi(line)

        # attacks
        found_attack = False
        for re_attack, attack_type, dmg in re_combo_attacks:
            match = re_attack.match(line)
            if match:
                attack_info = {"attack": attack_type, "target": match.groups()[0]}
                attack_info["dmg"] = dmg
                combo.append(attack_info)
                found_attack = True
                break
        if found_attack:
            lines_to_gag.append(line)
            continue

        # connect
        found_connect = False
        for re_conn, connect_type in re_connects:
            match = re_conn.match(line)
            if match:
                last_action = combo[-1]
                if "connect" not in last_action:
                    last_action["connect"] = connect_type
                    limb = match.groups()
                    if limb:
                        limb = limb[0]
                    else:
                        limb = ""
                    last_action["limb"] = limb
                found_connect = True
        if found_connect:
            lines_to_gag.append(line)
            continue

        # miss
        for re_miss, miss_type in re_misses:
            match = re_miss.match(line)
            if match:
                last_action = combo[-1]
                if "connect" not in last_action:
                    last_action["connect"] = miss_type
                    lines_to_gag.append(line)
                continue

    # echo(lines_to_gag)
    c.delete_lines(lines_to_gag)
    echo_combo(combo)
    # echo(pformat(combo))


tekura_triggers = [
    (att, process_tekura_actions) for att, att_type, dmg in combo_attacks
]
c.add_triggers(tekura_triggers)
