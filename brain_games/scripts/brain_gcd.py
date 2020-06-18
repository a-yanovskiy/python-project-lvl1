"""
Calling GCD-game.

Some discription.
"""

from brain_games.cli import welcome_user
from brain_games.game import general_logic
from brain_games.games.gcd import GAME_RULES, get_answer, set_question


def main():
    """Program start."""
    print('Welcome to the Brain Games!')  # noqa: WPS421
    print(GAME_RULES)  # noqa: WPS421

    username = welcome_user()

    print('Hello, {0}!\n'.format(username))  # noqa: WPS421
    general_logic(set_question, get_answer, username)


if __name__ == '__main__':
    main()
