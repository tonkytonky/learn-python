print('\n# Задача 1')
names_list = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

names_list_1 = names_list[:]
while True:
    if names_list_1.pop() == 'Валера':
        print('Валера нашелся')
        break

def find_person(name, names_list):
    names_list_2 = names_list[:]
    while True:
        if names_list_2.pop() == name:
            print('{} здесь!'.format(name))
            break

find_person('Валера', names_list)


print('\n# Задача 2')
def ask_user():
    while True:
        print('Как дела?')
        user_input = input().strip().rstrip('?!').lower()
        if user_input == 'хорошо':
            break

        print(get_answer(user_input))
        if user_input == 'пока':
            break

def get_answer(question):
    question = question.strip().rstrip('?!').lower()
    answers = {
        'привет': 'И тебе привет!',
        'как дела': 'Лучше всех',
        'пока': "Увидимся"
    }
    return answers.get(question, 'Я тебя не понимаю')

ask_user()
