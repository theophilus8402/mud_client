from achaea.basic import eqbal
from achaea.state import s
from achaea.group_fighting.party import party_announce, register_announce_type
from client import c, send

telepathy_aliases = [
    (
        "^sense(?: (.+))?$",
        "mind sense []/t",
        lambda matches: eqbal(f"mind sense {matches[0] or s.target}"),
    ),
    (
        "^ml(?: (.+))?$",
        "mind lock []/t",
        lambda matches: eqbal(f"mind lock {matches[0] or s.target}"),
    ),
    (
        "^mul(?: (.+))?$",
        "mind unlock []/t",
        lambda matches: eqbal(f"mind unlock {matches[0] or s.target}"),
    ),
    (
        "^mg$",
        "mind glance",
        lambda matches: eqbal(f"mind glance"),
    ),
    (
        "^mt(?: (.+))?$",
        "mind telesense [on]/off",
        lambda matches: eqbal(f"mind telesense {matches[0] or 'on'}"),
    ),
    (
        "^mf(?: (.+))?$",
        "mind fear [on]/off",
        lambda matches: eqbal(f"mind fear {matches[0] or s.target}"),
    ),
    (
        "^throw(?: (.+))?$",
        "mind throw dir",
        lambda matches: eqbal(f"mind throw {matches[0] or 'n'};mind lock {s.target}"),
    ),
    (
        "^ter$",
        "mind terror",
        lambda matches: eqbal(f"mind glance"),
    ),
    (
        "^mc(?: (.+))?$",
        "mind confuse []/t",
        lambda matches: eqbal(f"mind confuse {matches[0] or s.target}"),
    ),
    (
        "^msuf$",
        "mind suffuse",
        lambda matches: eqbal(f"mind suffuse"),
    ),
    (
        "^md(?: (.+))?$",
        "mind drain []/t",
        lambda matches: eqbal(f"mind drain {matches[0] or s.target}"),
    ),
    (
        "^mlist$",
        "mind listen",
        lambda matches: eqbal(f"mind listen"),
    ),
    (
        "^munlist$",
        "mind unlisten",
        lambda matches: eqbal(f"mind unlisten"),
    ),
    (
        "^mdiv(?: (.+))?$",
        "mind divine []/t",
        lambda matches: eqbal(f"mind divine {matches[0] or s.target}"),
    ),
    (
        "^fs$",
        "fullsense",
        lambda matches: eqbal(f"fullsense"),
    ),
    (
        "^miso$",
        "mind isolate",
        lambda matches: eqbal(f"mind isolate"),
    ),
    (
        "^muso$",
        "mind unisolate",
        lambda matches: eqbal(f"mind unisolate"),
    ),
    (
        "^dis(?: (.+))?$",
        "mind disrupt []/t",
        lambda matches: eqbal(f"mind disrupt {matches[0] or s.target}"),
    ),
    (
        "^mi(?: (.+))?$",
        "mind impatience []/t",
        lambda matches: eqbal(f"mind impatience {matches[0] or s.target}"),
    ),
    (
        "^me(?: (.+))?$",
        "mind epilepsy []/t",
        lambda matches: eqbal(f"mind epilepsy {matches[0] or s.target}"),
    ),
    (
        "^pac$",
        "mind pacify",
        lambda matches: eqbal(f"mind pacify"),
    ),
    (
        "^ms(?: (.+))?$",
        "mind stupidity []/t",
        lambda matches: eqbal(f"mind epilepsy {matches[0] or s.target}"),
    ),
    (
        "^mcl(?: (.+))?$",
        "mind cloak [on]/off",
        lambda matches: eqbal(f"mind cloak {matches[0] or 'on'}"),
    ),
    (
        "^mp(?: (.+))?$",
        "mind paralyse []/t",
        lambda matches: eqbal(f"mind paralyse {matches[0] or s.target}"),
    ),
    (
        "^hyp(?: (.+))?$",
        "mind hypersense []/t",
        lambda matches: eqbal(f"mind hypersense {matches[0] or 'on'}"),
    ),
    (
        "^ma(?: (.+))?$",
        "mind amnesia []/t",
        lambda matches: eqbal(f"mind amnesia {matches[0] or s.target}"),
    ),
    (
        "^mbar$",
        "mind barrier",
        lambda matches: eqbal(f"mind barrier"),
    ),
    (
        "^mubar$",
        "mind unbarrier",
        lambda matches: eqbal(f"mind unbarrier"),
    ),
    (
        "^scan$",
        "mind scan",
        lambda matches: eqbal(f"mind scan"),
    ),
    (
        "^mdead(?: (.+))?$",
        "mind deadening []/t",
        lambda matches: eqbal(f"mind deadening {matches[0] or s.target};mind unlock;mind lock {matches[0] or s.target}"),
    ),
    (
        "^mtrav$",
        "mind travel",
        lambda matches: eqbal(f"mind travel"),
    ),
    (
        "^mnet(?: (.+))?$",
        "mindnet [on]/off",
        lambda matches: eqbal(f"mindnet {matches[0] or 'on'}"),
    ),
    (
        "^mcr(?: (.+))?$",
        "mind crush []/t",
        lambda matches: eqbal(f"mind crush {matches[0] or s.target}"),
    ),
    (
        "^mda$",
        "mind daze",
        lambda matches: eqbal(f"mind daze"),
    ),
    (
        "^mstr(?: (.+))?$",
        "mind strip []/t",
        lambda matches: eqbal(f"mind strip {matches[0] or s.target}"),
    ),
    (
        "^msap$",
        "mind sapience",
        lambda matches: eqbal(f"mind sapience"),
    ),
    (
        "^clamp$",
        "mind clamp",
        lambda matches: eqbal(f"mind clamp"),
    ),
    (
        "^uclamp$",
        "mind unclamp",
        lambda matches: eqbal(f"mind unclamp"),
    ),
    (
        "^bl$",
        "mind blackout",
        lambda matches: eqbal(f"mind blackout"),
    ),
    (
        "^scy$",
        "mind scythe",
        lambda matches: eqbal(f"mind scythe"),
    ),
    (
        "^mb(?: (.+))?$",
        "mind batter []/t",
        lambda matches: eqbal(f"mind batter {matches[0] or s.target}"),
    ),
    (
        "^srad$",
        "mind radiance",
        lambda matches: eqbal(f"mind radiance"),
    ),
    (
        "^pr$",
        "mind print",
        lambda matches: eqbal(f"mind print"),
    ),
]
c.add_aliases("ab_telepathy", telepathy_aliases)


register_announce_type("telepathy")

def tannounce(msg):
    c.echo(msg)
    party_announce(msg, "telepathy")


telepathy_triggers = [
    (
        r"^You focus your mind, and begin to concentrate on forming a mind lock with",
        # starting a mind lock
        lambda m: tannounce("Starting mind lock"),
    ),
    (
        r"^Your telepathic efforts are successful, and the mind of (.*) is",
        # mind locked em!
        lambda m: tannounce(f"mind locked: {m[0]}"),
    ),
    (
        r"^Your mental lock on (.*) is shattered as",
        # lost lock!
        lambda m: c.echo(f"LOST LOCK {m[0]}\nLOST LOCK {m[0]}\nLOST LOCK {m[0]}"),
    ),
    (
        r"^You summon up your will and throw a devastating shaft of telepathic energy into (\w+), causing \w+ to experience a total blackout.$",
        # black out
        lambda m: tannounce(f"blackout: {m[0]}")
    ),
    (
        r"^You quickly attack (\w+)'s mind from multiple directions, upsetting \w+ equilibrium.$",
        # disrupt
        lambda m: tannounce(f"disrupt: {m[0]}")
    ),
    (
        r"^You direct a powerful pulse of telepathic energy into (\w+), throwing \w+ mind into chaos and confusion.$",
        # confusion
        lambda m: tannounce(f"confusion: {m[0]}")
    ),
]
c.add_triggers(telepathy_triggers)
