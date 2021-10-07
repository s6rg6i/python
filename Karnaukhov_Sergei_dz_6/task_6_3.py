# 6.3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий
# из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
# чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
#       Иванов,Иван,Иванович
#       Петров,Петр,Петрович
# Фрагмент файла с данными о хобби  (hobby.csv):
#       скалолазание,охота
#       горные лыжи

from itertools import zip_longest
import json
import sys

file_users = open('users.csv', 'r', encoding='utf-8')
f_users = file_users.read()
file_users.close()

file_hobby = open('hobby.csv', 'r', encoding='utf-8')
f_hobby = file_hobby.read()
file_hobby.close()

users = f_users.replace(',', ' ').split('\n')
hobbies = f_hobby.lower().split('\n')

if len(hobbies) > len(users):
    sys.exit(1)  # записей о хобби > записей о ФИО : ошибка по условию задачи

user_hobby_dict = {key: val for key, val in zip_longest(users, hobbies) if key is not None}
# Сохраним словарь в JSON файл
with open('hobby_users.json', 'w', encoding='utf-8') as f:  # словарь в JSON формат
    f.write(json.dumps(user_hobby_dict, ensure_ascii=False))  # ensure_ascii=false - для читабельности русских симв.
# Извлечем из JSON файла словарь
with open('hobby_users.json', 'r', encoding='utf-8') as f:
    user_hobby_dict1 = json.load(f)  # из JSON файла в новый словарь
if user_hobby_dict == user_hobby_dict1:  # сравниваем словари
    print('Словари исходный и полученный из JSON файла совпадают')
print(f'user_hobby_dict (id={id(user_hobby_dict)}):{user_hobby_dict}')
print(f'user_hobby_dict1 (id={id(user_hobby_dict1)}:{user_hobby_dict1}')
