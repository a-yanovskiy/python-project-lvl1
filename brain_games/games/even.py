"""
Игра: "Проверка на четность".

Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число четное, или no - если нечетное.
"""

from random import randint

game_rules = 'Answer "yes" if number even otherwise answer "no".\n'


def question():
    """Random digit from 0 to 100.

    Returns:
        Random digit from 0 to 100.
    """
    return randint(0, 100)  # noqa: S311


def answer(question_to_user):  # проверяет рандомное число на четность
    """Parity of random digit.

    Parameters:
        question_to_user: argument from question().

    Returns:
        'yes' or 'no': string.
    """
    ans = ''
    if question_to_user % 2 == 0:
        ans = 'yes'
    else:
        ans = 'no'
    return ans
