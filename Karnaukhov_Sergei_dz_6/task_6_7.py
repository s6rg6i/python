# 6.7. *(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
# передаём ему номер записи и новое значение. При этом файл не должен читаться целиком — обязательное требование.
# Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.
import sys
import os

if len(sys.argv) != 3 or not sys.argv[1].isnumeric() or int(sys.argv[1]) < 1:
    print('Необходимо 2 параметра: номер записи,начиная с 1-й, и новое значение')
    exit(1)
idx_0, val_0 = int(sys.argv[1]) - 1, sys.argv[2] + '\n'
if not os.path.exists('bakery.csv'):
    print('не найден файл <bakery.csv>')
    exit(1)
if os.path.exists('tmp.tmp'):
    os.remove('tmp.tmp')  # если вр.файл существует - удалить
os.rename('bakery.csv', 'tmp.tmp')  # переименовать во временный
is_edited = False
with open('bakery.csv', 'w', encoding='utf-8') as new_file:  # создать новый
    with open('tmp.tmp', 'r', encoding='utf-8') as tmp_file:
        for i, s in enumerate(tmp_file):
            if i == idx_0:
                s, is_edited = val_0, True  # если нужный номер строки - заменяем
            new_file.write(s)
os.remove('tmp.tmp')  # удаляем временный
if not is_edited:
    print(f'Не найдена строка номер {idx_0 + 1} в файле <bakery.csv>')
    exit(1)
exit(0)
