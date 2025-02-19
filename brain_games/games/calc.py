import random

TASK = 'What is the result of the expression?'


def logic_game():
    arithmetic = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
    }
    # Рандомное целое число из диапазонаот 1 до 50
    number1 = random.randrange(1, 50)
    number2 = random.randrange(1, 50)
    operator = random.choice(list(arithmetic.keys()))
    answer = str(arithmetic[operator](number1, number2))
    question = f"{number1} {operator} {number2}"
    return question, answer