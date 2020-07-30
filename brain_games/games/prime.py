"""
Игра "Простое ли число?".

Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число простое,
или no - если число не является простым.
"""

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


def generate_game_data():
    """Prime of random digit.

    Returns:
        question, answer.
    """
    question = randint(1, 100)
    answer = is_prime(question)
    return question, answer
