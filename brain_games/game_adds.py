"""
Дополнительный модуль для game.py
"""

def tellme_yes_or_no(predicat):
    """Take True or False.

    Parameters:
        predicat: True or False.

    Returns:
        'yes' or 'no.
    """
    if predicat:
        ans = 'yes'
    else:
        ans = 'no'
    return ans