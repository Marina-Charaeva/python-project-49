import prompt, random
from brain_games.games.sample import welcome, finish_game


def main_parity():
    #  Приветствие пользователя
    name = welcome()
    #  Задание на определение четности числа
    print('Answer "yes" if the number is even, otherwise answer "no".')
    # Цикл на три попытки
    for i in range(3):
        # Рандомное целое число из диапазонаот 1 до 99
        number = random.randrange(1, 99)
        print(f'Qustion: {number}')
        int = prompt.string(f'Your answer: ')
        if (int == 'yes') and (number % 2 == 0):
            print('Correct!')
        if (int == 'no') and (number % 2 != 0):
            print('Correct!')
        if (int != 'yes') and (number % 2 == 0):
            print(f"'{int}' is wrong answer ;(. Correct answer was 'yes'. 
                  \n Let's try again, {name}!")
            break
        if (int != 'no') and (number % 2 != 0):
            print(f"'{int}' is wrong answer ;(. Correct answer was 'no'. 
                  \n Let's try again, {name}!")
            break
    else:
        finish_game()