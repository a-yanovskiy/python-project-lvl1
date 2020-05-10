"""
Игра: "Проверка на четность".

Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число четное, или no - если нечетное.
"""

from random import randint

from prompt import string

from brain_games.cli import welcome_user

print('Welcome to the Brain Games!')                            # noqa: WPS421
print('Answer "yes" if number even otherwise answer "no".\n')   # noqa: WPS421

name = welcome_user()

print('Hello, {0}!\n'.format(name))                             # noqa: WPS421


def parity(digit):                                              # проверяет рандомное число на четность
    """Parity of random digit.

    Parameters:
        digit: argument, which must be check for parity.

    Returns:
        'yes' or 'no': string.
    """
    answer = ''
    if digit % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer


def input_answer():                                             # значение вводит пользователь
    """
    User answer.

    Returns:
        User input.
    """
    user_answer = string('Your answer: ')
    return user_answer                                          # noqa: WPS331


def parity_check():                                             # сравнение результатов
    # Parity check game.
    
    count = 0
    right_ans = ''
    user_ans = ''
    global name
    while count < 3:
        random_digit = randint(0, 100)
        print(random_digit)
        right_ans = parity(random_digit)
        user_ans = input_answer()
        if right_ans != user_ans:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(user_ans, right_ans, name))
            break
        else:
            print('Correct!')
            count += 1
            if count < 3:
                continue
        print('Congratulations, {0}!'.format(name))
