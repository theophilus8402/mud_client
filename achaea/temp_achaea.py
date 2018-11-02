
import asyncio
import random
import re
from datetime import datetime,timedelta

from modules.basemodule import BaseModule

def eq_bal(action, mud=None, matches=None):
    #print("eq_bal, msg: {}".format(action))
    msg = "queue add eqbal {}".format(action)
    if mud:
        mud.send(msg)
    else:
        return msg

def eat_herb(herb, mud=None, matches=None):
    msg = "outr {herb}\neat {herb}".format(herb=herb)
    if mud:
        mud.send(msg)
    else:
        return msg

def instill(target, mud=None, matches=None):
    return

def command_ent(entity, target, mud=None, matches=None):
    msg = "queue add class command {} at {}".format(entity, target)
    if mud:
        mud.send(msg)
    else:
        return msg

def auto_ent(entity, on=False):
    return

def remember_path(on, mud):
    # set it to True/False as dictated by "on"
    mud.v.remember_path = on
    if on:
        mud.v.path_to_remember = list()
    #return ""

def show_path(mud, matches=None):
    path = getattr(mud.v, "path_to_remember", [])
    print("path: {}".format(path))

def random_move(client):
    exits = list(client.v.room["exits"].keys())
    exit = random.choice(exits)
    move(exit, client)

def move(direction, mud):
    #print("v: {}".format(mud.v))
    remember_path = getattr(mud.v, "remember_path", False)
    if remember_path:
        mud.v.path_to_remember.append(direction)
    mud.send("queue prepend eqbal {}".format(direction))
    #return ""


def start_shown_map(client, matches):
    #client.v.showing_map = True
    print(client.line)
    print("showing_map!")
    # the line will be written to map_log by handle_input in pycat


def end_shown_map(client, matches):
    # write the line to map_log
    #print(client.line, file=client.map_log, flush=True)
    print(client.line) #, file=client.map_log, flush=True)
    print("NOT showing_map!")
    # set showing_map = False
    client.v.showing_map = False
    # need to return "" to make sure it doesn't get printed to screen
    return ""

shown_map_triggers = {
    "^--- Area (\d+): (.*) --+$": start_shown_map,
    "^--+ -?(\d+):-?(\d+):-?(\d+) --+$": end_shown_map,
}

def ratting(client, matches):
    if matches[0] == "on":

        # call the ratting function again in 3 seconds just incase there hasn't been much movement in the room
        client.timers["ratting"] = client.mktimer(3, lambda: rat(client, matches))

        client.v.ratting = True
    else:
        client.v.ratting = False
        del(client.timers["ratting"])


def ratting_move_on(client):
    client.v.rooms_ratted.add(client.v.room["num"])
    random_move(client)


def rat(client, matches):

    if datetime.now() < client.v.last_rat_call + timedelta(seconds=1):
        #print("You've run 'rat' too recently!")
        return

    # print("running rat!")

    # if it looks like we've been ratting in the room before, move on
    if client.v.room["num"] in client.v.rooms_ratted:
        print("It looks like we've ratted here before, moving on...")
        ratting_move_on(client)
        return

    # if we've been waiting for 15 seconds with no sign of a rat, move on
    if datetime.now() >= client.v.rat_last_seen + timedelta(seconds=15):
        print("We've been waiting for too long!  It's time to move on!")
        ratting_move_on(client)
        # move on
        return

    client.v.last_rat_call = datetime.now()
    if len(client.v.players_in_room) >= 1:
        print("There ARE people in the room!")
        # move on
        ratting_move_on(client)
        return

    # check to see if we've killed all the rats in the room
    if client.v.rats_killed_in_room >= 3:
        print("Killed {} rats here!  Moving on...".format(client.v.rats_killed_in_room))
        # move on
        ratting_move_on(client)
        return

    rat_in_room = False
    for mob,mob_id in client.v.mobs_in_room:
        print(mob)
        if "rat" in mob:
            rat_in_room = True
            client.v.rat_last_seen = datetime.now()
            break
    if not rat_in_room:
        #print("There's NOT a rat in the room!")
        return

    if not (client.v.bal and client.v.eq):
        #print("You DON'T have bal/eq!")
        return
    attack(client, matches)

def slain(client, matches):

    # this can be used for a number of things

    # check to see if we kill a rat for our ratting counter
    if "rat" in matches[0]:
        client.v.rats_killed_in_room += 1
        print("Rats killed in room: {}".format(client.v.rats_killed_in_room))

RE_CORPSE = re.compile("the corpse of (.*)")


mapping_aliases = {
    "^rpon$" : lambda mud,_: remember_path(on=True, mud=mud),
    "^rpoff$" : lambda mud,_: remember_path(on=False, mud=mud),
    "^showpath$" : show_path,
}

aff_healing_aliases = {
    "^dh$" : "drink health",
    "^dm$" : "drink mana",
    "^moss$" : eat_herb("moss"),
    "^broot$" : eat_herb("bloodroot"),
    "^coh$" : eat_herb("cohosh"),
    "^kelp$" : eat_herb("kelp"),
    "^myrrh$" : eat_herb("myrrh"),
    "^pear$" : eat_herb("pear"),
    "^pot$" : eat_herb("potash"),
    "^bay$" : eat_herb("bayberry"),
    "^gin$" : eat_herb("ginseng"),
    "^gold$" : eat_herb("goldenseal"),
    "^kola$" : eat_herb("kola"),
    "^ash$" : eat_herb("ash"),
    "^bell$" : eat_herb("bellwort"),
    "^ech$" : eat_herb("echinacea"),
    "^haw$" : eat_herb("hawthorn"),
    "^lob$" : eat_herb("lobelia"),
    "^ging$" : eat_herb("ginger"),
    "^sil$" : "outr sileris\napply sileris",
}

elixirs_aliases = {
    "^frost$" : "drink frost",
    "^imm$" : "drink immunity",
    "^levi$" : "drink levitation",
    "^speed$" : "drink speed",
    "^venom$" : "drink venom",
}

salves_aliases = {
    "^calor$" : "apply caloric",
    "^epi$" : "apply epidermal to torso",
    "^mass$" : "apply mass",
    "^mend$" : "apply mending",
    "^mendl$" : "apply mending to legs",
    "^menda$" : "apply mending to arms",
    "^resto$" : "apply restoration",
    "^restol$" : "apply restoration to legs",
    "^restoa$" : "apply restoration to arms",
}

pipes_aliases = {
    "^lp$" : "light pipes",
    "^skull$" : "light pipes;smoke pipe with skullcap",
    "^val$" : "light pipes;smoke pipe with valerian",
    "^elm$" : "light pipes;smoke pipe with elm",
}

def sear(client, matches):
    print("searing!")
    if not matches[0]:
        eq_bal("angel sear {}".format(client.v.target), mud=client)
    elif matches[0] in {"n", "ne", "e", "se", "s", "sw", "w", "nw", "u",
                        "d", "in", "out"}:
        eq_bal("stand;angel sear icewall {}".format(matches[0]), mud=client)
    else:
        eq_bal("angel sear {}".format(matches[0]), mud=client)

spirituality_aliases = {
    "^shine(?: (.+))?$" : lambda mud, matches: eq_bal("angel shine {}".format(matches[0] or "")),
    "^cham$" : lambda mud,_: eq_bal("smite {t} chasten {t} mind".format(t=mud.v.target)),
    "^chab$" : lambda mud,_: "stand;smite {t} chasten {t} body".format(t=mud.v.target),
    "^judge(?: (.+))?$" : lambda mud, matches: eq_bal("judge {}".format(matches[0] or "")),
    "^strip(?: (.+))?$" : lambda mud, matches: eq_bal("angel strip {}".format(matches[0] or mud.v.target)),
    "^sear(?: (.+))?$" : sear,
    "^ward$" : eq_bal("angel ward"),
    "^pres$" : eq_bal("angel presences"),
    "^trace(?: (.+))?$" : lambda mud, matches: eq_bal("angel trace {}".format(matches[0] or mud.v.target)),
    "^sap(?: (.+))?$" : lambda mud, matches: eq_bal("angel sap {}".format(matches[0] or mud.v.target)),
    "^care(?: (.+))?$" : lambda mud, matches: eq_bal("angel care {}".format(matches[0])),
    "^wra(?: (.+))?$" : lambda mud, matches: eq_bal("angel spiritwrack {}".format(matches[0] or mud.v.target)),
    "^emp(?: (.+))?$" : lambda mud, matches: eq_bal("angel empathy {}".format(matches[0] or "")),
    "^cont$" : lambda mud,_: eq_bal("contemplate {}".format(mud.v.target)),
    "^sacri$" : lambda mud,_: eq_bal("angel sacrifice"),
    "^absolve$" : lambda mud,_: eq_bal("angel absolve {}".format(mud.v.target)),
}

def pilgrimage(client, matches):
    if matches[0]:
        eq_bal("perform pilgrimage {}".format(matches[0]), mud=client)
    else:
        eq_bal("perform rite of pilgrimage", mud=client)

devotion_aliases = {
    "^hh(?: (.+))?$" : lambda mud, matches: eq_bal("perform hands {}".format(matches[0] or "")),
    "^truth$" : eq_bal("perform truth"),
    "^bliss(?: (.+))?$" : lambda mud, matches: eq_bal("perform bliss {}".format(matches[0] or "me")),
    "^pur(?: (.+))?$" : lambda mud, matches: eq_bal("perform purity {}".format(matches[0] or client.v.target)),
    "^hell(?: (.+))?$" : lambda mud, matches: eq_bal("perform hellsight {}".format(matches[0] or client.v.target)),
    "^pilg(?: (.+))?$" : pilgrimage,
    "^insp$" : eq_bal("perform inspiration"),
    "^pheal$" : eq_bal("perform rite of healing"),
    "^demons$" : eq_bal("perform rite of demons"),
}

def channel_all(client, matches):
    
    for chan in ["air", "fire", "water", "earth", "spirit"]:
        eq_bal("channel {}".format(chan), mud=client)

healing_aliases = {
    "^hdb$" : lambda mud, matches: eq_bal("heal {} blindness;heal {} deafness".format(mud.v.target, mud.v.target)),
    "^chans$" : channel_all,
}

sigil_aliases = {
    "^eyesig$" : "get eyesigil from pack;unwield left;wield eyesigil;throw eyesigil at ground",
}


battlerage_aliases = {
    "^mm$" : lambda mud,_: "angel torment {}".format(mud.v.target),
    "^incen$" : lambda mud,_: "angel incense {}".format(mud.v.target),
    "^cra$" : lambda mud,_: "crack {}".format(mud.v.target),
    "^deso$" : lambda mud,_: "perform rite of desolation on {}".format(mud.v.target),
    #"^mm$" : lambda mud,_: "harry {}".format(mud.v.target),
    #"^cg$" : lambda mud,_: "chaosgate {}".format(mud.v.target),
    #"^rui$" : lambda mud,_: "ruin {}".format(mud.v.target),
}

tattoo_aliases = {
    "^clk$" : eq_bal("touch cloak"),
    #"^shd$" : eq_bal("touch shield"),
    "^shd$" : eq_bal("angel aura"),
    "^minds$" : eq_bal("touch mindseye"),
}

def multiple_ally(client, matches):
    for person in matches[0].split(" "):
        client.send("ally {}".format(person))

def multiple_enemy(client, matches):
    for person in matches[0].split(" "):
        client.send("enemy {}".format(person))

misc_aliases = {
    "^pg$" : "put coins in pack",
    "^gg$" : "get gold",
    "^gp (.+)$" : lambda mud, matches: "get {} gold from pack".format(matches[0]),
    "^rat$" : rat,
    "^rat (.*)$" : ratting,
    "^men (.+)$" : multiple_enemy,
    "^mall (.+)$" : multiple_ally,
}

anti_theft_aliases = {
    "^self$" : "selfishness",
    "^gener$" : "generosity",
}

occultism_aliases = {
    "^ague(?: (.+))?$" : lambda mud, matches: eq_bal("ague {}".format(matches[0] or mud.v.target)),
    "^agl(?: (.+))?$" : lambda mud, matches: eq_bal("auraglance {}".format(matches[0] or mud.v.target)),
    "^bwarp$" : eq_bal("bodywarp"),
    "^att(?: (.+))?$" : lambda mud, matches: eq_bal("attend {}".format(matches[0] or mud.v.target)),
    "^ene(?: (.+))?$" : lambda mud, matches: eq_bal("enervate {}".format(matches[0] or mud.v.target)),
    "^qui(?: (.+))?$" : lambda mud, matches: eq_bal("quicken {}".format(matches[0] or mud.v.target)),
    "^sarm(?: (.+))?$" : lambda mud, matches: eq_bal("shrivel arms {}".format(mud.v.target)),
    "^sleg(?: (.+))?$" : lambda mud, matches: eq_bal("shrivel legs {}".format(mud.v.target)),
    "^twarp(?: (.+))?$" : eq_bal("timewarp"),
    "^daura(?: (.+))?$" : eq_bal("distortaura"),
    "^pclk(?: (.+))?$" : lambda mud, matches: eq_bal("pinchaura {} cloak".format(matches[0] or mud.v.target)),
    "^pspe(?: (.+))?$" : lambda mud, matches: eq_bal("pinchaura {} speed".format(mud.v.target)),
    "^pcalor(?: (.+))?$" : lambda mud, matches: eq_bal("pinchaura {} caloric".format(mud.v.target)),
    "^pfrost(?: (.+))?$" : lambda mud, matches: eq_bal("pinchaura {} frost".format(mud.v.target)),
    "^plevi(?: (.+))?$" : lambda mud, matches: eq_bal("pinchaura {} levitation".format(mud.v.target)),
    "^pinsom(?: (.+))?$" : lambda mud, matches: eq_bal("pinchaura {} insomnia".format(mud.v.target)),
    "^pkola(?: (.+))?$" : lambda mud, matches: eq_bal("pinchaura {} kola".format(mud.v.target)),
    "^spe(?: (.+))?$" : eq_bal("unnamable speak"),
    "^vis(?: (.+))?$" : eq_bal("unnamable vision"),
    "^devo(?: (.+))?$" : lambda mud, matches: eq_bal("devolve {}".format(mud.v.target)),
    "^caura(?: (.+))?$" : lambda mud, matches: eq_bal("cleanseaura {}".format(mud.v.target)),
    "^tent(?: (.+))?$" : eq_bal("tentacles"),
    "^inst(?: (.+))?$" : lambda mud, matches: instill(matches[0] or mud.v.target),
    "^whisp$" : lambda mud, matches: eq_bal("whisperingmadness {}".format(mud.v.target)),
    "^dev$" : eq_bal("devilmark"),
    "^enl$" : lambda mud, matches: eq_bal("enlighten {}".format(matches[0] or mud.v.target)),
    "^ast$" : eq_bal("astralform"),
    "^devo$" : lambda mud, matches: eq_bal("unravel mind of {}".format(mud.v.target)),
    "^ra$" : lambda mud, matches: eq_bal("readaura {}".format(mud.v.target)),
}

tarot_aliases = {
    "^sun$" : eq_bal("fling sun at ground"),
    "^priest(?: (.+))?$" : lambda mud, matches: eq_bal("fling priestess at {}".format(matches[0] or "me")),
    "^magi(?: (.+))?$" : lambda mud, matches: eq_bal("fling magician at {}".format(matches[0] or "me")),
    "^fool(?: (.+))?$" : lambda mud, matches: eq_bal("fling fool at {}".format(matches[0] or "me")),
    "^hang(?: (.+))?$" : lambda mud, matches: eq_bal("fling hangedman at {}".format(matches[0] or mud.v.target)),
    "^star(?: (.+))?$" : lambda mud, matches: eq_bal("fling star at {}".format(matches[0] or mud.v.target)),
    "^just(?: (.+))?$" : lambda mud, matches: eq_bal("fling justice at {}".format(matches[0] or mud.v.target)),
    "^aeon(?: (.+))?$" : lambda mud, matches: eq_bal("fling aeon at {}".format(matches[0] or mud.v.target)),
    "^lust(?: (.+))?$" : lambda mud, matches: eq_bal("fling lust at {}".format(matches[0] or mud.v.target)),
    "^moon(?: (.+))?$" : lambda mud, matches: eq_bal("fling moon at {}".format(matches[0] or mud.v.target)),
    "^devil(?: (.+))?$" : lambda mud, matches: eq_bal("fling devil at ground"),
    "^univ(?: (.+))?$" : lambda mud, matches: eq_bal("fling universe at ground"),
}

domination_aliases = {
    "^derv(?: (.+))?$" : lambda mud, matches: command_ent("dervish", matches[0] or mud.v.target),
    "^syc(?: (.+))?$" : lambda mud, matches: command_ent("sycophant", matches[0] or mud.v.target),
    "^grem(?: (.+))?$" : lambda mud, matches: command_ent("gremlin", matches[0] or mud.v.target),
    "^orb(?: (.+))?$" : lambda mud, matches: command_ent("orb", matches[0] or "me"),
    "^leech(?: (.+))?$" : lambda mud, matches: command_ent("bloodleech", matches[0] or mud.v.target),
    "^leechon$" : auto_ent("bloodleech", on=True),
    "^leechoff$" : auto_ent("bloodleech", on=False),
    "^nem(?: (.+))?$" : lambda mud, matches: command_ent("nemesis", matches[0] or mud.v.target),
    "^nemon$" : auto_ent("nemesis", on=True),
    "^nemoff$" : auto_ent("nemesis", on=False),
    "^poss$" : lambda mud, matches: mud.send("order soulmaster possess {}".format(mud.v.target)),
    "^osp$" : lambda mud, matches: mud.send("order {} smoke pipe with skullcap".format(mud.v.target)),
}

direction_aliases = {
    "^n$" : lambda mud,_: move("n", mud),
    "^ne$" : lambda mud,_: move("ne", mud),
    "^nw$" : lambda mud,_: move("nw", mud),
    "^e$" : lambda mud,_: move("e", mud),
    "^s$" : lambda mud,_: move("s", mud),
    "^se$" : lambda mud,_: move("se", mud),
    "^sw$" : lambda mud,_: move("sw", mud),
    "^w$" : lambda mud,_: move("w", mud),
    "^in$" : lambda mud,_: move("in", mud),
    "^out$" : lambda mud,_: move("out", mud),
    "^u$" : lambda mud,_: move("u", mud),
    "^d$" : lambda mud,_: move("d", mud),
    "^rdir$" : lambda mud,_: random_move(mud)
}

def says(mud, matches):
    #print("Found something that is a say!")
    with open("says.txt", "a") as f:
        f.write("{}\n".format(mud.line))

def target(mud, matches):
    mud.v.target = matches[0]
    print("new target: {}".format(mud.v.target))

def attack(mud, _):
    #mud.send("stand\nwarp {}".format(mud.v.target))
    eq_bal("stand;smite {}".format(mud.v.target), mud=mud)

def echo(msg, mud=None):
    if mud:
        print(msg, end="")
    else:
        return lambda mud,_: print(msg, end="")

def exits(mud, matches):
    print("exits: {}".format(matches[0]))
    #pass

class Achaea(BaseModule):

    def __init__(self, session, client):
        print("Starting Achaea module!")
        self.client = client
        super().__init__(session)

    def display_status_info(self):
        file_name = "status_info.txt"
        with open(file_name, "w") as f:
            f.write("\n"*6)
            mobs = [m.split(" ")[-1] for m,i in self.client.v.mobs_in_room]
            f.write("room: {}\n".format(", ".join([*self.client.v.players_in_room, *mobs])))

    def handleGmcp(self, cmd, value):
        if cmd == "Char.Items.List":
            # GMCP! cmd: Char.Items.List value: {'location': 'room', 'items': [{'id': '44247', 'name': 'a runic totem', 'icon': 'rune'}, {'id': '213216', 'name': 'a demented skyscourge', 'icon': 'guard', 'attrib': 'mx'}, {'id': '213970', 'name': 'a demented skyscourge', 'icon': 'guard', 'attrib': 'mx'}, {'id': '314205', 'name': 'a logosmas stocking', 'icon': 'lamp'}, {'id': '355847', 'name': 'a War Witch', 'icon': 'guard', 'attrib': 'mx'}, {'id': '419262', 'name': 'a small cooking stove'}, {'id': '450780', 'name': 'a thrall of the wheel', 'icon': 'guard', 'attrib': 'mx'}, {'id': '72156', 'name': 'a thrall of the wheel', 'icon': 'guard', 'attrib': 'mx'}, {'id': '501673', 'name': 'an old rat', 'icon': 'animal', 'attrib': 'm'}, {'id': '520131', 'name': 'a rat', 'icon': 'animal', 'attrib': 'm'}]} type value: <class 'dict'>
            if value["location"] == "room":
                self.client.v.mobs_in_room = {(item["name"], item["id"]) for item in value["items"] if item.get("attrib") == "m"}
                self.display_status_info()
        elif cmd == "Char.Items.Add":
            # make sure it was an "item" in the room
            if value['location'] == 'room':
                name = value['item']['name']
                eid = value['item']['id']
                self.client.v.mobs_in_room.add((name, eid))
                self.display_status_info()
                #print("{} {} entered the room!".format(name, eid), end="")
        elif cmd == "Char.Items.Remove":
            # make sure it was an "item" in the room
            if value['location'] == 'room':
                name = value['item']['name']
                eid = value['item']['id']
                # sometimes, this is a mob we have just killed
                # but it shows as a corpse having been removed by
                # me picking it up
                # KeyError: ('the corpse of a black rat', '502337')
                match = RE_CORPSE.match(name)
                if match:
                    name = match.groups()[0]
                self.client.v.mobs_in_room.discard((name, eid))
                self.display_status_info()
                #print("{} {} left the room!".format(name, eid), end="")
        elif cmd == "Room.Players":
            # GMCP! cmd: Room.Players value: [{'name': 'Dirus', 'fullname': "Drudge Dirus Sar'vet"}] type value: <class 'list'>
            self.client.v.players_in_room = {p["name"] for p in value if p["name"] not in {"Dirus", "Palleo"}}
            #echo("Players: {}".format(", ".join(self.client.v.players_in_room)), self.mud)
            #echo("v: {}".format(self.client.v), self.mud)
            #echo("state: {}".format(self.client.state), self.mud)
        elif cmd == "Room.AddPlayer":
            # GMCP! cmd: Room.AddPlayer value: {'name': 'Miharu', 'fullname': 'Awakened Miharu'} type value: <class 'dict'>
            player = value["name"]
            self.client.v.players_in_room.add(player)
            echo("Players: {}".format(", ".join(self.client.v.players_in_room)), self.mud)
            #echo("+{}".format(value["name"]), self.mud)
        elif cmd == "Room.RemovePlayer":
            # GMCP! cmd: Room.RemovePlayer value: Miharu type value: <class 'str'>
            player = value
            if player not in {"Palleo", "Dirus"}:
                self.client.v.players_in_room.remove(player)
            echo("Players: {}".format(", ".join(self.client.v.players_in_room)), self.mud)
            #echo("-{}".format(value), self.mud)
        elif cmd == "Room.Info":
            # GMCP! cmd: Room.Info value: {'num': 40255, 'name': 'Harbour Way overlooking the ocean', 'desc': "The industrial clamour of the docks fills this boardwalk as it edges Shornwall Isle, supported by great stone pilings mired in the shallow ocean below. Warehouses and other wood buildings stand on the west side of the way, built in all shapes and sizes and painted with cheerful colours from yellow to pale blue and green. Most have shuttered windows facing the open sea to the east, where all that blocks one's view of the horizon is a handrail of taut ropes and the masts of ships as they move in and out of the harbour area.", 'area': 'Targossas', 'environment': 'Urban', 'coords': '271,56,3,-1', 'map': 'www.achaea.com/irex/maps/clientmap.php?map=271&building=0&level=-1 29 5', 'details': [], 'exits': {'se': 40218, 's': 41466, 'w': 40766, 'nw': 40149}} type value: <class 'dict'>
            # check to see if we've moved into a new room:
            if self.client.v.room["num"] != value["num"]:
                # if we have, at least reset the number of rats killed in the room
                self.client.v.rats_killed_in_room = 0
                # start the timer stating that we haven't seen rats in the room
                self.client.v.rat_last_seen = datetime.now()
            self.client.v.room.update(value)
        elif cmd == "Char.Vitals":
            # GMCP! cmd: Char.Vitals value: {'hp': '3300', 'maxhp': '3300', 'mp': '3994', 'maxmp': '4372', 'ep': '15400', 'maxep': '15400', 'wp': '18775', 'maxwp': '18775', 'nl': '2', 'bal': '1', 'eq': '1', 'string': 'H:3300/3300 M:3994/4372 E:15400/15400 W:18775/18775 NL:2/100 ', 'charstats': ['Bleed: 0', 'Rage: 0', 'Karma: 45%', 'Entity: Yes']} type value: <class 'dict'>
            #echo("GMCP! cmd: {} value: {} type value: {}".format(cmd, value, type(value)), self.mud)
            bal = value.get("bal", "0")
            self.client.v.bal = True if bal == "1" else False

            eq = value.get("eq", "0")
            self.client.v.eq = True if eq == "1" else False

            #if self.client.v.ratting:
            #    rat(self.client, [])
        elif cmd == "Char.Status":
            # GMCP! cmd: Char.Status value: {'gold': '1915'} type value: <class 'dict'>
            pass
        else:
            print("GMCP! cmd: {} value: {} type value: {}".format(cmd, value, type(value)))

    def trigger(self, raw, stripped):
        #print("this might be the trigger function that can replace lines")
        if re.match("^.* is tormented by horrific visions from the Plane of Chaos.$", stripped):
            return ""
    """
    """

    def getAliases(self):
        print("loading Achaea aliases")
        aliases = {
                    "^m$": attack,
                    "^t (.*)$": target,
                }
        #aliases.update(occultism_aliases)
        #aliases.update(tarot_aliases)
        #aliases.update(domination_aliases)
        aliases.update(spirituality_aliases)
        aliases.update(devotion_aliases)
        aliases.update(healing_aliases)
        aliases.update(tattoo_aliases)
        aliases.update(battlerage_aliases)
        aliases.update(aff_healing_aliases)
        aliases.update(elixirs_aliases)
        aliases.update(salves_aliases)
        aliases.update(pipes_aliases)
        aliases.update(misc_aliases)
        aliases.update(direction_aliases)
        aliases.update(mapping_aliases)
        aliases.update(anti_theft_aliases)
        aliases.update(sigil_aliases)
        return aliases

    def getTriggers(self):
        triggers = {
                    "^You see exits leading (.*)\.$" : exits,
                    "^\(.*\): .* says?, \".*\"$" : says,
                    "^.* says?, \".*\"$" : says,
                    "^You have slain (.*), retrieving the corpse.$" : slain,
                    #"^You rub your hands together greedily.$" : 
                    "^You remove a steel suit of splintmail.$" : lambda client,_: client.send("wear splintmail"),
                    "^You cease wielding a spiritual mace in your .* hand\.$" : lambda client,_: client.send("wield mace"),
                    "^You cease wielding a splendid Targossian kite shield in your right hand." : lambda client,_: client.send("wield shield"),
                    "^You remove a canvas backpack." : lambda client,_: client.send("wear backpack"),
                }
        triggers.update(shown_map_triggers)
        return triggers

def getClass():
    return Achaea

