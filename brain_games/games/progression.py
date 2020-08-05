"""
Игра "Арифметическая прогрессия".

Игроку показывается ряд чисел, образующий арифметическую прогрессию,
заменив любое из чисел двумя точками. Игрок должен определить это число.
"""

from random import randint

GAME_DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(length, start_dig, step_dig):
    """Set question and answer from arithmetic progression.

    Parameters:
        length: lenght of arithmetic progression
        start_dig: start of arithmetic progression
        step_dig: step of arithmetic progression

    Returns:
        progression: progression with skiped digit
        answer: skiped digit with index = skip_digit
    """
    progression = []
    for index in range(length):
        dig = str(start_dig + step_dig * index)
        progression.append(dig)
    return progression


def find_question_and_answer(progression, skip_dig):
    """Set question and answer from arithmetic progression.

    Parameters:
        skip_dig: index of element in progression will skip
        progression: arithmetic progression

    Returns:
        question: progression with skiped digit
        answer: skiped digit with index = skip_digit
    """
    result = ''
    answer = 0
    for (index, element) in enumerate(progression):
        if index == skip_dig:  # replace skiping digit to '..'
            answer = element
            element = '..'
        result += element + ' '
    question = result[:-1]  # del last space
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

    # Take progression
    progression = generate_progression(PROGRESSION_LENGHT, digit, step)
    # end

    # Take answer and question
    que_ans_list = find_question_and_answer(progression, skip)
    (question, answer) = que_ans_list
    # end

    return question, answer
