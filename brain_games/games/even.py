"""
Игра: "Проверка на четность".

Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число четное, или no - если нечетное.
"""

from random import randint

GAME_RULES = 'Answer "yes" if number even otherwise answer "no".\n'


def game_logic():
    """Random digit from 1 to 100.

    Returns:
        Random digit from 1 to 100.
    """
    question = randint(1, 100) # noqa: S311
    answer = ''
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
