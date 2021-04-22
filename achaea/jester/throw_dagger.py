import re

from colorama import Fore, Style

from achaea.basic import eqbal
from achaea.state import s
from client import c, send
from telnet_manager import strip_ansi

THROW_DAGGER_HELP = """
THROW DAGGERS!
dj  - juggle daggers
dc  - throw dagger curare (paralysis - broot/magnesium)
dk  - throw dagger kalmia (asthma - kelp/aurum)
dg  - throw dagger gecko (slickness - broot/magnesium // smoke val/realgar)
da  - throw dagger aconite (stupidity - goldenseal/plumbum/focus)
ds  - throw dagger slike (anorexia - epidermal/focus)
dv  - throw dagger vernalius (weariness - kelp/aurum)
"""


def _throw_dagger(target, venom):
    eqbal(f"stand;get dagger;throw dagger at {target} {venom}")


def juggle_daggers():
    eqbal(
        f"stand;get dagger;get dagger;get dagger;unwield left;juggle dagger dagger dagger;wield blackjack"
    )

dagger_aliases = [
    (
        "^dd$",
        "dagger help",
        lambda m: c.echo(THROW_DAGGER_HELP)
    ),
    (
        "^dj$",
        "juggle daggers!",
        lambda m: juggle_daggers()
    ),
    (
        "^dc$",
        "throw daggers curare!",
        lambda m: _throw_dagger(s.target, "curare")
    ),
    (
        "^dk$",
        "throw daggers kalmia!",
        lambda m: _throw_dagger(s.target, "kalmia")
    ),
    (
        "^dg$",
        "throw daggers gecko!",
        lambda m: _throw_dagger(s.target, "gecko")
    ),
    (
        "^da$",
        "throw daggers aconite!",
        lambda m: _throw_dagger(s.target, "aconite")
    ),
    (
        "^ds$",
        "throw daggers slike!",
        lambda m: _throw_dagger(s.target, "slike")
    ),
    (
        "^dv$",
        "throw daggers vernalius!",
        lambda m: _throw_dagger(s.target, "vernalius")
    ),
]
c.add_aliases("dagger", dagger_aliases)


juggled_items = []


def begin_juggling(matches):
    global juggled_items
    juggled_items = list(matches)
    c.echo(f"juggling: {juggled_items}")


def threw_something(matches):
    # You cock back your arm and throw an obsidian dagger at Parthenope.
    # You cock back your arm and throw an obsidian dagger southwest at Ellryn.

    # figure out if it was a direction
    global juggled_items
    item = matches[0]
    try:
        juggled_items.remove(item)
    except ValueError as e:
        c.echo(f"I guess I wasn't juggling: {item}")
    c.echo(f"ha! threw: {item}")


re_venom = re.compile("You rub some (.*) on (.*).")
re_throw = re.compile(r"You cock back your arm and throw (.*) at (\w+).")
re_throw = re.compile(r"(\w+) twists (\w+) body out of harm's way.")

def queued_throw_dagger(current_chunk):
    #Running queued eqbal command: STAND;GET DAGGER;THROW DAGGER AT RASAHI ACONITE\r\nYou are not fallen or kneeling.\r\nI see no \"dagger\" to take.\r\nYou rub some aconite on an obsidian dagger.\r\nYou cock back your arm and throw an obsidian dagger at Rasahi.

    #Running queued eqbal command: STAND;GET DAGGER;THROW DAGGER AT RASAHI ACONITE\r\nYou are not fallen or kneeling.\r\nYou pick up an obsidian dagger.\r\nYou must have whatever you wish to throw wielded.

    #Lizabel twists her body out of harm's way.


    current_chunk = strip_ansi(current_chunk)

    info = {}
    info["missed"] = False

    for line in current_chunk.split("\r\n"):

        matches = re_venom.match(line)
        if matches:
            m = matches.groups()
            venom = m[0]
            weapon = m[1]
            c.echo(f"venom: {venom} weapon: {weapon}")
            info["venom"] = venom
            info["weapon"] = weapon
            continue

        matches = re_throw.match(line)
        if matches:
            m = matches.groups()
            weapon = m[0]
            target = m[1]
            info["target"] = target
            c.echo(f"target: {target} weapon: {weapon}")

        if line == "You must have whatever you wish to throw wielded.":
            c.echo(f"{Fore.YELLOW}{Style.BRIGHT}#######################")
            c.echo("## NOT JUGGLING !!!  ##")
            c.echo(f"#######################{Style.NORMAL}")

        matches = re_throw_miss.match(line)
        if matches:
            info["missed"] = True

    if info["missed"] == False:
            c.echo(f"{Fore.YELLOW}{Style.BRIGHT}#######################")
            c.echo("## NOT JUGGLING !!!  ##")
            c.echo(f"#######################{Style.NORMAL}")


juggling_triggers = [
    (
        r"^You begin to juggle (.+), (.+), and (.+) with your free hand.$",
        # starting to juggle something
        lambda m: begin_juggling(m),
    ),
    (
        r"^You cock back your arm and throw (.+) at (.+).$",
        # threw something at someone
        lambda m: threw_something(m),
    ),
    (
        r"Running queued eqbal command: (.*)THROW DAGGER AT (\w+) (\w+)",
        # threw something at someone
        lambda m: queued_throw_dagger(c.current_chunk),
    ),
]
c.add_triggers(juggling_triggers)


#Running queued eqbal command: STAND;GET DAGGER;THROW DAGGER AT RASAHI ACONITE\r\nYou are not fallen or kneeling.\r\nI see no \"dagger\" to take.\r\nYou rub some aconite on an obsidian dagger.\r\nYou cock back your arm and throw an obsidian dagger at Rasahi.

#Running queued eqbal command: STAND;GET DAGGER;THROW DAGGER AT RASAHI ACONITE\r\nYou are not fallen or kneeling.\r\nYou pick up an obsidian dagger.\r\nYou must have whatever you wish to throw wielded.

#Running queued eqbal command: STAND;GET DAGGER;GET DAGGER;GET DAGGER;UNWIELD LEFT;JUGGLE DAGGER DAGGER DAGGER;WIELD BLACKJACK\r\nYou are not fallen or kneeling.\r\nI see no \"dagger\" to take.\r\nI see no \"dagger\" to take.\r\nI see no \"dagger\" to take.\r\nYou cease wielding a small blackjack in your left hand.\r\nYou begin to juggle an obsidian dagger, an obsidian dagger, and an obsidian dagger with your free hand.

#Running queued eqbal command: STAND;GET DAGGER;GET DAGGER;GET DAGGER;UNWIELD LEFT;JUGGLE DAGGER DAGGER DAGGER;WIELD BLACKJACK\r\nYou must regain balance first.\r\nYou must regain balance first.\r\nYou must regain balance first.\r\nYou must regain balance first.\r\nYou must regain balance first.\r\nYou must have one empty hand to juggle.

#Running queued eqbal command: STAND;GET DAGGER;GET DAGGER;GET DAGGER;UNWIELD LEFT;JUGGLE DAGGER DAGGER DAGGER;WIELD BLACKJACK\r\nYou are not fallen or kneeling.\r\nYou pick up an obsidian dagger.\r\nI see no \"dagger\" to take.\r\nI see no \"dagger\" to take.\r\nYou cease wielding a small blackjack in your left hand.\r\nYou begin to juggle an obsidian dagger, an obsidian dagger, and an obsidian dagger with your free hand.

#Running queued eqbal command: STAND;GET DAGGER;GET DAGGER;GET DAGGER;UNWIELD LEFT;JUGGLE DAGGER DAGGER DAGGER;WIELD BLACKJACK\r\nYou are not fallen or kneeling.\r\nYou pick up an obsidian dagger.\r\nI see no \"dagger\" to take.\r\nI see no \"dagger\" to take.\r\nYou aren't wielding that.\r\nYou cannot juggle more than three things.\r\nYou start to wield a small blackjack in your left hand.


## start juggling
#["2020/10/27 22:03:34.442121", "gmcp_data", "{\"type\": \"Char.Items.Update\", \"data\": {\"location\": \"inv\", \"item\": {\"id\": \"587891\", \"name\": \"a concussion bomb\", \"icon\": \"clothing\", \"attrib\": \"Wg\"}}}"]
#["2020/10/27 22:03:34.442305", "gmcp_data", "{\"type\": \"Char.Vitals\", \"data\": {\"hp\": \"4300\", \"maxhp\": \"4300\", \"mp\": \"4237\", \"maxmp\": \"4730\", \"ep\": \"15178\", \"maxep\": \"16400\", \"wp\": \"16150\", \"maxwp\": \"16400\", \"nl\": \"19\", \"bal\": \"0\", \"eq\": \"1\", \"string\": \"H:4300/4300 M:4237/4730 E:15178/16400 W:16150/16400 NL:19/100 \", \"charstats\": [\"Bleed: 0\", \"Rage: 0\"]}}"]
#["2020/10/27 22:03:34.442524", "server_text", "\u001b[1;32m[\u001b[0;37mSystem\u001b[1;32m]\u001b[0;37m: Added STAND;GET DAGGER;GET DAGGER;GET DAGGER;UNWIELD LEFT;JUGGLE DAGGER DAGGER DAGGER;WIELD BLACKJACK to your eqbal queue.\r\n\u001b[1;32m[\u001b[0;37mSystem\u001b[1;32m]\u001b[0;37m: Running queued eqbal command: STAND;GET DAGGER;GET DAGGER;GET DAGGER;UNWIELD LEFT;JUGGLE DAGGER DAGGER DAGGER;WIELD BLACKJACK\r\nYou are not fallen or kneeling.\r\nI see no \"dagger\" to take.\r\nI see no \"dagger\" to take.\r\nI see no \"dagger\" to take.\r\nYou cease wielding a concussion bomb in your left hand.\r\nYou begin to juggle an obsidian dagger, an obsidian dagger, and an obsidian dagger with your free hand.\r\nYou must regain balance first.\r\n\u001b[32m4300h, \u001b[37m\u001b[32m4237m \u001b[37mcekdb-"]
#
#
## throwing a dagger
#["2020/10/27 22:03:37.631843", "gmcp_data", "{\"type\": \"Char.Defences.Remove\", \"data\": [\"rebounding\"]}"]
#["2020/10/27 22:03:37.632161", "gmcp_data", "{\"type\": \"Char.Items.Remove\", \"data\": {\"location\": \"inv\", \"item\": {\"id\": \"70148\", \"name\": \"an obsidian dagger\", \"icon\": \"weapon\"}}}"]
#["2020/10/27 22:03:37.632273", "gmcp_data", "{\"type\": \"Char.Items.Add\", \"data\": {\"location\": \"room\", \"item\": {\"id\": \"70148\", \"name\": \"an obsidian dagger\", \"icon\": \"weapon\"}}}"]
#["2020/10/27 22:03:37.632506", "gmcp_data", "{\"type\": \"Char.Status\", \"data\": {\"gold\": \"4176\"}}"]
#["2020/10/27 22:03:37.632652", "gmcp_data", "{\"type\": \"Char.Vitals\", \"data\": {\"hp\": \"4300\", \"maxhp\": \"4300\", \"mp\": \"4212\", \"maxmp\": \"4730\", \"ep\": \"15123\", \"maxep\": \"16400\", \"wp\": \"16151\", \"maxwp\": \"16400\", \"nl\": \"19\", \"bal\": \"0\", \"eq\": \"1\", \"string\": \"H:4300/4300 M:4212/4730 E:15123/16400 W:16151/16400 NL:19/100 \", \"charstats\": [\"Bleed: 0\", \"Rage: 0\"]}}"]
#["2020/10/27 22:03:37.632910", "server_text", "\u001b[1;32m[\u001b[0;37mSystem\u001b[1;32m]\u001b[0;37m: Added STAND;GET DAGGER;THROW DAGGER AT PARTHENOPE KALMIA to your eqbal queue.\r\n\u001b[1;32m[\u001b[0;37mSystem\u001b[1;32m]\u001b[0;37m: Running queued eqbal command: STAND;GET DAGGER;THROW DAGGER AT PARTHENOPE KALMIA\r\nYou are not fallen or kneeling.\r\nI see no \"dagger\" to take.\r\nYour aura of weapons rebounding disappears.\r\nYou rub some kalmia on an obsidian dagger.\r\nYou cock back your arm and throw an obsidian dagger at Parthenope.\r\nParthenope exhales loudly.\r\n\u001b[32m4300h, \u001b[37m\u001b[32m4212m \u001b[37mcekdb-"]
#
#
## not juggling
#["2020/10/27 22:03:27.267595", "data_sent", "queue add eqbal stand;get dagger;throw dagger at Parthenope kalmia"]
#["2020/10/27 22:03:27.380494", "gmcp_data", "{\"type\": \"Char.Items.Remove\", \"data\": {\"location\": \"room\", \"item\": {\"id\": \"480163\", \"name\": \"an obsidian dagger\", \"icon\": \"weapon\", \"attrib\": \"t\"}}}"]
#["2020/10/27 22:03:27.380890", "gmcp_data", "{\"type\": \"Char.Items.Add\", \"data\": {\"location\": \"inv\", \"item\": {\"id\": \"480163\", \"name\": \"an obsidian dagger\", \"icon\": \"weapon\", \"attrib\": \"t\"}}}"]
#["2020/10/27 22:03:27.381082", "gmcp_data", "{\"type\": \"Char.Status\", \"data\": {\"gold\": \"4176\"}}"]
#["2020/10/27 22:03:27.381226", "gmcp_data", "{\"type\": \"Char.Vitals\", \"data\": {\"hp\": \"4166\", \"maxhp\": \"4300\", \"mp\": \"4386\", \"maxmp\": \"4730\", \"ep\": \"15168\", \"maxep\": \"16400\", \"wp\": \"16147\", \"maxwp\": \"16400\", \"nl\": \"19\", \"bal\": \"1\", \"eq\": \"1\", \"string\": \"H:4166/4300 M:4386/4730 E:15168/16400 W:16147/16400 NL:19/100 \", \"charstats\": [\"Bleed: 0\", \"Rage: 0\"]}}"]
#["2020/10/27 22:03:27.381475", "server_text", "\u001b[1;32m[\u001b[0;37mSystem\u001b[1;32m]\u001b[0;37m: Added STAND;GET DAGGER;THROW DAGGER AT PARTHENOPE KALMIA to your eqbal queue.\r\n\u001b[1;32m[\u001b[0;37mSystem\u001b[1;32m]\u001b[0;37m: Running queued eqbal command: STAND;GET DAGGER;THROW DAGGER AT PARTHENOPE KALMIA\r\nYou are not fallen or kneeling.\r\nYou pick up an obsidian dagger.\r\nYou must have whatever you wish to throw wielded.\r\n\u001b[32m4166h, \u001b[37m\u001b[32m4386m \u001b[37mcexkdb-"]
#
#
## currently juggling something
#You cannot juggle more than three things.
#
#
## throw dagger ne
#["2020/10/27 22:53:34.800411", "gmcp_data", "{\"type\": \"Char.Items.Remove\", \"data\": {\"location\": \"inv\", \"item\": {\"id\": \"555673\", \"name\": \"an obsidian dagger\", \"icon\": \"weapon\"}}}"]
#["2020/10/27 22:53:34.800585", "gmcp_data", "{\"type\": \"Char.Status\", \"data\": {\"gold\": \"8210\"}}"]
#["2020/10/27 22:53:34.800691", "gmcp_data", "{\"type\": \"Char.Vitals\", \"data\": {\"hp\": \"4300\", \"maxhp\": \"4300\", \"mp\": \"4680\", \"maxmp\": \"4730\", \"ep\": \"6576\", \"maxep\": \"16400\", \"wp\": \"16400\", \"maxwp\": \"16400\", \"nl\": \"24\", \"bal\": \"0\", \"eq\": \"1\", \"string\": \"H:4300/4300 M:4680/4730 E:6576/16400 W:16400/16400 NL:24/100 \", \"charstats\": [\"Bleed: 0\", \"Rage: 0\"]}}"]
#["2020/10/27 22:53:34.800905", "server_text", "You hurl an obsidian dagger northeast.\r\n\u001b[32m4300h, \u001b[37m\u001b[32m4680m \u001b[37mcekdb-"]
#
#
## throw dagger sw at ellryn
#["2020/10/27 23:24:00.937111", "gmcp_data", "{\"type\": \"Char.Items.Remove\", \"data\": {\"location\": \"inv\", \"item\": {\"id\": \"388122\", \"name\": \"an obsidian dagger\", \"icon\": \"weapon\"}}}"]
#["2020/10/27 23:24:00.937325", "gmcp_data", "{\"type\": \"Char.Status\", \"data\": {\"gold\": \"8210\"}}"]
#["2020/10/27 23:24:00.937463", "gmcp_data", "{\"type\": \"Char.Vitals\", \"data\": {\"hp\": \"4300\", \"maxhp\": \"4300\", \"mp\": \"4730\", \"maxmp\": \"4730\", \"ep\": \"9727\", \"maxep\": \"16400\", \"wp\": \"16400\", \"maxwp\": \"16400\", \"nl\": \"24\", \"bal\": \"0\", \"eq\": \"1\", \"string\": \"H:4300/4300 M:4730/4730 E:9727/16400 W:16400/16400 NL:24/100 \", \"charstats\": [\"Bleed: 0\", \"Rage: 0\"]}}"]
#["2020/10/27 23:24:00.937777", "server_text", "You cock back your arm and throw an obsidian dagger southwest at Ellryn.\r\n\u001b[32m4300h, \u001b[37m\u001b[32m4730m \u001b[37mcekdb-"]
