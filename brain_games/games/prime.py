import random

import prompt

from brain_games.games.sample import finish_game, right_answer, welcome


def main_prime():
    #  Приветствие пользователя
    name = welcome()
    #  Задание на определение четности числа
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    no_simple = 'no'
    simple = 'yes'
    # Цикл на три попытки
    for i in range(3):
        # Рандомное целое число из диапазонаот 1 до 500
        number = random.randrange(0, 500)
        if number <= 1:
            answer = no_simple
        for i in range(2, number):
            if number % i == 0:
                answer = no_simple
                break
        else:
            answer = simple
        print(f'Question: {number}')
        int = prompt.string('Your answer: ')
        if int == answer:
            right_answer()
        if int != answer:
            print(f'"{int}" is wrong answer ;(. Correct answer was "{answer}". \
                  \n Let\'s try again, {name}!')
            break
    else:
        finish_game()