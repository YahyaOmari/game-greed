from game_of_greed import __version__
from game_of_greed.game import Game


def test_version():
    assert __version__ == '0.1.0'

def test_rolling_dice_length():
    actual = len(Game.roll_dice(6))
    expected = 6
    assert actual == expected

def test_rolling_dice_sequence():
    actual = Game.roll_dice(6)
    
    for key in actual:
        assert key in range(1, 7)