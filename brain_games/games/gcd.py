"""
The game "GCD".

The user is shown two random numbers.
The user must calculate and enter the greatest common divisor of these numbers.
"""

from random import randint

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(first_digit, second_digit):
    """Take two digits, returns greatest common divisor.

    Parameters:
        first_digit: integer
        second_digit: integer.

    Returns:
        Greatest common divisor
    """
    if first_digit == second_digit:
        answer = first_digit
    else:
        min_digit = min(first_digit, second_digit)
        max_digit = max(first_digit, second_digit)
        answer = min_digit  # минимальное число принимаем за ответ
        while max_digit % answer != 0:  # делим большее число на меньшее
            answer -= 1
            while min_digit % answer != 0:
                answer -= 1
    return answer


def generate_game_data():
    """Right answer.

    Returns:
        question, answer.
    """
    first_random_digit = randint(1, 100)
    second_random_digit = randint(1, 100)

    question = '{0}, {1}'.format(first_random_digit, second_random_digit)
    answer = get_gcd(first_random_digit, second_random_digit)
    return question, str(answer)
