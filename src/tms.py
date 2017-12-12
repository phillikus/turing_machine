from turing_machine import TuringMachine
from state import State, StateType
from transition import Transition
from direction import Direction
from tape import Tape


def increment(word):
    tape = Tape(word, '|')
    states = [
                State("s0", StateType.Start),
                State("s1", StateType.Empty),
                State("sf", StateType.Final)
             ]

    transitions = [
                     Transition("s0", "$", "s1", "$", Direction.Right),
                     Transition("s1", "|", "s1", "|", Direction.Right),
                     Transition("s1", "#", "sf", "|", Direction.Neutral)
                  ]

    return TuringMachine(states, transitions, tape)