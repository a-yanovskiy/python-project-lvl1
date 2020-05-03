"""
Script brain_games.

Simple console games. Project #1
"""

from brain_games.cli import welcome_user


def main():
    """Return greeting to new user."""
    return 'Welcome to the Brain Games!\n'


print(main())
print(welcome_user())


if __name__ == '__main__':
    main()
    welcome_user()
