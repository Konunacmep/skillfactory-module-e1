import game
import pytest

@pytest.fixture()
def some_choices():
    return ['black', 'box']

@pytest.fixture()
def data_for_test():
    return 'black', '_ _ _ _ _ '

@pytest.fixture()
def try_game():
    game.CHOICES = ['black']

import builtins
input_values = ['c', 'k', 'g', '22', 'f', 'a', 'l', 'b']

def mock_input(s):
    return input_values.pop(0)

@pytest.fixture()
def set_keyboard_input():
    builtins.input = mock_input