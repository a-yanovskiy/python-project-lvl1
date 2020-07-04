"""
Calling Prime-check game.

Some discription.
"""

from brain_games.game import set_general_logic
from brain_games.games.prime import description, set_game_logic


def main():
    """Program start."""
    set_general_logic(description, set_game_logic)


if __name__ == '__main__':
    main()
