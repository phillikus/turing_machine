from state import State, StateType
from transition import Transition
from direction import Direction
from tape import Tape


class TuringMachine:
    def __init__(self, states, transitions, tape, verbose=False):
        self.states = states
        self.start_state = self.get_start_state()
        self.transitions = transitions
        self.tape = tape
        self.verbose = verbose

    def get_tape(self):
        return self.tape.get_tape()

    def get_start_state(self):
        return next(state for state in self.states if state.type == StateType.Start)

    def process(self, verbose=False):
        current_state = self.start_state
        step = 0

        self._log_process(step)

        while current_state.type != StateType.Final:
            current_char = self.tape.read()
            state_id = current_state.id

            transition = next(t for t in self.transitions
                              if t.current_state == state_id
                              and t.current_char == current_char)

            current_state = next(state for state in self.states if state.id == transition.new_state)

            step += 1
            self.tape.write(transition.new_char)
            self.tape.move_head(transition.direction)
            self._log_process(step)

    def _log_process(self, step):
        if self.verbose is True:
            print('\nTape after step {0}: '.format(step))
            print('[', end='')

            for i in range(0, self.tape.get_length()):
                if self.tape.head_position == i:
                    print("\033[4m" + self.tape._tape[i] + "\033[0m", end='')
                else:
                    print(self.tape._tape[i], end='')

            print(']')

