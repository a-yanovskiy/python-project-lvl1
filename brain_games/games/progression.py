"""
Игра "Арифметическая прогрессия".

Игроку показывается ряд чисел, образующий арифметическую прогрессию,
заменив любое из чисел двумя точками. Игрок должен определить это число.
"""

from random import randint

GAME_DESCRIPTION = 'What number is missing in the progression?'


def find_question_and_ans(length, start_dig, step_dig, skip_dig):
    """Set question and answer from arithmetic progression.

    Parameters:
        length: lenght of arithmetic progression
        start_dig: start of arithmetic progression
        step_dig: step of arithmetic progression
        skip_dig: index of digit which must be skiped

    Returns:
        question: progression with skiped digit
        answer: skiped digit with index = skip_digit
    """
    res = ''  # result
    for index in range(10):
        dig = str(start_dig + step_dig * index)
        if index == skip_dig:  # replace skiping digit to '..'
            dig = '..'
        res += dig + ' '
    question = res[:-1]  # del last spase
    answer = str(start_dig + step_dig * skip_dig)
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
    # End

    # Take from functions
    que_ans_list = find_question_and_ans(PROGRESSION_LENGHT, digit, step, skip)
    question = que_ans_list[0]
    answer = que_ans_list[1]
    # End
    return question, answer
