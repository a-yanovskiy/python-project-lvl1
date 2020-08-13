"""
Игра: "Проверка на четность".

Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число четное, или no - если нечетное.
"""

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
    answer = 'yes' if is_even(question) else 'no'
    return question, answer
