"""
Calling Prime-check game.

Some discription.
"""

from brain_games.game import play_game_engine
from brain_games.games import prime


def main():
    """Program start."""
    play_game_engine(prime)


if __name__ == '__main__':
    main()
