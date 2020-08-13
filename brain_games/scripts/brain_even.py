"""
Calling Calulator-check game.

Some discription.
"""

from brain_games.game_engine import play_game
from brain_games.games import even


def main():
    """Program start."""
    play_game(even)


if __name__ == '__main__':
    main()
