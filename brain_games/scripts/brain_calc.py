"""
Calling Calculator-game.

Some discription.
"""

from brain_games.games.calc import GAME_RULES, game_logic
from brain_games.game import general_logic


def main():
    """Program start."""
    general_logic(GAME_RULES, game_logic)


if __name__ == '__main__':
    main()
    general_logic()
