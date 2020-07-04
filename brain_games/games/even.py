"""
Игра: "Проверка на четность".

Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число четное, или no - если нечетное.
"""

from random import randint

description = 'Answer "yes" if number even otherwise answer "no".'


def set_game_logic():
    """Logic for Brain-even game.

    Returns:
        question, answer.
    """
    question = randint(1, 100)  # noqa: S311
    return question, 'yes' if question % 2 == 0 else 'no'
