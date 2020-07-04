"""
Script brain_games.

Simple console games. Project #1
"""

from brain_games.cli import welcome_user

def greeting():
    print('Welcome to the Brain Games!')
    print('\n')  # noqa: WPS421

def greeting_user():
    print('Hello, {0}\n'.format(welcome_user()))  # noqa: WPS421


def main():
    greeting()
    greeting_user()


if __name__ == '__main__':
    main()
