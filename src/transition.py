from state import State


class Transition:
    def __init__(self, current_state, current_char, new_state, new_char, direction):
        self.current_state = current_state
        self.current_char = current_char
        self.new_state = new_state
        self.new_char = new_char
        self.direction = direction
