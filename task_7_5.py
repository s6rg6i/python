# 7.5.  *  Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
# а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#     {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

import os
import json


def find_files(catalog):
    size_statistics = {key: [0, []] for key in (10 ** n for n in range(1, 10))}
    for root, dirs, files in os.walk(catalog):
        for f_name in files:
            size = os.stat(os.path.join(root, f_name)).st_size
            key = [x for x in (10 ** n for n in range(1, 10)) if x >= size][0]
            ext = os.path.splitext(f_name)[1][1:]
            size_statistics[key][0] += 1
            if ext not in size_statistics[key][1]:
                size_statistics[key][1].append(ext)
    for k, val in size_statistics.items():
        size_statistics[k] = tuple(val)
    return size_statistics


curr_dir = os.getcwd()
summary = find_files(curr_dir)
with open(f'{os.path.basename(curr_dir)}_summary.json', 'w', encoding='utf-8') as f:  # сохранили в JSON
    json.dump(summary, f, ensure_ascii=False)
print(summary)
