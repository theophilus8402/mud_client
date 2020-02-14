
import itertools

from prompt_toolkit.completion import Completer, Completion


class TargetCompleter(Completer):

    def __init__(self, state):
        self.state = state

    def get_completions(self, document, complete_event):
        word = document.get_word_before_cursor()
        #print(f"word: {word}")

        players = self.state.players_in_room
        enemies = self.state.enemies
        mobs = self.state.mobs_in_room
        enemies_in_room = players.intersection(enemies)
        others = players.difference(enemies)

        for ent in itertools.chain(enemies_in_room, mobs, others):
            if ent.lower().startswith(word.lower()):
                yield Completion(
                    ent,
                    start_position=-len(word),
                )
