def ask_user():
    try:
        while True:
            print('Как дела?')
            user_input = input().strip().rstrip('?!').lower()
            if user_input == 'хорошо':
                print('Ясно, пока!')
                break

            try:
                print(get_answer(user_input))
            except KeyError:
                print('Я тебя не понимаю')

            if user_input == 'пока':
                break

    except KeyboardInterrupt:
        print('Увидимся')


def get_answer(question):
    question = question.strip().rstrip('?!').lower()
    answers = {
        'привет': 'И тебе привет!',
        'как дела': 'Лучше всех',
        'пока': 'Увидимся'
    }

    return answers[question]


ask_user()
