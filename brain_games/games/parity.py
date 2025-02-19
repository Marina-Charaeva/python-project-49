import random

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def logic_game():
    number = random.randrange(1, 99)
    even = 'yes'
    odd = 'no'
    question = str(number)
    if number % 2 == 0:
        answer = even
    else:
        answer = odd
    return question, answer