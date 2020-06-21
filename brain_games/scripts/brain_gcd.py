"""
Calling GCD-game.

Some discription.
"""

from brain_games.game import general_logic
from brain_games.games.gcd import game_logic, game_rules


def main():
    """Program start."""
    general_logic(game_rules, game_logic)


if __name__ == '__main__':
    main()
