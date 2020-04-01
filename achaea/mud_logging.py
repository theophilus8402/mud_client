
"""
verbose logger:
    this is a very different beast
    format is different:
        json.dump the stuff so it's in a good format for me to parse
    want extra context to know from where we got the message
    want the time the msg was received
    this is unmodified data... this helps with running through the triggers/aliases
        later to test things
says logger:
    just says... very simple
fighting logger:
    says (so this would be an example of sending a feed to another logger or another level...)
        maybe I could filter it even more (at times) to just the party channel
    fighting stuff
    deaths
    movement
    afflictions
    echos/reminders
main visual logger:
    this has all the normal text
    some stuff will be filtered out / modified
"""
