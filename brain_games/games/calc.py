"""
Игра: "Калькулятор".

Пользователю показывается случайное математическое выражение,
которое нужно вычислить и записать правильный ответ.
"""

from random import choice, randint

GAME_RULES = 'What is the result of the expression?.\n'


def set_question():
    """Question.

    Returns:
        Question: string.
    """
    first_digit = randint(1, 100)  # noqa: S311
    second_digit = randint(1, 100)  # noqa: S311
    sigh = choice('{0}{1}{2}'.format('+', '-', '*'))  # noqa: S311
    return str(first_digit) + sigh + str(second_digit), None  # question_list


def get_answer(question_list):
    """Calculate set_question().

    Parameters:
        question_list: argument from set_question()

    Returns:
        Right answer.
    """
    return str(eval(question_list[0]))  # noqa: WPS421, S307
