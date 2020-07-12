"""
Игра "НОД".

Суть игры в следующем:
Пользователю показывается два случайных числа.
Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.
"""

from random import randint

description = 'Find the greatest common divisor of given numbers.'


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


def set_game_logic():
    """Right answer.

    Returns:
        question, answer.
    """
    first_random_digit = randint(1, 100)
    second_random_digit = randint(1, 100)

    question = '{0}, {1}'.format(first_random_digit, second_random_digit)
    answer = get_gcd(first_random_digit, second_random_digit)
    return question, str(answer)
