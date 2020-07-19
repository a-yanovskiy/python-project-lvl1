"""
Calling GCD-game.

Some discription.
"""

from brain_games.game import generate_general_game_data
from brain_games.games import gcd


def main():
    """Program start."""
    generate_general_game_data(gcd)


if __name__ == '__main__':
    main()
