"""
Script brain_games.

Simple console games. Project #1
"""

from brain_games.cli import welcome_user

print('Welcome to the Brain Games!\n')  # noqa: WPS421


def main():
    """Print greeting for new user."""
    print('Hello, {0}'.format(welcome_user()))  # noqa: WPS421


if __name__ == '__main__':
    main()
    welcome_user()
