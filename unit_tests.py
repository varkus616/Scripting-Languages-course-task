from game_modules import *
import pytest


@pytest.mark.parametrize("test_input,expected",
                         [("prawo", True),
                          ("lewo", True),
                          ("moc", True),
                          ("koks", False),
                          ("wojtek", True),
                          ("herbata", False)
                          ])
def test_validator(test_input, expected):
    validator = Validator()
    assert validator.check_word(test_input) == expected


@pytest.mark.parametrize("user_guess,word,expected",
                         [
                             ('abr', "koktajl", (0, 1)),
                             ('bryka', "pomidor", (0, 1)),
                             ('myka', "rybator", (2, 0)),
                             ('mord', "morderstwo", (4,0)),
                             ('wampir', "wampir", (6,0)),
                             ('trol', "peoltr", (2,2))
                         ])
def test_check_user_word(user_guess, word, expected):
    engine = Engine()
    stats = Stats()
    assert engine.check_user_word(stats, user_guess, word) == expected


@pytest.mark.parametrize("bulls,word,expected",
                         [
                             (4, "ogor", True),
                             (3, "modliszka", False),
                             (6, "rebacz", True),
                             (11, "drewno", False),
                             (4, "roki", True),
                             (9, "mrok", False),
                             (19, "konstantynopolitanczykowianeczka", False),
                             (2, "cos", False),
                             (4, "Leki", True)
                         ])
def test_guess_conditions(bulls, word, expected):
    engine = Engine()
    stats = Stats()
    stats.bulls = bulls
    stats.cows = 0
    ret_val, cows = engine.check_guess_conditions(stats, word)
    assert ret_val == expected
