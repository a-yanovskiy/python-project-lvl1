"""
Calling Calulator-check game.

Some discription.
"""

from brain_games.game import generate_general_game_data
from brain_games.games import even


def main():
    """Program start."""
    generate_general_game_data(even)


if __name__ == '__main__':
    main()
