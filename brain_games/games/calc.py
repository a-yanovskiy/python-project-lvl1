"""
Игра: "Калькулятор".

Пользователю показывается случайное математическое выражение,
которое нужно вычислить и записать правильный ответ.
"""

from random import choice, randint


GAME_RULES = 'What is the result of the expression?.\n'


def game_logic():
    """Question.

    Returns:
        Question: string.
    """
    first_digit = randint(1, 100)  # noqa: S311
    second_digit = randint(1, 100)  # noqa: S311
    sigh = ['+', '-', '*']
    choice_sigh = choice(sigh)  # noqa: S311
    if choice_sigh == '+':
        question = '{0} + {1}'.format(first_digit, second_digit)
        answer = first_digit + second_digit
    elif choice_sigh == '-':
        question = '{0} - {1}'.format(first_digit, second_digit)
        answer = first_digit - second_digit
    elif choice_sigh == '*':
        question = '{0} * {1}'.format(first_digit, second_digit)
        answer = first_digit * second_digit
    return question, str(answer)
