import pytest
from tape import Tape, Direction


@pytest.fixture
def empty_tape():
    return Tape('', '|')


@pytest.fixture
def invalid_tape():
    return Tape('|||', '')


@pytest.fixture
def valid_tape():
    return Tape('|||', '|')


def test_empty_tape(empty_tape):
    assert is_empty(empty_tape.get_tape())


def test_invalid_tape(invalid_tape):
    assert is_empty(invalid_tape.get_tape())


def test_valid_tape(valid_tape):
    assert valid_tape.get_tape() == '$|||#'


def test_write_valid_character(empty_tape):
    empty_tape.head_position = 1
    empty_tape.write('|')

    assert empty_tape.get_tape() == '$|'


def test_write_invalid_character(empty_tape):
    empty_tape.head_position = 1
    empty_tape.write('b')

    assert is_empty(empty_tape.get_tape())


def test_write_valid_character_at_invalid_position(empty_tape):
    empty_tape.write('|')

    assert is_empty(empty_tape.get_tape())


def test_read_at_invalid_position(empty_tape):
    with pytest.raises(Exception):
        empty_tape.head_position = -1
        character = empty_tape.read()


def test_read_at_valid_position(empty_tape):
    first_char = empty_tape.read()
    empty_tape.head_position += 1
    second_char = empty_tape.read()

    assert first_char == '$'
    assert second_char == '#'


def is_empty(tape):
    return tape == '$#'