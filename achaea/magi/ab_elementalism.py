from client import c, echo, send

from ..basic import eqbal
from ..state import s

elementalism_triggers = [
    (
        "^You grow still and begin to silently pray for preservation of your soul while",
        # you're leaving so detach the fist sigil!
        lambda _: eqbal("detach fist from staff"),
    ),
]
c.add_triggers(elementalism_triggers)


def stormhammer(matches):
    echo(matches)
    try:
        if matches is None:
            peeps = s.target
        else:
            peeps = " and ".join([s.target, *matches.split(" ")])
        echo(peeps)
        eqbal(f"stand;cast stormhammer at {peeps}")
    except Exception as e:
        echo(f"stormhammer: {e}")


elementalism_aliases = [
    (
        "^light$",
        "cast light",
        lambda matches: eqbal(f"stand;cast light"),
    ),
    (
        "^gust(?: (.+))?$",
        "cast gust at t [dir]",
        lambda matches: eqbal(f"stand;cast gust at {s.target} {matches[0]}"),
    ),
    (
        "^ref(?: (.+))?$",
        "cast reflection at me/[]",
        lambda matches: eqbal(f"stand;cast reflection at {matches[0] or 'me'}"),
    ),
    (
        "^fl(?: (.+))?$",
        "cast firelash at []/t",
        lambda matches: eqbal(f"stand;cast firelash at {matches[0] or s.target}"),
    ),
    (
        "^ww(?: (.+))?$",
        "cast waterweird at me/[]",
        lambda matches: eqbal(f"stand;cast waterweird at {matches[0] or 'me'}"),
    ),
    (
        "^okill(?: (.+))?$",
        "order waterweird kill t/[]",
        lambda matches: eqbal(f"stand;order waterweird kill {matches[0] or s.target}"),
    ),
    (
        "^opass(?: (.+))?$",
        "order waterweird passive",
        lambda matches: eqbal(f"stand;order waterweird passive"),
    ),
    (
        "^stone$",
        "cast stoneskin",
        lambda matches: eqbal(f"stand;cast stoneskin"),
    ),
    (
        "^fort (.+)?$",
        "fortify []",
        lambda matches: eqbal(f"stand;fortify {matches[0]}"),
    ),
    (
        "^fr$",
        "cast freeze at t",
        lambda matches: eqbal(f"stand;cast freeze at {s.target}"),
    ),
    (
        "^frg$",
        "cast freeze at ground",
        lambda matches: eqbal(f"stand;cast freeze at ground"),
    ),
    (
        "^gey(?: (.+))?$",
        "cast geyser at []/t",
        lambda matches: eqbal(f"stand;cast geyser at {matches[0] or s.target}"),
    ),
    (
        "^scry(?: (.+))?$",
        "cast scry at []/t",
        lambda matches: eqbal(f"stand;cast scry at {matches[0] or s.target}"),
    ),
    (
        "^sand$",
        "cast sandling",
        lambda matches: eqbal(f"stand;cast sandling"),
    ),
    (
        "^bur (.+)$",
        "burrow []",
        lambda matches: eqbal(f"stand;burrow {matches[0]}"),
    ),
    (
        "^charge(?: (.+))?$",
        "cast chargeshield at me/[]",
        lambda matches: eqbal(f"stand;cast chargeshield at {matches[0] or 'me'}"),
    ),
    (
        "^supp?$",
        "cast suppression",
        lambda matches: eqbal(f"stand;cast suppression"),
    ),
    (
        "^bb$",
        "cast bloodboil",
        lambda matches: eqbal(f"stand;cast bloodboil"),
    ),
    (
        "^ring$",
        "cast ring",
        lambda matches: eqbal(f"stand;cast ring"),
    ),
    (
        "^bind (.+)$",
        "bind []",
        lambda matches: eqbal(f"stand;bind {matches[0]}"),
    ),
    (
        "^muff$",
        "cast muffle",
        lambda matches: eqbal(f"stand;cast muffle"),
    ),
    (
        "^lning(?: (.+))?$",
        "cast lightning at []/t",
        lambda matches: eqbal(f"stand;cast lightning at {matches[0] or s.target}"),
    ),
    (
        "^fw (.+)$",
        "cast firewall []",
        lambda matches: eqbal(f"stand;cast firewall {matches[0]}"),
    ),
    (
        "^fog$",
        "cast fog",
        lambda matches: eqbal(f"stand;cast fog"),
    ),
    (
        "^dfr$",
        "cast deepfreeze",
        lambda matches: eqbal(f"stand;cast deepfreeze"),
    ),
    (
        "^hell$",
        "cast hellfumes",
        lambda matches: eqbal(f"stand;cast hellfumes"),
    ),
    (
        "^fly$",
        "cast aerial",
        lambda matches: eqbal(f"stand;cast aerial"),
    ),
    (
        "^flood$",
        "cast flood",
        lambda matches: eqbal(f"stand;cast flood"),
    ),
    (
        "^ill$",
        "cast illusion",
        lambda matches: echo("not doing anything with illusions!"),
    ),
    (
        "^quake$",
        "cast quake",
        lambda matches: eqbal(f"stand;cast quake"),
    ),
    (
        "^iw (.+)$",
        "cast icewall []",
        lambda matches: eqbal(f"stand;cast icewall {matches[0]}"),
    ),
    (
        "^simul$",
        "simultaneity",
        lambda matches: eqbal(f"stand;attach fist to staff;simultaneity"),
    ),
    (
        "^std(?: (.+))?$",
        "staffcast dissolution at []/t",
        lambda matches: eqbal(
            f"stand;staffcast dissolution at {matches[0] or s.target}"
        ),
    ),
    (
        "^stl(?: (.+))?$",
        "staffcast lightning at []/t",
        lambda matches: eqbal(f"stand;staffcast lightning at {matches[0] or s.target}"),
    ),
    (
        "^sts(?: (.+))?$",
        "staffcast scintilla at []/t",
        lambda matches: eqbal(f"stand;staffcast scintilla at {matches[0] or s.target}"),
    ),
    (
        "^sth(?: (.+))?$",
        "staffcast horripilation at []/t",
        lambda matches: eqbal(
            f"stand;staffcast horripilation at {matches[0] or s.target}"
        ),
    ),
    (
        "^m(?: (.+))?$",
        "staffcast dissolution at []/t",
        lambda matches: eqbal(
            f"stand;staffcast dissolution at {matches[0] or s.target}"
        ),
    ),
    (
        "^diamond$",
        "cast diamondskin",
        lambda matches: eqbal(f"stand;cast diamondskin"),
    ),
    (
        "^efr$",
        "cast efreeti",
        lambda matches: eqbal(f"stand;cast efreeti"),
    ),
    (
        "^fix(?: (.+))?$",
        "cast transfix at []/t",
        lambda matches: eqbal(f"stand;cast transfix at {matches[0] or s.target}"),
    ),
    (
        "^ssa(?: (.+))?$",
        "staffstrike t with air",
        lambda matches: eqbal(f"stand;staffstrike {s.target} with air"),
    ),
    (
        "^sse(?: (.+))?$",
        "staffstrike t with earth",
        lambda matches: eqbal(f"stand;staffstrike {s.target} with earth"),
    ),
    (
        "^ssf(?: (.+))?$",
        "staffstrike t with fire",
        lambda matches: eqbal(f"stand;staffstrike {s.target} with fire"),
    ),
    (
        "^ssw(?: (.+))?$",
        "staffstrike t with water",
        lambda matches: eqbal(f"stand;staffstrike {s.target} with water"),
    ),
    (
        "^hail$",
        "cast hailstorm",
        lambda matches: eqbal(f"stand;cast hailstorm"),
    ),
    (
        "^ham(?: (.+))?$",
        "cast stormhammer at [] and [] and []",
        lambda matches: stormhammer(matches[0] or None),
    ),
]
c.add_aliases("ab_elementalism", elementalism_aliases)
