""" Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
Решить задачу не создавая новый список (как говорят, in place). """

base_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
add_plus = ''   # '+', если число начинается с +
str0 = ''

for val in base_list:
    add_plus = ''
    if val.startswith('+'):
        add_plus = '+'
        val = val.replace('+', '0')
    str0 += '"' + add_plus + val.zfill(2) + '" ' if val.isdigit() else val + ' '
print(f'Исходный список:{base_list}')
print(f'Результат:{str0}')
