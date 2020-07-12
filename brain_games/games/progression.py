"""
Игра "Арифметическая прогрессия".

Игроку показывается ряд чисел, образующий арифметическую прогрессию,
заменив любое из чисел двумя точками. Игрок должен определить это число.
"""

from random import randint

description = 'What number is missing in the progression?'


def gen_progression(length, start_dig, step_dig):
    """Generate arithmetic progression.

    Parameters:
        length: length of progression
        start_dig: the number at which progression begins
        step_dig: progression step

    Returns:
        progression: returns arithmetic progression
    """
    progression = []
    for __index__ in range(length):  # __index__ is fix linter issue B007
        progression.append(start_dig)
        start_dig += step_dig
    return progression


def find_question_and_answer(progression, skip_dig):
    """Set question and answer from arithmetic progression.

    Parameters:
        progression: returns arithmetic progression
        skip_dig: index of digit which must be skiped

    Returns:
        question: progression with skiped digit
        answer: skiped digit with index = skip_digit
    """
    index = 0
    question = ''
    answer = progression[skip_dig]
    for dig in progression:
        if dig == answer:
            question = question + '.. '
            index += 1
            continue
        question += str(dig) + ' '
        index += 1
    return question, str(answer)


def set_game_logic():
    """Logic for Progression-game.

    Returns:
        question: returns progression list with missed digit
        answer: missed digit
    """
    progression_lenght = 10
    digit_randomize_to = 10
    step_randomize_to = 10

    # Randoms block
    digit = randint(1, digit_randomize_to)
    step = randint(1, step_randomize_to)
    skip = randint(0, progression_lenght - 1)
    # End

    # Take from functions
    progression_list = gen_progression(progression_lenght, digit, step)
    question_answer_list = find_question_and_answer(progression_list, skip)
    question = question_answer_list[0]
    answer = question_answer_list[1]
    # End
    return question, answer
