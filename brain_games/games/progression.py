"""
Игра "Арифметическая прогрессия".

Игроку показывается ряд чисел, образующий арифметическую прогрессию,
заменив любое из чисел двумя точками. Игрок должен определить это число.
"""

from random import randint

game_rules = 'What number is missing in the progression?\n'


def game_logic():  # noqa: WPS210
    """Logic for Progression-game.

    Returns:
        question: returns progression list with missed digit
        answer: missed digit
    """
    digit = randint(1, 10)  # noqa: S311
    step = randint(1, 10)  # noqa: S311
    skip = randint(0, 9)  # noqa: S311
    question = ''
    number_of_digits_in_progression = 10
    for index in range(number_of_digits_in_progression):
        if index == skip:
            question = ('{0} .. ').format(question)
            answer = digit
            digit += step
        question = ('{0} {1} ').format(question, str(digit))
        digit += step
    return question, str(answer)
