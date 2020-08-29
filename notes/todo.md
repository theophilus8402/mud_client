* < > room stuff
    * storing notes in notes/mapping.md
    * <x> store every room I enter into a db
    * < > exploring
        * < > find every room in that area
        * < > of those rooms, check all the exits/rooms they touch
                have we been to all those rooms?
        * < > if not, go to those rooms
    * < > pathing
        * < > path area/room/person, go
            * < > locate that area/room/person
            * < > find the best path there
            * < > walk there
    * < > ratting
        * < > have a pre-determined route? and follow it
        * < > kill stuff
        * < > move on
    * < > bashing
        * < > follow route
        * < > kill stuff
        * < > don't die
            * < > values of dangers for mobs, if too dangerous, move on
* <x> make it so that logging in by different characters will load
    different modules
    * ["2020/04/17 10:48:00.129817", "gmcp_data", "{\"type\": \"Char.Name\", \"data\": {\"name\": \"Vindiconis\", \"fullname\": \"Sentry Vindiconis\"}}"]
* < > change loaded modules based on class
    * < > have something that tracks class being used between restarts
        * < > probably a file that keeps track of some of the state
    * < > be able to load and unload triggers/aliases/timers...
        without having to restart the program
* sarmenti
    * <x> finish tasks
    * < > hr3
        * <x> join the army (lord marshal or aide to war)
        * <x> hhelp mentors (mizik?)
                saibel, davok, umaiar, nbige, syndra
        * < > allies to mhaldor
        * < > chelp eidolons, help font
        * < > refill the font some
        * < > learn about distrinnith sect (rituals, sermons...)
        * < > jagganeth sect, class skills
        * < > khovroth sect
        * < > intro to combat
    * <x> get shimmering orb
    * < > more minerals
    * <x> fix defence for deathsight
    * <x> learning
        * <x> tarot hangedman
    * < > pranks
        * < > make aliases
            * <x> mb con, mb web, mb ...
            * <x> mb (shows a quick summary of all bombs)
        * < > get materials for bombs
        * <x> get daggers
        * < > try things!
    * < > hunting
        * < > greatrock, bopalopia, xhaiden dale wildlife + monks
                ganeve hidden in xhaiden dale's grotto
        * < > creville
        * < > 4k hp tomacula, bitterfork, darkenwood,
                rhodestrian, aeraithean (walk to lordar)
        * < > 5k hp meropis
* fix logging being printed to the screen sometimes
* < > clean up defences.py
    * <x> might be able to change it so achaea's auto curing
        can keep up my defences
    * <x> so my aliases would be to just add and remove defs to the
        list of defences the curing system should keep up
* fix up tab completing
    * prioritize targets at least a lil better
* state
    * <x> s.mobs_in_room -> tuple
    * <x> s.defences -> tuple
    * < > s.wanted_defences -> tuple
    * < > s.enemies -> tuple
    * < > s.new_afflictions -> tuple
    * < > s.cured_afflictions -> tuple
    * < > s.current_afflictions -> tuple
        * might be able to get rid of new and cured with this tuple stuff
