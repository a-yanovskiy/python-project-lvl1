"""
Game engine.

For simple console games.
"""
from prompt import string

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


def play_game_engine(game):
    """Game engine.

    Parameters:
        game: game module
    """
    GAME_DESCRIPTION = game.GAME_DESCRIPTION
    print('Welcome to the Brain Games!')
    print('{0}\n'.format(GAME_DESCRIPTION))
    username = string('May I have your name? ')
    print('Hello, {0}!\n'.format(username))
    count = 0
    # extract question, answer from generate_game_data
    NUMBER_OF_QUESTIONS = 3
    while count < NUMBER_OF_QUESTIONS:
        (question, answer) = game.generate_game_data()
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
