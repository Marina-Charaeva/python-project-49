import random

TASK = 'What number is missing in the progression?'


def logic_game():
    # Переменная начала прогрессии
    start = random.randrange(1, 50)
    # Шаг прогрессии
    step = random.randrange(1, 10)
    # Длина ряда
    length = random.randrange(5, 10)
    # Позиция в ряду, которую будет рассчитвать пользователь
    position = random.randrange(0, length - 1)
    list = [start, ]
    for i in range(length):
        next_step = start + step
        list.append(next_step)
        start = next_step
    answer = str(list[position])
    list[position] = '..'
    question = ' '.join(map(str, list))
    return question, answer
