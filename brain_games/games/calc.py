"""
Игра: "Калькулятор".

Пользователю показывается случайное математическое выражение,
которое нужно вычислить и записать правильный ответ.
"""

from random import choice, randint
import operator

description = 'What is the result of the expression?.'


def set_game_logic():  # noqa: WPS210
    """Question.

    Returns:
        Question: string.
    """
    first_digit = randint(1, 100)  # noqa: S311
    second_digit = randint(1, 100)  # noqa: S311
    sighs = ['+', '-', '*']
    choice_sigh = choice(sighs)  # noqa: S311
    if choice_sigh == '+':
        answer = operator.add(first_digit, second_digit)
    elif choice_sigh == '-':
        answer = operator.sub(first_digit, second_digit)
    elif choice_sigh == '*':
        answer = operator.mul(first_digit, second_digit)
    question = '{0} {1} {2}'.format(first_digit, choice_sigh, second_digit)
    return question, str(answer)
