"""
Игра "Простое ли число?".

Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число простое,
или no - если число не является простым.
"""

import brain_games.game_adds
from random import randint

GAME_DESCRIPTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
        )


def is_prime(digit):  # должен быть предикат
    """Take digit. Returns True if it is prime, or False is not.

    Parameters:
        digit: integer.

    Returns:
        answer: True if it is prime, or False is not.
    """
    if digit < 2:  # guardian expression
        divider = (digit / 2) - 1
        while divider > 1:
            if digit % divider == 0:
                answer = False
                break
            else:
                divider -= 1
        else:
            answer = True
            return answer
    else:
        return False


def generate_game_data():
    """Prime of random digit.

    Returns:
        question, answer.
    """
    question = randint(1, 100)
    answer = game_adds.tellme_yes_or_no(is_prime(question))
    return question, answer
