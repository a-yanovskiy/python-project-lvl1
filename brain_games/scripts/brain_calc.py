"""
Calling Calculator-game.
"""

from brain_games.game_engine import play_game
from brain_games.games import calc


def main():
    """Program start."""
    play_game(calc)


if __name__ == '__main__':
    main()
