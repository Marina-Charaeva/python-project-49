import random

import prompt

from brain_games.games.sample import finish_game, right_answer, welcome


def main_gcd():
    #  Приветствие пользователя
    name = welcome()
    # Задание на вычисление наибольшего общего делителя
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        # Рандомное целое число из диапазонаот 1 до 100
        number1 = random.randrange(1, 100)
        number2 = random.randrange(1, 100)     
        print(f'Qustion: {number1} {number2}')
        int = prompt.string('Your answer: ')
        if number1 == number2:
            answer = str(number1)
        else:
            x = number1
            y = number2
            while (x != 0) and (y != 0):
                if x > y:
                    x = x % y
                else:
                    y = y % x
            answer = str(x + y)
        if int == answer:
            right_answer()
        if int != answer:
            print(f'"{int}" is wrong answer ;(. Correct answer was "{answer}". \
                  \n Let\'s try again, {name}!')
            break
    else:
        finish_game()