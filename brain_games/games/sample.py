import prompt


def welcome():
    #  Приветствие пользователя
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return (name)


def right_answer():
    print('Correct!')


def finish_game():
    print(f'Congratulations, {name}!')