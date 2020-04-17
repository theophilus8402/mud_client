
import json
import logging
import re
import time

from .client import c, send, echo
from .state import s


logger = logging.getLogger("achaea")


aff_aliases = [
    (   "get_all_aff",
        "get_all_aff",
        lambda m: get_all_aff_info()
    ),
]
c.add_aliases("aff", aff_aliases)


def get_all_aff_info():
    all_aff_list_path = "notes/all_afflictions.txt"
    with open(all_aff_list_path) as f:
        for index, aff in enumerate(f):
            send(f"affliction show {aff}")
            if (index % 5) == 0:
                c.send_flush()
                time.sleep(.5)


def summarize_afflictions():

    if not (s.new_afflictions or s.cured_afflictions):
        return []

    aff_strs = []
    for aff in s.current_afflictions:
        if aff in s.new_afflictions:
            aff_strs.append(f"+{aff}")
        else:
            aff_strs.append(aff)
    for aff in s.cured_afflictions:
        aff_strs.append(f"-{aff}")

    s.new_afflictions.clear()
    s.cured_afflictions.clear()

    return aff_strs


def gained_aff(gmcp_data):
    new_aff = gmcp_data['name']
    echo(f"Gained {new_aff}!")
    s.new_afflictions.add(new_aff)
    s.current_afflictions.add(new_aff)
    logger.fighting(f"Affs: {' '.join(summarize_afflictions())}")
c.add_gmcp_handler("Char.Afflictions.Add", gained_aff)


def cured_aff(gmcp_data):
    cured_affs = set(gmcp_data)
    echo(f"Cured {', '.join(cured_affs)}!")
    s.cured_afflictions.update(cured_affs)
    s.current_afflictions.difference_update(set(cured_affs))
    logger.fighting(f"Affs: {' '.join(summarize_afflictions())}")
c.add_gmcp_handler("Char.Afflictions.Remove", cured_aff)


AFFLICTION_DETAILS_JSON = "achaea/affliction_details.json"
def parse_affliction_details():
    affliction_details_path = "notes/affliction_details.txt"
    with open(affliction_details_path) as f:
        aff_details_blob = f.read().rstrip()

    affs = []
    for aff in aff_details_blob.split("\n\n"):
        detail = {}
        #import pdb;pdb.set_trace()
        for line in aff.split("\n"):
            try:
                key, value = line.split(":")
            except ValueError as e:
                print(f"problem: '{line}'")
                print(f"aff: '{aff}'")
            value = value.lstrip()
            detail[key] = value
        affs.append(detail)

    with open(AFFLICTION_DETAILS_JSON, "w") as f:
        json.dump(affs, f, indent=2)
#parse_affliction_details()


def get_cure_msg(affliction):
    return affliction["Cured msg"]


def get_aff_msg(affliction):
    return affliction["Afflicted msg"]


def setup_suppress_afflictions():
    with open(AFFLICTION_DETAILS_JSON, "r") as f:
        aff_details = json.load(f)

    triggers = []
    for aff in aff_details:
        cure_msg = get_cure_msg(aff)
        triggers.append((r"^{}$".format(re.escape(cure_msg)), lambda m: c.delete_line()))

        aff_msg = get_aff_msg(aff)
        triggers.append((r"^{}$".format(re.escape(aff_msg)), lambda m: c.delete_line()))

    c.add_triggers(triggers)
setup_suppress_afflictions()
