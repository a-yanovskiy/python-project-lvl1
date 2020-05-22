"""
Calling Prime-check game.

Some discription.
"""

from brain_games.cli import welcome_user
from brain_games.game import general_logic
from brain_games.games.prime import answer, game_rules, question

print('Welcome to the Brain Games!')  # noqa: WPS421
print(game_rules)  # noqa: WPS421

name = welcome_user()

print('Hello, {0}!\n'.format(name))  # noqa: WPS421


def main():
    """Program start."""
    global name  # noqa: WPS420
    general_logic(question, answer, name)


if __name__ == '__main__':
    main()
