"""
Calling Parity-check game.

Some discription.
"""

from brain_games.cli import welcome_user
from brain_games.parity_check import parity_check
from brain_games.scripts.brain_games import greeting


def main():
    """
    Main function.

    Program start.
    """
    print(greeting())
    print(welcome_user())
    parity_check()


if __name__ == '__main__':
    main()
    greeting()
    welcome_user()
    parity_check()
