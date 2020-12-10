import logging
from logging import NOTSET, Logger, addLevelName, setLoggerClass

# verbose logger:
#     this is a very different beast
#     format is different:
#         json.dump the stuff so it's in a good format for me to parse
#     want extra context to know from where we got the message
#     want the time the msg was received
#     this is unmodified data... this helps with running through the triggers/aliases
#         later to test things
# says logger:
#     just says... very simple
# fighting logger:
#     says (so this would be an example of sending a feed to another logger or another level...)
#         maybe I could filter it even more (at times) to just the party channel
#     fighting stuff
#     deaths
#     movement
#     afflictions
#     echos/reminders
#     should try to color things appropriately
# party logger:
#     this will be a level and a handler
#     announce things to the party channel
#     I can have an alias that turns this on and off
#     targetting
#     target movement
#     different affs I give
#     this gets fed to the fighting/brief logger
#     party handler:
#         set to NOTHING initially
#         alias can change on and off to PARTY
#         filter will only let PARTY level logs go to the handler
#         will send stuff to the party
# main visual logger:
#     this has all the normal text
#     some stuff will be filtered out / modified


FIGHTING = 5
PARTY = 7
SAYS = 15
MAIN = 25
ECHO = 27
NOTHING = 65


class AchaeaLogger(Logger):
    def __init__(self, name, level=NOTSET):
        super().__init__(name, level)

        addLevelName(FIGHTING, "FIGHTING")
        addLevelName(PARTY, "PARTY")
        addLevelName(SAYS, "SAYS")
        addLevelName(MAIN, "MAIN")
        addLevelName(NOTHING, "NOTHING")

    def fighting(self, msg, *args, **kwargs):
        if self.isEnabledFor(FIGHTING):
            self._log(FIGHTING, msg, args, **kwargs)

    def party(self, msg, *args, **kwargs):
        if self.isEnabledFor(PARTY):
            self._log(PARTY, msg, args, **kwargs)

    def says(self, msg, *args, **kwargs):
        if self.isEnabledFor(SAYS):
            self._log(SAYS, msg, args, **kwargs)

    def main(self, msg, *args, **kwargs):
        if self.isEnabledFor(MAIN):
            self._log(MAIN, msg, args, **kwargs)

    def echo(self, msg, *args, **kwargs):
        if self.isEnabledFor(ECHO):
            self._log(ECHO, msg, args, **kwargs)


setLoggerClass(AchaeaLogger)


class SaysFilter(logging.Filter):
    def filter(self, record):
        if record.levelno == SAYS:
            return True
        else:
            return False


class FightingFilter(logging.Filter):

    approved_levels = [FIGHTING, SAYS, PARTY]

    def filter(self, record):
        if record.levelno in FightingFilter.approved_levels:
            return True
        else:
            return False


def initialize_logging():

    says_log_path = "says.log"
    says_handler = logging.FileHandler(says_log_path, mode="a")
    says_handler.setLevel(SAYS)
    says_filter = SaysFilter()
    says_handler.addFilter(says_filter)

    fighting_log_path = "fighting.log"
    fighting_handler = logging.FileHandler(fighting_log_path, mode="a")
    fighting_handler.setLevel(FIGHTING)
    fighting_filter = FightingFilter()
    fighting_handler.addFilter(fighting_filter)

    log = logging.getLogger("achaea")
    log.setLevel(FIGHTING)
    log.addHandler(fighting_handler)
    log.addHandler(says_handler)


def switch_to_fighting_log():
    pass


def switch_from_fighting_log():
    pass


if __name__ == "__main__":

    log = logging.getLogger("achaea")
    # log.says("Billy said something.")
    # log.fighting("Tim hit Tom!")
    # log.main("Something normal.")

    """
    logging.addLevelName(60, SAYS)
    log.warning("Hello, World!")
    log.says("Tim said something!")
    """
