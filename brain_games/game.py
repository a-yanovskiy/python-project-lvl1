"""
Game engine.

For simple console games.
"""
from prompt import string

from brain_games.cli import welcome_user


def tellme_yes_or_no(predicat):
    """Take True or False.

    Parameters:
        predicat: True or False.

    Returns:
        'yes' or 'no.
    """
    if predicat is True:
        ans = 'yes'
    elif predicat is False:
        ans = 'no'
    else:
        ans = predicat
    return ans


def generate_general_game_data(game):
    """Game engine.

    Parameters:
        game: game module
    """
    description = game.description
    print('Welcome to the Brain Games!')
    print('{0}\n'.format(description))
    username = welcome_user()
    print('Hello, {0}!\n'.format(username))
    count = 0
    # extract question, answer from generate_game_data
    NUMBER_OF_QUESTIONS = 3
    while count < NUMBER_OF_QUESTIONS:
        game_logic_list = game.generate_game_data()
        question = game_logic_list[0]
        answer = game_logic_list[1]
        answer = tellme_yes_or_no(answer)  # проверка на предикат
        print(question)
        user_answer = string('Your answer: ')  # user input
        if user_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(
                """'{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!
                """.format(user_answer, answer, username),
            )
            break
        if count < NUMBER_OF_QUESTIONS:
            continue
        print('Congratulations, {0}!'.format(username))
