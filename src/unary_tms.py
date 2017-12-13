from turing_machine import TuringMachine
from state import State, StateType
from transition import Transition
from direction import Direction
from tape import Tape


def increment(word, verbose=False):
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

    return TuringMachine(states, transitions, tape, verbose)


def decrement(word, verbose=False):
    tape = Tape(word, '|')
    states = [
                State("s0", StateType.Start),
                State("s1", StateType.Empty),
                State("s2", StateType.Empty),
                State("sf", StateType.Final)
             ]

    transitions = [
                     Transition("s0", "$", "s1", "$", Direction.Right),
                     Transition("s1", "|", "s1", "|", Direction.Right),
                     Transition("s1", "#", "s2", "#", Direction.Left),
                     Transition("s2", "$", "sf", "$", Direction.Neutral),
                     Transition("s2", "|", "sf", "#", Direction.Neutral)
                  ]

    return TuringMachine(states, transitions, tape, verbose)


def add(word, verbose=False):
    tape = Tape(word, '|&')
    states = [
                State("s0", StateType.Start),
                State("s1", StateType.Empty),
                State("s2", StateType.Empty),
                State("s3", StateType.Empty),
                State("s4", StateType.Empty),
                State("sf", StateType.Final)
             ]

    transitions = [
                     Transition("s0", "$", "s1", "$", Direction.Right),
                     Transition("s1", "#", "sf", "#", Direction.Neutral),
                     Transition("s1", "|", "s1", "|", Direction.Right),
                     Transition("s1", "&", "s2", "|", Direction.Right),
                     Transition("s2", "|", "s2", "|", Direction.Right),
                     Transition("s2", "#", "s3", "#", Direction.Left),
                     Transition("s3", "|", "s4", "#", Direction.Left),
                     Transition("s4", "|", "s4", "|", Direction.Left),
                     Transition("s4", "$", "sf", "$", Direction.Neutral),
                  ]

    return TuringMachine(states, transitions, tape, verbose)


def subtract(word, verbose=False):
    tape = Tape(word, '|&')
    states = [
                State("s0", StateType.Start),
                State("s1", StateType.Empty),
                State("s2", StateType.Empty),
                State("s3", StateType.Empty),
                State("s4", StateType.Empty),
                State("s5", StateType.Empty),
                State("s6", StateType.Empty),
                State("s7", StateType.Empty),
                State("s8", StateType.Empty),
                State("sf", StateType.Final)
             ]

    transitions = [
                     Transition("s0", "$", "s0", "$", Direction.Right),
                     Transition("s0", "#", "sf", "#", Direction.Neutral),
                     Transition("s0", "|", "s1", "|", Direction.Right),
                     Transition("s1", "|", "s1", "|", Direction.Right),
                     Transition("s1", "#", "s2", "#", Direction.Right),
                     Transition("s2", "#", "s2", "#", Direction.Right),
                     Transition("s2", "|", "s3", "|", Direction.Right),
                     Transition("s3", "|", "s4", "|", Direction.Left),
                     Transition("s3", "#", "s6", "#", Direction.Left),
                     Transition("s4", "|", "s5", "#", Direction.Left),
                     Transition("s5", "#", "s5", "#", Direction.Left),
                     Transition("s5", "|", "s2", "#", Direction.Right),
                     Transition("s5", "$", "s2", "$", Direction.Right),
                     Transition("s6", "|", "s7", "#", Direction.Left),
                     Transition("s7", "#", "s7", "#", Direction.Left),
                     Transition("s7", "$", "sf", "$", Direction.Neutral),
                     Transition("s7", "|", "s8", "#", Direction.Left),
                     Transition("s8", "|", "s8", "|", Direction.Left),
                     Transition("s8", "$", "sf", "$", Direction.Neutral)
                  ]

    return TuringMachine(states, transitions, tape, verbose)