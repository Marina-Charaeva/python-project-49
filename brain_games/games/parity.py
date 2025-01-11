import random

import prompt

from brain_games.games.sample import finish_game, right_answer, welcome


def main_parity():
    #  Приветствие пользователя
    name = welcome()
    #  Задание на определение четности числа
    print('Answer "yes" if the number is even, otherwise answer "no".')
    # Цикл на три попытки
    for i in range(3):
        # Рандомное целое число из диапазонаот 1 до 99
        number = random.randrange(1, 99)
        even = 'yes'
        odd = 'no'
        if number % 2 == 0:
            answer = even
        else:
            answer = odd
        print(f'Question: {number}')
        int = prompt.string('Your answer: ')
        if int == answer:
            right_answer()
        if int != answer:
            print(f"'{int}' is wrong answer ;(. Correct answer was '{answer}'. \
                  \n Let\'s try again, {name}!")
            break
    else:
        finish_game()