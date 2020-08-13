"""
Игра "Арифметическая прогрессия".

Игроку показывается ряд чисел, образующий арифметическую прогрессию,
заменив любое из чисел двумя точками. Игрок должен определить это число.
"""

from random import randint

GAME_DESCRIPTION = 'What number is missing in the progression?'


def progression(length, start, step, skip):
    """Set question and answer from arithmetic progression.

    Parameters:
        length: lenght of arithmetic progression
        start: start of arithmetic progression
        step: step of arithmetic progression

    Returns:
        progression: progression with skiped digit
        answer: skiped digit with index = skip_digit
    """
    progression = []
    for index in range(length):
        element = str(start + step * index)
        if index == skip:  # replace skiping digit to '..'
            answer = element
            progression.append('.. ')
            continue
        progression.append(element)
    return progression, answer



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

    # Take progression
    (question, answer) = progression(PROGRESSION_LENGHT, digit, step, skip)
    # end


    return question, answer
