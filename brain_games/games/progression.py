"""
Игра "Арифметическая прогрессия".

Игроку показывается ряд чисел, образующий арифметическую прогрессию,
заменив любое из чисел двумя точками. Игрок должен определить это число.
"""

from random import randint

game_rules = 'What number is missing in the progression?\n'


def logic():
    digit = randint(1, 10)
    step = randint(1, 10)  # увеличить для усложнения
    skip = randint(0, 9)
    question_list = ''
    for i in range(10):
        if i == skip:
            question_list = question_list + '.. '
            skiped_digit = digit
            digit += step
        question_list = question_list + str(digit) + ' '
        digit += step
    return question_list, skiped_digit


def question():
    """Question.

    Returns:
        Question: string.
    """
    question_list, skiped_digit = logic()
    return question_list, skiped_digit


def answer(question_list):
    """Right answer.

    Parameters:
        quest: argument question() returns

    Returns:
        Right answer.
    """
    # получаем значения из входного списка
    skiped_digit = question_list[1]
    return str(skiped_digit)
