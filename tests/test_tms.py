import tms
import pytest


def test_increment():
    tm = tms.increment('|||')
    tm.process()
    assert tm.get_tape() == "$||||#"


def test_increment_empty_tape():
    tm = tms.increment('')
    tm.process()
    assert tm.get_tape() == "$|#"
