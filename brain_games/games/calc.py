"""
Игра: "Калькулятор".

Пользователю показывается случайное математическое выражение,
которое нужно вычислить и записать правильный ответ.
"""

import operator
from random import choice, randint

GAME_DESCRIPTION = 'What is the result of the expression?.'


def generate_game_data():
    """Question.

    Returns:
        Question: string.
    """
    first_digit = randint(1, 100)
    second_digit = randint(1, 100)
    sighs = ['+', '-', '*']
    choice_sigh = choice(sighs)
    if choice_sigh == '+':
        answer = operator.add(first_digit, second_digit)
    elif choice_sigh == '-':
        answer = operator.sub(first_digit, second_digit)
    elif choice_sigh == '*':
        answer = operator.mul(first_digit, second_digit)
    question = '{0} {1} {2}'.format(first_digit, choice_sigh, second_digit)
    return question, str(answer)
