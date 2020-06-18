"""
Игра "НОД".

Суть игры в следующем:
Пользователю показывается два случайных числа.
Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.
"""

from random import randint

GAME_RULES = 'Find the greatest common divisor of given numbers.\n'


def random_digit():
    """Random digit.

    Returns:
        random digit (1,100).
    """
    return randint(1, 100)  # noqa: S311


def set_question():
    """Question.

    Returns:
        Question: string.
    """
    return ('{0} {1}'.format(random_digit(), random_digit())), None  # question_list


def get_answer(question_list):  # noqa: WPS210
    """Right answer.

    Parameters:
        question_list: arg from question()

    Returns:
        Right answer.
    """
    # получаем значения из входного списка
    from_question = question_list[0]

    digits_str = from_question.split()  # сплитим str значения из question()

    # загоняем их в переменные:
    first_random_digit = int(digits_str[0])
    second_random_digit = int(digits_str[1])

    # проверяем, равны числа или нет
    if first_random_digit == second_random_digit:
        ans = first_random_digit
    else:
        # выясняем, какое из чисел больше, а какое меньше
        min_digit = min(first_random_digit, second_random_digit)
        max_digit = max(first_random_digit, second_random_digit)
        ans = min_digit  # минимальное число принимаем за ответ
        while max_digit % ans != 0:  # делим большее число на меньшее
            # если не делится, отнимаем 1 от ans
            ans -= 1
            # проверяем делится ли меньшее число на делитель большего
            while min_digit % ans != 0:
                ans -= 1
    return str(ans)
