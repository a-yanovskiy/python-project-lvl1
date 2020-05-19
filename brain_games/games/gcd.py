"""
Игра "НОД".

Суть игры в следующем:
Пользователю показывается два случайных числа. 
Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.
"""

from random import randint

game_rules = 'Find the greatest common divisor of given numbers.\n'


def random_digit():
    """Random digit.

    Returns:
        random digit (1,100).
    """
    random_digit = randint(1, 100)  # noqa: S311
    return (random_digit)


def question():
    """Question.

    Returns:
        Question: string.
    """
    first_random_digit = random_digit()
    second_random_digit = random_digit()
    return ('{0} {1}'.format(first_random_digit, second_random_digit))


def answer(question):
    """Right answer.

    Parameters:
        first_digit: first argument from question()
        second_digit: second argument from question()

    Returns:
        Right answer.
    """
    # сплитим str значения из question():
    digits_str = question.split()

    # загоняем их в переменные:
    first_random_digit = int(digits_str[0])
    second_random_digit = int(digits_str[1])

    # решение
    if first_random_digit == second_random_digit:
        answer = first_random_digit
    else:
        min_digit = min(first_random_digit, second_random_digit)
        max_digit = max(first_random_digit, second_random_digit)
        answer = min_digit
        while max_digit % answer != 0:
            answer -= 1
            while min_digit % answer != 0:
                answer -=1
                continue
    return str(answer)