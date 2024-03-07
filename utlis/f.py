import datetime
import json
from class_Print_history import Print_history

def import_json():
    """ Открывает json объект и возвращает его"""
    # with open('C:\\Users\\79096\\PycharmProjectsGit\\CW_3\\CW_3\\utlis\\operations.json', 'r',encoding='utf-8') as file:
    with open('C:\\Users\\79096\\PycharmProjectsGit\\CW_3\\CW_3\\utlis\\operations.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def check_error(word):
    """ Проверка на наличие ключа в словаре, возвращает False
или True """
    if word == None:
        print("Что-то не так с ключом :(\nКакое-то значение будет \'None\' ")
        return False
    else:
        return True


def print_sorted_list(Print_history_=Print_history, import_json_=import_json(), min=0, max=5):
    """ Сортировка 5 значений, возварщает отсортированный список индексов,
    который используеться для создания экземпляров по убыванию дат """

    dict_sort = {}
    for i in range(min, max):
        copy_print_history = Print_history_(import_json_, i)
        d = copy_print_history.date_print()
        dict_sort[i] = d
    sorted_values = sorted(dict_sort.values(), key=lambda x: datetime.datetime.strptime(x, "%d.%m.%Y"), reverse=True)
    list_index = list()
    for i in range(min, max):
        for k, v in dict_sort.items():
            if v == sorted_values[i]:
                list_index.append(k)
    return list_index
