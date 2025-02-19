import random
from math import gcd

TASK = 'Find the greatest common divisor of given numbers.'


def logic_game():
    # Рандомное целое число из диапазонаот 1 до 100
    number1 = random.randrange(1, 100)
    number2 = random.randrange(1, 100)     
    question = f'{number1} {number2}'
    answer = gcd(number1, number2)
    return question, str(answer)