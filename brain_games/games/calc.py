import prompt, random
from brain_games.games.sample import welcome, finish_game


def main_calc():
    #  Приветствие пользователя
    name = welcome()
    # Задание на вычисление математического выражения
    print('What is the result of the expression?')
    arithmetic = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
    }
    # Цикл на три попытки
    for i in range(3):
        # Рандомное целое число из диапазонаот 1 до 50
        number1 = random.randrange(1, 50)
        number2 = random.randrange(1, 50)
        operator = random.choice(list(arithmetic.keys()))
        question = str(number1) + str(operator) + str(number2)
        answer = str(arithmetic[operator](number1, number2))
        print(f'Qustion: {question}')
        int = prompt.string('Your answer: ')
        if int == answer:
            print('Correct!')
        if int != answer:
            print(f"'{int}' is wrong answer ;(. Correct answer was '{answer}'. \
                  \n Let's try again, {name}!")
            break
    else:
        finish_game()