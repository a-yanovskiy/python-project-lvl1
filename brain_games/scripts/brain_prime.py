"""
Calling Prime-check game.

Some discription.
"""

from brain_games.game import generate_general_game_data
from brain_games.games import prime


def main():
    """Program start."""
    generate_general_game_data(prime)


if __name__ == '__main__':
    main()
