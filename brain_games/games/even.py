"""
Игра: "Проверка на четность".

Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число четное, или no - если нечетное.
"""

from random import randint

description = 'Answer "yes" if number even otherwise answer "no".'


def is_even(digit):
    """Take digit, if even returns True.

    Parameters:
        digit: Integer.

    Returns:
        True or False
    """
    return True if digit % 2 == 0 else False


def set_game_logic():
    """Logic for Brain-even game.

    Returns:
        question, answer.
    """
    question = randint(1, 100)
    answer = is_even(question)
    return question, answer
