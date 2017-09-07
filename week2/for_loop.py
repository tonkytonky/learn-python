import random


print('\n# Задача 1')
for number in range(10):
    print(number + 1)


print('\n# Задача 2')
for char in input('Введите строку: '):
    print(char)


print('\n# Задача 3')
def gen_scores_list():
    return [random.randint(2, 5) for _ in range(random.randint(5, 15))]

def get_school_class_average(school_class):
    return sum(school_class['scores']) / len(school_class['scores'])

def get_school_average(school_classes_list):
    return sum(get_school_class_average(school_class) for school_class in school_classes_list) / len(school_classes_list)

school_classes_list = [
    {'school_class': '1а', 'scores': gen_scores_list()},
    {'school_class': '1б', 'scores': gen_scores_list()},
    {'school_class': '2a', 'scores': gen_scores_list()},
    {'school_class': '2б', 'scores': gen_scores_list()},
    {'school_class': '2в', 'scores': gen_scores_list()},
    {'school_class': '3', 'scores': gen_scores_list()},
    {'school_class': '4a', 'scores': gen_scores_list()},
    {'school_class': '4б', 'scores': gen_scores_list()},
    {'school_class': '5a', 'scores': gen_scores_list()},
    {'school_class': '5б', 'scores': gen_scores_list()},
]

print('Средний балл по всей школе: {:.1f}'.format(get_school_average(school_classes_list)))
for school_class in school_classes_list:
    print('Средний балл класса {}: {:.1f}'.format(school_class['school_class'], get_school_class_average(school_class)))
