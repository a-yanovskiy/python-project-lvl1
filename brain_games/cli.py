"""
Asking username.

Some docstring to satisfy linter.
"""

import prompt


def welcome_user():
    """Asking username.

    Returns:
        New user name.
    """
    name = prompt.string('May I have your name? ')
    return name     # noqa: WPS331
