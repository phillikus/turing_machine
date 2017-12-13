import unary_tms


def test_increment_unary():
    tm = unary_tms.increment('|||')
    tm.process()
    assert tm.get_tape() == "$||||#"


def test_increment_unary_empty_tape():
    tm = unary_tms.increment('')
    tm.process()
    assert tm.get_tape() == "$|#"


def test_decrement_unary():
    tm = unary_tms.decrement('|||')
    tm.process()
    assert tm.get_tape() == "$||#"


def test_decrement_unary_empty_tape():
    tm = unary_tms.decrement('')
    tm.process()
    assert tm.get_tape() == "$#"


def test_add_unary():
    tm = unary_tms.add('|||&||')
    tm.process()
    assert tm.get_tape() == "$|||||#"


def test_add_unary_empty_tape():
    tm = unary_tms.add('', True)
    tm.process()
    assert tm.get_tape() == "$#"


def test_subtract_unary():
    tm = unary_tms.subtract('|||#||')
    tm.process()
    assert tm.get_tape() == "$|#"


def test_subtract_unary_empty_tape():
    tm = unary_tms.subtract('', True)
    tm.process()
    assert tm.get_tape() == "$#"

