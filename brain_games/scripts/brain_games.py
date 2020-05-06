"""
Script brain_games.

Simple console games. Project #1
"""

from brain_games.cli import welcome_user


def greeting():
    """Return greeting to new user.

    Returns:
        Greeting
    """
    return 'Welcome to the Brain Games!\n'

def main():
    print(greeting())
    print(welcome_user())


if __name__ == '__main__':
    main()
    greeting()
    welcome_user()
