"""
Игра: "Проверка на четность".

Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число четное, или no - если нечетное.
"""

from random import randint

from prompt import string


def parity(digit):    # проверяет рандомное число на четность
    """Parity of random digit.

    Returns:
        Right answer.
    """
    if digit % 2 == 0:
        return 'yes'
    else:
        return 'no'


def input_answer():    # значение вводит пользователь
    """
    User answer.

    Returns:
        User input.
    """
    user_answer = string('Your answer: ')
    return user_answer

def parity_check():    # сравнение результатов
    """
    Parity check game.
    """
    count = 0
    right_ans = ''
    user_ans = ''
    while count != 3:
        random_digit = randint(0,100)
        print(random_digit)
        right_ans = parity(random_digit)
        user_ans = input_answer()
        if right_ans == user_ans:
            print('Correct!')
            count += 1
        else:
            count = 3
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(user_ans, right_ans))
