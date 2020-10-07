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
        * < > values of dangers for mobs, if too dangerous, move
* < > change loaded modules based on class
    * < > have something that tracks class being used between restarts
        * < > probably a file that keeps track of some of the state
    * < > be able to load and unload triggers/aliases/timers...
        without having to restart the program
* trigger off tumble and walk in that direction
* sarmenti
    * <x> finish tasks
    * <x> learning
        * < > tarot aeon
    * < > pranks
        * < > make aliases
    * < > hr4
        * < > go to another plane with open pk
        * < > work as a team with someone for combat
    * < > get
        * < > aconite, slike, vernalius
    * < > resolves
        * < > 10 seamonsters?
* < > redirecting map
    * <x> capture the map lines and don't delete the lines
    * < > actually redirect the map to a file?
    * < > integrate it into the ui
* < > fix logging being printed to the screen sometimes
* < > fix up tab completing
    * < > prioritize targets at least a lil better
* < > ui
    * < > show people in the room
        * < > people in the room get cleared when
                someone leaves
    * < > show people/mobs by priorities
    * < > show afflictions
    * < > integrate the main screen into the ui
    * < > make it so pageup/down will scroll the main screen
* < > need to fix this:
  File "/home/veredus/mud_client/achaea/room_info/room_info.py", line 37, in get_room_info
    s.room_info = StateRoomInfo(**gmcp_data)
TypeError: __new__() got an unexpected keyword argument 'ohmap'
* state
    * < > s.enemies -> tuple
    * < > s.new_afflictions -> tuple
    * < > s.cured_afflictions -> tuple
    * < > s.current_afflictions -> tuple
        * might be able to get rid of new and cured with this tuple stuff
* meropis
    * mirror caves (walk to mirrorcaves... awesome money! not that hard)
    * chaghut
    * orilla
    * outside sirocco fortress
    * ulsyndar
    * help geography

