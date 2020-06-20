"""
Игра "НОД".

Суть игры в следующем:
Пользователю показывается два случайных числа.
Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.
"""

from random import randint

GAME_RULES = 'Find the greatest common divisor of given numbers.\n'


def game_logic():  # noqa: WPS210
    """Right answer.

    Parameters:
        question_list: arg from question()

    Returns:
        Right answer.
    """
    first_random_digit = randint(1, 100)  # noqa: S311
    second_random_digit = randint(1, 100)  # noqa: S311

    question = '{0}, {1}'.format(first_random_digit, second_random_digit)

    # проверяем, равны числа или нет
    if first_random_digit == second_random_digit:
        answer = first_random_digit
    else:
        # выясняем, какое из чисел больше, а какое меньше
        min_digit = min(first_random_digit, second_random_digit)
        max_digit = max(first_random_digit, second_random_digit)
        answer = min_digit  # минимальное число принимаем за ответ
        while max_digit % answer != 0:  # делим большее число на меньшее
            # если не делится, отнимаем 1 от answer
            answer -= 1
            # проверяем делится ли меньшее число на делитель большего
            while min_digit % answer != 0:
                answer -= 1
    return question, str(answer)
