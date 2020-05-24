"""
Calling GCD-game.

Some discription.
"""

from brain_games.cli import welcome_user
from brain_games.game import general_logic
from brain_games.games.gcd import answer, game_rules, question


def main():
    """Program start."""
    print('Welcome to the Brain Games!')  # noqa: WPS421
    print(game_rules)  # noqa: WPS421

    name = welcome_user()

    print('Hello, {0}!\n'.format(name))  # noqa: WPS421
    general_logic(question, answer, name)


if __name__ == '__main__':
    main()
