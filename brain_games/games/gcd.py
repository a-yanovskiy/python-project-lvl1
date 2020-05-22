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
    return randint(1, 100)  # noqa: S311


def question():
    """Question.

    Returns:
        Question: string.
    """
    return ('{0} {1}'.format(random_digit(), random_digit())), None


def answer(question_list):  # noqa: WPS210
    """Right answer.

    Parameters:
        from_question: arg from question()

    Returns:
        Right answer.
    """
    # получаем значения из входного списка
    from_question = question_list[0]

    digits_str = from_question.split()  # сплитим str значения из question()

    # загоняем их в переменные:
    first_random_digit = int(digits_str[0])
    second_random_digit = int(digits_str[1])

    # решение
    if first_random_digit == second_random_digit:
        ans = first_random_digit
    else:
        min_digit = min(first_random_digit, second_random_digit)
        max_digit = max(first_random_digit, second_random_digit)
        ans = min_digit
        while max_digit % ans != 0:
            ans -= 1
            while min_digit % ans != 0:
                ans -= 1
    return str(ans)
