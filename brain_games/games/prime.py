"""
The game "Is a number prime?".

A random number is shown to the user. 
Needs to answer yes if the number is prime, or no if the number is not prime.
"""

from random import randint

GAME_DESCRIPTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
        )


def is_prime(digit):
    """Take digit. Returns True if it is prime, or False is not.

    Parameters:
        digit: integer.

    Returns:
        answer: True if it is prime, or False is not.
    """
    if digit < 2:
        return False
    else:
        divider = (digit // 2)
        while divider > 1:
            if digit % divider == 0:
                return False
            else:
                divider -= 1
        else:
            return True


def generate_game_data():
    """Prime of random digit.

    Returns:
        question, answer.
    """
    question = randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
