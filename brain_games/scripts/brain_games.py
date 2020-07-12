"""
Script brain_games.

Simple console games. Project #1
"""

from brain_games.cli import welcome_user


def greeting():
    """Welcome new user."""
    print('Welcome to the Brain Games!')
    print('\n')


def greeting_user():
    """Greeting to user with username."""
    print('Hello, {0}\n'.format(welcome_user()))


def main():
    """Greeting user."""
    greeting()
    greeting_user()


if __name__ == '__main__':
    main()
