import game
import pytest
from mock_input import set_keyboard_input

# Проверяем, что функция выдает слово из списка
def test_initialize_picks_word(some_choices):
    result_initial_word = game.initialize(some_choices)
    assert [True for x in some_choices if x == result_initial_word[0]]

# проверяем, что функция создает шаблон для слова, в два раза его длиннее, т.е. после каждой _ добавляется пробел
def test_initialize_makes_proper_template_length(some_choices):
    result_initial_word = game.initialize(some_choices)
    assert [True for x in some_choices if len(x)*2 == len(result_initial_word[1])]

# проверяем, что шаблон состоит из "_ "
def test_initialize_makes_proper_template_filling(some_choices):
    result_initial_word = game.initialize(some_choices)
    assert result_initial_word[1].replace('_ ', '') == ''

# проверим, как идет поиск букв в словах
@pytest.mark.parametrize('letter, result', [('a', '_ _ a _ _ '), ('b', 'b _ _ _ _ '), ('d', None)])
def test_check_letter_no_exists(data_for_test, letter, result):
    assert game.check_letter(*data_for_test, letter) == result

# удостоверимся, что функция принимает только одну букву
@pytest.mark.parametrize('letter, result', [('a', 'a'), ('ab', None), ('1', None), ('a1', None)])
def test_evaluate_input(letter, result):
    assert game.evaluate_input(letter) == result

# верно ли вычисляется победа. функция должна сопоставить, что "black" и "b l a c k " - одно слово
def test_victoty_win():
    assert game.victory('black', 'b l a c k ')

# проверим и противоположную ситуацию
@pytest.mark.xfail()
def test_victoty_not_win():
    assert game.victory('black', '_ _ a c k ')

# попробуем имитировать пользователя и поиграть в игру, выиграв (слово black)
def test_game_win(try_game):
    set_keyboard_input(['c', 'k', 'g', '22', 'f', 'a', 'l', 'b'])
    assert game.game()

# попробуем имитировать пользователя и поиграть в игру, проиграв
def test_game_lose(try_game):
    set_keyboard_input(['p', 'k', 'g', '22', 'f', 'n', 'l', 'b'])
    assert game.game() is False
