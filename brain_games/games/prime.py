"""
Игра "Простое ли число?".

Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число простое,
или no - если число не является простым.
"""

from random import randint

game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'


def question():
    """Random digit from 1 to 100.

    Returns:
        Random digit from 1 to 100.
    """
    return randint(1, 100), None  # noqa: S311


def answer(question_list):
    """Prime of random digit.

    Parameters:
        question_list: argument from question().

    Returns:
        'yes' or 'no': string.
    """
    from_question = question_list[0]

    ans = 'yes'
    divider = from_question - 1
    while divider > 1:
        if from_question % divider == 0:
            ans = 'no'
            break
        else:
            divider -= 1
    return ans
