"""
Game engine.

For simple console games.
"""

from prompt import string
from brain_games.cli import welcome_user


def general_logic(GAME_RULES, game_logic):  # noqa: WPS231
    """Game engine.

    Parameters:
        question: question to user
        answer: right answer
        name: username
    """

    print('Welcome to the Brain Games!')  # noqa: WPS421
    print(GAME_RULES)  # noqa: WPS421
    username = welcome_user()
    print('Hello, {0}!\n'.format(username))  # noqa: WPS421


    count = 0
    while count < 3:
    # extract question, answer from game_logic
        game_logic_list = game_logic()
        question = game_logic_list[0]
        answer = game_logic_list[1]
        print(question)  # noqa: WPS421
        user_answer = string('Your answer: ')  # user input
        if user_answer == answer:
            print('Correct!')  # noqa: WPS421
            count += 1
        else:
            print(  # noqa: WPS421
                """'{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!
                """.format(user_answer, answer, username),
                  )
            break
        if count < 3:
            continue
        print('Congratulations, {0}!'.format(username))  # noqa: WPS421
