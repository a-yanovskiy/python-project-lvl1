"""
Calling Calulator-check game.

Some discription.
"""

from brain_games.game import play_game_engine
from brain_games.games import even


def main():
    """Program start."""
    play_game_engine(even)


if __name__ == '__main__':
    main()
