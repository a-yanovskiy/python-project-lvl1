"""
Game: "Parity check".
A random number is shown to the user.
And he needs to answer yes if the number is even, or no if it is odd.
"""

from random import randint

GAME_DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(digit):
    """Take digit, if even returns True.

    Parameters:
        digit: Integer.

    Returns:
        True or False
    """
    return digit % 2 == 0


def generate_game_data():
    """Logic for Brain-even game.

    Returns:
        question, answer.
    """
    question = randint(1, 100)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer
