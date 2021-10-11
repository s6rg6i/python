# 7.4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов
# (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
#
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os


def find_files(catalog):
    size_statistics = {key: 0 for key in (10 ** n for n in range(1, 10))}
    for root, dirs, files in os.walk(catalog):
        for f_name in files:
            size = os.stat(os.path.join(root, f_name)).st_size
            key = [x for x in (10 ** n for n in range(1, 10)) if x >= size][0]
            size_statistics[key] += 1
    return size_statistics


curr_dir = os.getcwd()
summary = find_files(curr_dir)
print(summary)
