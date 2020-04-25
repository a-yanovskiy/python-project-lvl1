"""
Asking username.

Some docstring to satisfy linter.
"""

import prompt


def welcome_user():
    """Asking username.

    Returns:
        greeting for new user.
    """
    name = prompt.string('May I have your name? ')
    return 'Hello, {0}'.format(name)
