"""
Calling GCD-game.

Some discription.
"""

from brain_games.game_engine import play_game
from brain_games.games import gcd


def main():
    """Program start."""
    play_game(gcd)


if __name__ == '__main__':
    main()
