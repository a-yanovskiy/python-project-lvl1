"""
Calling Progression-game.
"""

from brain_games.game_engine import play_game
from brain_games.games import progression


def main():
    """Program start."""
    play_game(progression)


if __name__ == '__main__':
    main()
