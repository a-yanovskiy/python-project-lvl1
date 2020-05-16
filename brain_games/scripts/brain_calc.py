"""
Calling Parity-check game.

Some discription.
"""

from brain_games.games.calc import question, answer, game_rules
from brain_games.game import general_logic
from brain_games.cli import welcome_user

print('Welcome to the Brain Games!')  # noqa: WPS421
print(game_rules)  # noqa: WPS421

name = welcome_user()

print('Hello, {0}!\n'.format(name))  # noqa: WPS421


def main():
    """Program start."""
    global name
    general_logic(question, answer, name)


if __name__ == '__main__':
    main()
    general_logic
    
