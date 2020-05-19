"""
Game engine.

For simple console games.
"""

from prompt import string


def input_answer():
    """
    User answer.

    Returns:
        User input.
    """
    user_answer = string('Your answer: ')
    return user_answer  # noqa: WPS331


def general_logic(question, answer, name):
    """Game engine.

    Parameters:
        question: question to user
        answer: right answer
        name: username
    """
    count = 0
    while count < 3:
        quest = question()
        print(quest)  # noqa: WPS421
        user_answer = input_answer()
        right_ans = answer(quest)
        if user_answer == 'exit':
            break
        if user_answer == right_ans:
            print('Correct!')  # noqa: WPS421
            count += 1
        else:
            print(  # noqa: WPS421
                """'{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!
                """.format(user_answer, right_ans, name),
                  )
            break
        if count < 3:
            continue
        print('Congratulations, {0}!'.format(name))  # noqa: WPS421
