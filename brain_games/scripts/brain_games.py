"""
Script brain_games.

Simple console games. Project #1
"""

print('Welcome to the Brain Games!\n')

from brain_games.cli import welcome_user


def main():
    print('Hello, {0}'.format(welcome_user()))


if __name__ == '__main__':
    main()
    welcome_user()
