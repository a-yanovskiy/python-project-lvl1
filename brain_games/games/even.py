"""
Игра: "Проверка на четность".

Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число четное, или no - если нечетное.
"""

from random import randint


game_rules = 'Answer "yes" if number even otherwise answer "no".\n'



def question():
    random_digit = randint(0, 100)  # noqa: S311
    return random_digit


def answer(question):               # проверяет рандомное число на четность
    """Parity of random digit.

    Parameters:
        digit: argument, which must be check for parity.

    Returns:
        'yes' or 'no': string.
    """
    answer = ''
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer
