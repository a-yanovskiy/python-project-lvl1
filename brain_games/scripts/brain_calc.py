"""
Calling Calculator-game.

Some discription.
"""

from brain_games.game import play_game_engine
from brain_games.games import calc


def main():
    """Program start."""
    play_game_engine(calc)


if __name__ == '__main__':
    main()
