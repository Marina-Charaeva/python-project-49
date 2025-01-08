import prompt, random
from brain_games.games.sample import welcome, finish_game


def main_progression():
    #  Приветствие пользователя
    name = welcome()
    # Задание на вычисление недостающего числа в арифметической прогрессии
    print('What number is missing in the progression?')
    for i in range(3):
        # Переменная начала прогрессии
        start = random.randrange(1, 50)
        # Шаг прогрессии
        step = random.randrange(1, 10)
        # Длина ряда
        length = random.randrange(5, 10)
        # Позиция в ряду, которую будет рассчитвать пользователь
        position = random.randrange(0, length-1)
        list = [start, ]
        for i in range(length):
            next_step = start + step
            list.append(next_step)
            start = next_step
        answer = str(list[position])
        list[position] = '..'
        question = ' '.join(map(str, list))
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