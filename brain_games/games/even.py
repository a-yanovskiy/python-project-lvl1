"""
Игра: "Проверка на четность".

Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число четное, или no - если нечетное.
"""

from random import randint

game_rules = 'Answer "yes" if number even otherwise answer "no".\n'


def question():
    """Random digit from 1 to 100.

    Returns:
        Random digit from 1 to 100.
    """
    return randint(1, 100), None  # noqa: S311


def answer(question_list):  # проверяет рандомное число на четность
    """Parity of random digit.

    Parameters:
        question_list: argument from question().

    Returns:
        'yes' or 'no': string.
    """
    # получаем значения из входного списка
    from_question = question_list[0]

    ans = ''
    if from_question % 2 == 0:
        ans = 'yes'
    else:
        ans = 'no'
    return ans
