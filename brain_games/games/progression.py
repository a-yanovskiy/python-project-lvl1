"""
Игра "Арифметическая прогрессия".

Игроку показывается ряд чисел, образующий арифметическую прогрессию,
заменив любое из чисел двумя точками. Игрок должен определить это число.
"""

from random import randint

game_rules = 'What number is missing in the progression?\n'


def logic():  # noqa: WPS210
    """Logic for Progression-game.

    Returns:
        question_list: returns progression list with missed digit
        skiped_digit: missed digit
    """
    digit = randint(1, 10)  # noqa: S311
    step = randint(1, 10)  # noqa: S311
    skip = randint(0, 9)  # noqa: S311
    question_list = ''
    for index in range(10):
        if index == skip:
            question_list = ('{0} .. ').format(question_list)
            skiped_digit = digit
            digit += step
        question_list = ('{0} {1} ').format(question_list, str(digit))
        digit += step
    return question_list, skiped_digit
# нужно было получить из logic() пропущенное число skiped_digit из прогрессии,
# из-за этого пришлось возвращать все question() списками


def question():
    """Question.

    Returns:
        Question: string.
    """
    question_list, skiped_digit = logic()
    return question_list, skiped_digit  # noqa: WPS331


def answer(question_list):
    """Right answer.

    Parameters:
        question_list: argument question() returns

    Returns:
        Right answer.
    """
    # получаем значения из входного списка
    skiped_digit = question_list[1]
    return str(skiped_digit)
