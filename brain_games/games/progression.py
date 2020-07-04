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

    PROGRESSION_LENGTH = 10

    digit = randint(1, PROGRESSION_LENGTH)  # noqa: S311
    step = randint(1, PROGRESSION_LENGTH)  # noqa: S311
    skip = randint(0, PROGRESSION_LENGTH - 1)  # noqa: S311

    # question = ''

    # for index in range(PROGRESSION_LENGTH):
    #     if index == skip:
    #         question = ('{0} .. ').format(question)
    #         answer = digit
    #         digit += step
    #     question = ('{0} {1} ').format(question, str(digit))
    #     digit += step


    def gen_progression(length, start, step, skip):
        question = ''
        answer = 0
        element = ''
        for index in range(length):
            element = str(start + step * index) + ' '
            if index == skip:
                answer = start + step * index
                element = '.. '
            question += element
        return question, answer


    progression_list = gen_progression(PROGRESSION_LENGTH, digit, step, skip)

    question = progression_list[0]
    answer = progression_list[1]


    return question, str(answer)
