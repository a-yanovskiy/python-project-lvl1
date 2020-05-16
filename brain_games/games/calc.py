"""
Игра: "Калькулятор".

Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число четное, или no - если нечетное.
"""

from random import randint, choice


game_rules = 'What is the result of the expression?.\n'



def question():
    first_digit = randint(0, 100)  # noqa: S311
    second_digit = randint(0, 100)  # noqa: S311
    sigh = choice('+' + '-' + '*')
    return str(first_digit) + sigh + str(second_digit)


def answer(question):               # проверяет рандомное число на четность
    """Parity of random digit.

    Parameters:
        digit: argument, which must be check for parity.

    Returns:
        'yes' or 'no': string.
    """
    answer = str(eval(question))
    return answer
