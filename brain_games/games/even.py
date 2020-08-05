"""
Игра: "Проверка на четность".

Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число четное, или no - если нечетное.
"""

from brain_games import game_adds
from random import randint

GAME_DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(digit):
    """Take digit, if even returns True.

    Parameters:
        digit: Integer.

    Returns:
        True or False
    """
    return digit % 2 == 0


def generate_game_data():
    """Logic for Brain-even game.

    Returns:
        question, answer.
    """
    question = randint(1, 100)
    answer = game_adds.tellme_yes_or_no(is_even(question))
    return question, answer
