"""
Игра "Простое ли число?".

Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число простое,
или no - если число не является простым.
"""

from random import randint

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'


def game_logic():
    """Prime of random digit.

    Parameters:
        question_list: argument from set_question().

    Returns:
        'yes' or 'no': string.
    """
    question = randint(1, 100)  # noqa: S311
    answer = 'yes'
    divider = question - 1
    while divider > 1:
        if question % divider == 0:
            answer = 'no'
            break
        else:
            divider -= 1
    return question, answer
