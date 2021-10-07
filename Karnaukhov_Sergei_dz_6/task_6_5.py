# 6.5. **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
# задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.

from itertools import zip_longest
import sys
import os


if len(sys.argv) != 4:
    print('Необходимо 3 параметра: <имя 1 вх.файла> <имя 2 вх.файла> <имя вых.файла>')
    exit(1)
if not os.path.exists(sys.argv[1]) or not os.path.exists(sys.argv[2]):
    print('входные файлы не найдены')
    exit(1)
if os.path.exists(sys.argv[3]):
    print('Выходной файл существует и может быть затерт')
    exit(1)
s_file_1, s_file_2, s_file_out = sys.argv[1:]
with open(s_file_1, encoding='utf-8') as file_1:
    with open(s_file_2, encoding='utf-8') as file_2:
        with open(s_file_out, 'w', encoding='utf-8') as file_out:
            num_lines_users = sum(1 for line in file_1)  # пробегаем по строкам генератором
            num_lines_hobby = sum(1 for line in file_2)  # и подсчитываем к-во строк в ф файлах
            if num_lines_users < num_lines_hobby:
                print('В файле, хранящем данные о хобби, записей > чем в файле с ФИО')
                exit(1)
            file_1.seek(0)
            file_2.seek(0)  # Возвращаем указатель на начало

            for user, hobby in zip_longest(file_1, file_2):
                user = user.strip() if user is not None else 'None'
                hobby = hobby.strip().lower() if hobby is not None else 'None'
                file_out.write(f'{user}: {hobby}\n')
print(f'Успешно создан файл <{s_file_out}>')


