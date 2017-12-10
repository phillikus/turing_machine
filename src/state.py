from enum import Enum


class StateType(Enum):
    Start = 1
    Final = 2
    Empty = 3


class State:
    def __init__(self, id, state_type):
        self.id = id
        self.type = state_type
