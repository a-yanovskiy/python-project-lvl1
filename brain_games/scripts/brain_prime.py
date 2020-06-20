"""
Calling Prime-check game.

Some discription.
"""

from brain_games.games.prime import GAME_RULES, game_logic
from brain_games.game import general_logic


def main():
    """Program start."""
    general_logic(GAME_RULES, game_logic)


if __name__ == '__main__':
    main()
