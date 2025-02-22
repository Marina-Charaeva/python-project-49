import random

TASK = 'Answer 'yes' if given number is prime. Otherwise answer 'no'.'


def logic_game():
    no_simple = 'no'
    simple = 'yes'
    # Рандомное целое число из диапазонаот 1 до 500
    number = random.randrange(0, 500)
    question = str(number)
    if number <= 1:
        answer = no_simple
    for i in range(2, number):
        if number % i == 0:
            answer = no_simple
            break
    else:
        answer = simple
    return question, answer