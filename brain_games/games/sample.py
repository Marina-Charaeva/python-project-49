import prompt


def start_game(game_name):
    #  Приветствие пользователя
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_name.TASK)
    for i in range(3):
        question, answer = game_name.logic_game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'. \n"
                  f"Let\'s try again, {name}!")
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {name}!')