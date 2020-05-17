"""
Игра: "Калькулятор".

Пользователю показывается случайное математическое выражение,
которое нужно вычислить и записать правильный ответ.
"""

from random import choice, randint

game_rules = 'What is the result of the expression?.\n'


def question():
    """Question.

    Returns:
        Question: string.
    """
    first_digit = randint(0, 100)  # noqa: S311
    second_digit = randint(0, 100)  # noqa: S311
    sigh = choice('{0}{1}{2}'.format('+', '-', '*'))  # noqa: S311
    return str(first_digit) + sigh + str(second_digit)


def answer(question_to_user):
    """Right answer.

    Parameters:
        question_to_user: argument from question()

    Returns:
        Right answer.
    """
    return str(eval(question_to_user))  # noqa: WPS421, S307
