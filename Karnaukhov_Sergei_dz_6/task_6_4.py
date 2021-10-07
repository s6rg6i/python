# 6.4. *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется,
# не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Только теперь не нужно создавать словарь с данными. Вместо этого нужно сохранить объединенные данные
# в новый файл (users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

from itertools import zip_longest

with open('users.csv', encoding='utf-8') as file_1:
    with open('hobby.csv', encoding='utf-8') as file_2:
        with open('users_hobby.txt', 'w', encoding='utf-8') as file_out:
            num_lines_users = sum(1 for line in file_1)  # пробегаем по строкам генератором
            num_lines_hobby = sum(1 for line in file_2)  # и подсчитываем к-во строк в ф файлах
            if num_lines_users < num_lines_hobby:
                print('В файле, хранящем данные о хобби, записей > чем в файле с ФИО')
                exit(1)
            file_1.seek(0)
            file_2.seek(0)  # Возвращаем указатель на начало
            for user, hobby in zip_longest(file_1, file_2):  # Формируем выходной файл
                user = user.strip() if user is not None else 'None'
                hobby = hobby.strip().lower() if hobby is not None else 'None'
                file_out.write(f'{user}: {hobby}\n')
print('Создан файл, превышающий объём ОЗУ, <users_hobby.txt>')
