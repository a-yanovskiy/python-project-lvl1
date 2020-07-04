"""
Игра "Простое ли число?".

Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число простое,
или no - если число не является простым.
"""

from random import randint

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def set_game_logic():
    """Prime of random digit.

    Returns:
        question, answer.
    """
    question = randint(1, 100)  # noqa: S311

    def check_simpity(digit):
        answer = 'yes'
        divider = digit - 1
        while divider > 1:
            if digit % divider == 0:
                answer = 'no'
                break
            else:
                divider -= 1
        return answer

    return question, check_simpity(question)
