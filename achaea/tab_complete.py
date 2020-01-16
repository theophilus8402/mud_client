
import readline
import logging

from itertools import chain

LOG_FILENAME = 'completer.log'
logging.basicConfig(
    format='%(message)s',
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)


class SimpleCompleter:

    def __init__(self, players, mobs, enemies):
        self._players_in_room = players
        self._mobs_in_room = mobs
        self._enemies = enemies

    def complete(self, text, state):
        print(f"Trying to tab complete: {text} {state}")
        print(f"mobs: {self._mobs_in_room} id: {id(self._mobs_in_room)}")
        logging.debug(f"complete - text: {text}, state: {state}")
        response = None
        # if the first word/command has not been given, return no matches
        #words = text.split()
        #if len(words) <= 1:
        #    return None

        # for now, we're just going to assume the next target is what we're
        #   trying to tab complete
        # the order of prority is: enemies > mobs (not guards) > other players
        #   to be an option, the target must been in the room at the moment
        # todo: what do I do about the list having been updated???
        #   just let the user "start" over?  which should just be editing the
        #   text for the target
        if state == 0:
            # This is the first time for this text,
            # so build a match list.
            if text:
                #print(self._players_in_room)
                #print(self._mobs_in_room)
                #print(self._enemies)
                #print(self.get_sorted_options())
                self.matches = [
                    s
                    for s in self.get_sorted_options()
                    if s and s.startswith(text)
                ]
                logging.debug(f'{repr(text)} matches: {self.matches}')
            else:
                self.matches = self.get_sorted_options()
                logging.debug(f'(empty input) matches: {self.matches}')

        # Return the state'th item from the match list,
        # if we have that many.
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        logging.debug(f'complete({repr(text)}, {state}) => {repr(response)}')
        return response

    def get_sorted_options(self):
        enemies_in_room = self._players_in_room.intersection(self._enemies)
        other_players = self._players_in_room.difference(self._enemies)
        logging.debug(f"others: {other_players}")
        logging.debug(f"enemies_in_room: {enemies_in_room}")
        logging.debug(f"mobs_in_room: {self._mobs_in_room}")
        options = list(chain.from_iterable([enemies_in_room,
                                        self._mobs_in_room,
                                        other_players]))
        logging.debug(f"options: {options}")
        return options

def input_loop():
    line = ''
    while line != 'stop':
        line = input('Prompt ("stop" to quit): ')
        print('Dispatch {}'.format(line))


# Register the completer function
#players = {"billy", "theo", "dirus"}
#mobs = {"rat1", "orc", "rat2", "turkey"}
#enemies = {"theo", "billy"}
#readline.set_completer(SimpleCompleter(players, mobs, enemies).complete)

# Use the tab key for completion
#readline.parse_and_bind('tab: complete')

# Prompt the user for text
#input_loop()

