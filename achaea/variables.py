
from .client import add_temp_trigger, remove_temp_trigger

class Variable():

    def __init__(self):
        self.target = "rat"
        add_temp_trigger("target_trigger", ("target_trigger", lambda m: False))

v = Variable()

