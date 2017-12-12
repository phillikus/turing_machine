from state import State, StateType
from transition import Transition
from direction import Direction
from tape import Tape


class TuringMachine:
    def __init__(self, states, transitions, tape):
        self.states = states
        self.start_state = self.get_start_state()
        self.transitions = transitions
        self.tape = tape

    def get_tape(self):
        return self.tape.get_tape()

    def get_start_state(self):
        return next(state for state in self.states if state.type == StateType.Start)

    def process(self):
        current_state = self.start_state

        while current_state.type != StateType.Final:
            current_char = self.tape.read()
            state_id = current_state.id

            transition = next(t for t in self.transitions
                              if t.current_state == state_id
                              and t.current_char == current_char)

            current_state = next(state for state in self.states if state.id == transition.new_state)
            current_char = transition.new_char

            self.tape.write(current_char)
            self.tape.move_head(transition.direction)
