# task 7.1, task 7.2, task 7.3
#
# 7.1. 7.1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
#
# 7.2. *  Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# my_project:
# ├─ settings:
# │  ├─ __init__.py
# │  ├─ dev.py
# │  └─ prod.py
# ├─ mainapp:
# │  ├─ __init__.py
# │  ├─ models.py
# │  ├─ views.py
# │  └─ templates:
# │     └─ mainapp:
# │        ├─ base.html
# │        └─ index.html
# └─ authapp:
#    ├─ __init__.py
#    ├─ models.py
#    ├─ views.py
#    └─ templates:
#       └─ authapp:
#          ├─ base.html
#          └─ index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
# (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
#
# 7.3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
# которая решена, например, во фреймворке django.

import os
import sys
import json
import shutil


def get_yaml_struct_list(file):
    # Из YAML файла делаем список: [[<отступ::=1,2,3...><строка><True|False::=>Каталог|файл>],[...]...]
    try:
        with open(file) as f_yaml:
            for str0 in f_yaml:
                if str0.startswith('---'):  # начало YAML файла
                    continue
                nest_level = (len(str0) - len(str0.lstrip())) // 3  # ур. вложенности (3 отступа на 1)
                is_dir = str0.strip().endswith(':')  # True, если директория
                str0 = str0.strip()[:-1] if is_dir else str0.strip()  # Имя файла или каталого
                list_yaml.append([nest_level, str0, is_dir])
    except FileNotFoundError as e:
        print(f'Не найден файл: {e.filename}')
        exit(1)
    return


def get_same_indent_nums(idx):
    # Получаем список номеров строк блока с одинаковым отступом в YAML файле
    indent, indexes = list_yaml[idx][0] + 1, []
    for i, l in enumerate(list_yaml[idx + 1::]):  # пропускаем 1 строку '---'
        if l[0] == indent:
            indexes.append(idx + 1 + i)
        elif l[0] < indent:
            break
    return indexes


def decode_yaml(num_string):
    # Получаем иерархическую структуру ветки каталога с директориями разной вложенности и файлами в них,
    # записанную в YAML файле в удобочитаемом виде, типа:
    # {'dir': [{'dir1': [{'dir11': ['file1.py', 'file2.py,', 'file3.py']}, [{'dir12': ['file.py']}]]}]}
    # где директория - словарь, a файлы - эл-ты списка

    list_indexes = get_same_indent_nums(num_string)
    if len(list_indexes) == 1:  # пустой каталог
        if list_yaml[num_string + 1][2]:
            return [{list_yaml[num_string + 1][1]: decode_yaml(num_string + 1)}]
        else:
            return [list_yaml[num_string + 1][1]]
    list_files = []
    if len(list_indexes) > 1:  # Больше 2 записей в каталоге - возвращаем List
        for num_file in list_indexes:
            if list_yaml[num_file][2]:
                list_files.append({list_yaml[num_file][1]: decode_yaml(num_file)})  # Dir - добавляем в list - Dict
            else:
                list_files.append(list_yaml[num_file][1])  # Файл - добавляем в list его имя
    return list_files


def get_list_files_and_dirs(pattern, path):
    # получаем последовательный список для создания структуры папок и файлов вида:
    # ['dir', 'dir/dir1', 'dir/dir1/dir11', 'file1.py', 'file2.py,', 'file3.py', 'dir/dir2', 'file.py']
    result_of_paths = []
    for v in pattern:
        if type(v) is dict:
            dir_path = list(v.keys())[0]
            new_path = path + os.path.sep + dir_path

            result_of_paths.append(f'{new_path}{os.path.sep}')
            result_of_paths.extend(get_list_files_and_dirs(v[dir_path], new_path))
        else:
            result_of_paths.append(v)
    return result_of_paths


def starter(li):
    # Разворачиваем заданную структуру файлов и папок в текущей директории
    last_path = ''
    for val in li:
        if val.endswith(os.path.sep):  # каталог
            last_path = val
            try:
                os.mkdir(val)
            except OSError:
                print(f'Ошибка создания папки {val} в {os.getcwd()}')
                exit(1)
        else:
            f = os.path.join(last_path, val)
            try:
                open(f, 'a').close()
            except OSError:
                print(f'Ошибка создания файла: {os.path.join(os.getcwd(), f)}')
                exit(1)
    return 0


def take_and_expand_file_structure(yaml_file_name):
    # yaml_file_name -->  YAML file, описывающий дерево папок и файлов
    get_yaml_struct_list(yaml_file_name)  # [[1,'dir',True],[2,'file.txt',False],...]
    dict_dir.setdefault(list_yaml[0][1], decode_yaml(0))  # корень структуры папок и файлов

    first_key = list(dict_dir.keys())[0]  # str - первый ключ
    list_of_files.append(f'{first_key}{os.path.sep}')
    list_of_files.extend(get_list_files_and_dirs(dict_dir[first_key], first_key))  # развернутый список  папок и файлов
    ex = starter(list_of_files)  # создаем файлы и папки в текущей директории
    if ex == 0:
        print(f'Структура папок и файлов <{first_key}> развернута в {os.getcwd()}')
    return ex


def task_7_1():
    #  Cформирована cтруктура <dict_dir> из 'config1.yaml'.
    #  Развернута в каталоге запуска.
    #  Сохранена в 'task_7_1.json'.
    #  Для изменения конфигурации - достаточно изменить yaml файл.
    print('Задача 7.1')
    if (q0 := take_and_expand_file_structure('config1.yaml')) != 0:
        return q0
    with open('task_7_1.json', 'w', encoding='utf-8') as f:  # сохранили в JSON
        json.dump(dict_dir, f, ensure_ascii=False)
    print(f'Словарь структуры папок и файлов сохранен в JSON файле')
    return 0


def task_7_2():
    # отличается от предыдущей только более сложной структурой каталогов + добавлены файлы
    print('Задача 7.2')
    return take_and_expand_file_structure('config2.yaml')


def task_7_3():
    print('Задача 7.3')
    if (ret := take_and_expand_file_structure('config2.yaml')) != 0:
        exit(ret)
    coll_folder = f'{list_of_files[0]}template{os.path.sep}'
    os.mkdir(coll_folder)  # создаем дир. <template> для сбора *.html

    last_dir = ''
    for file_n in list_of_files:
        if file_n.endswith(os.path.sep):  # каталог
            last_dir = file_n
        elif file_n.endswith('.html'):
            sour = last_dir + file_n
            des = coll_folder + last_dir.split(os.path.sep, 2)[-2] + os.path.sep
            if not os.path.exists(des):
                os.mkdir(des)
            shutil.copyfile(sour, des + file_n)
    print('В созданную папку <template> собраны все шаблоны ')
    return 0


list_yaml = []  # структурированный список, полученный из <file>.yaml
dict_dir = {}  # иерархическая структура папок и файлов
list_of_files = []  # линейный список папок и файлов для starter

exec_task = {1: task_7_1, 2: task_7_2, 3: task_7_3}


s = input('введите цифру для запуска задания:\n1 - task 7.1\n2 - task 7.2\n3 - task 7.3\n>>> ')
num = int(s) if s.isnumeric() else 1
num = num if 1 <= num <= 3 else 1
exec_task[num]()
