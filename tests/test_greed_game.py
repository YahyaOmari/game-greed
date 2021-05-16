from game_of_greed import __version__
from game_of_greed.game import GameLogic


def test_version():
    assert __version__ == '0.1.0'

def test_rolling_dice_length():
    actual = len(GameLogic.roll_dice())
    expected = 6
    assert actual == expected

def test_rolling_dice_sequence():
    actual = GameLogic.roll_dice()
    
    for key in actual:
        assert key in range(1, 6)