"""
Script brain_games.

Simple console games. Project #1
"""

from brain_games.cli import welcome_user


def greeting():
    """Welcome new user."""
    print('Welcome to the Brain Games!')  # noqa: WPS421
    print('\n')  # noqa: WPS421


def greeting_user():
    """Greeting to user with username."""
    print('Hello, {0}\n'.format(welcome_user()))  # noqa: WPS421


def main():
    """Greeting user."""
    greeting()
    greeting_user()


if __name__ == '__main__':
    main()
