
import json
import time

from .client import c, send, echo
from .state import s

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
        return

    aff_strs = []
    for aff in s.current_afflictions:
        if aff in s.new_afflictions:
            aff_strs.append(f"+{aff}")
        else:
            aff_strs.append(aff)
    for aff in s.cured_afflictions:
        aff_strs.append(f"-{aff}")
    echo(f"Affs: {' '.join(aff_strs)}")

    s.new_afflictions.clear()
    s.cured_afflictions.clear()


def gained_aff(gmcp_data):
    new_aff = gmcp_data['name']
    echo(f"Gained {new_aff}!")
    s.new_afflictions.add(new_aff)
    s.current_afflictions.add(new_aff)
c.add_gmcp_handler("Char.Afflictions.Add", gained_aff)


def cured_aff(gmcp_data):
    cured_affs = set(gmcp_data)
    echo(f"Cured {', '.join(cured_affs)}!")
    s.cured_afflictions.update(cured_affs)
    s.current_afflictions.difference_update(set(cured_affs))
c.add_gmcp_handler("Char.Afflictions.Remove", cured_aff)


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

    affliction_details_json = "achaea/affliction_details.json"
    with open(affliction_details_json, "w") as f:
        json.dump(affs, f, indent=2)
parse_affliction_details()
