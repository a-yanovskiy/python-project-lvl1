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
    first_digit = randint(1, 100)  # noqa: S311
    second_digit = randint(1, 100)  # noqa: S311
    sigh = choice('{0}{1}{2}'.format('+', '-', '*'))  # noqa: S311
    return str(first_digit) + sigh + str(second_digit), None


def answer(question_list):
    """Right answer.

    Parameters:
        question_to_user: argument from question()

    Returns:
        Right answer.
    """
    # получаем значения из входного списка
    from_question = question_list[0]
    return str(eval(from_question))  # noqa: WPS421, S307
