"""
The game "Arithmetic progression".

The player is shown a series of numbers forming an arithmetic progression,
replacing any of the numbers with two dots. The player must determine this number.
"""

from random import randint

GAME_DESCRIPTION = 'What number is missing in the progression?'


def generate_game(length, start, step, skip):
    """Set question and answer from arithmetic progression.

    Parameters:
        length: lenght of arithmetic progression
        start: start of arithmetic progression
        step: step of arithmetic progression
        skip: index of skiping number

    Returns:
        progression: progression with skiped digit
        answer: skiped digit with index = skip_digit
    """
    progression = ''
    for index in range(length):
        element = str(start + step * index)
        if index == skip:
            answer = element
            progression += '.. '
            continue
        progression += element + ' '
        question = progression[:-1]
    return question, answer


def generate_game_data():
    """Logic for Progression-game.

    Returns:
        question: returns progression list with missed digit
        answer: missed digit
    """
    PROGRESSION_LENGHT = 10
    DIGIT_RANDOM_TO = 10
    STEP_RANDOM_TO = 10

    # Randoms block
    digit = randint(1, DIGIT_RANDOM_TO)
    step = randint(1, STEP_RANDOM_TO)
    skip = randint(0, PROGRESSION_LENGHT - 1)
    # end

    (question, answer) = generate_game(
        PROGRESSION_LENGHT, digit, step, skip,
    )

    return question, answer
