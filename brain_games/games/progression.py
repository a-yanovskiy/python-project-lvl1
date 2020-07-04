"""
Игра "Арифметическая прогрессия".

Игроку показывается ряд чисел, образующий арифметическую прогрессию,
заменив любое из чисел двумя точками. Игрок должен определить это число.
"""

from random import randint

description = 'What number is missing in the progression?'


def set_game_logic():  # noqa: WPS210
    """Logic for Progression-game.

    Returns:
        question: returns progression list with missed digit
        answer: missed digit
    """
    progression_lenght = 10

    digit = randint(1, progression_lenght)  # noqa: S311
    step = randint(1, progression_lenght)  # noqa: S311
    skip = randint(0, progression_lenght - 1)  # noqa: S311

    def gen_progression(length, start, step_dig, skip_dig):
        question = ''
        answer = 0
        element = ''
        for index in range(length):
            element = str(start + step_dig * index) + ' '  # noqa: WPS336
            if index == skip_dig:
                answer = start + step_dig * index
                element = '.. '
            question += element
        return question, answer

    progression_list = gen_progression(progression_lenght, digit, step, skip)
    question = progression_list[0]
    answer = progression_list[1]
    return question, str(answer)
