"""
Game engine.

For simple console games.
"""
from prompt import string

NUMBER_OF_QUESTIONS = 3


def play_game(game):
    """Game engine.

    Parameters:
        game: game module
    """
    print('Welcome to the Brain Games!')
    print('{0}\n'.format(game.GAME_DESCRIPTION))
    username = string('May I have your name? ')
    print('Hello, {0}!\n'.format(username))
    count = 0
    # extract question, answer from generate_game_data
    while count < NUMBER_OF_QUESTIONS:
        (question, answer) = game.generate_game_data()
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
            return
        print('Congratulations, {0}!'.format(username))
