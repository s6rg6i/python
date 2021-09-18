# Задание 2 к 1 уроку

# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X)
MAX_NUMBER = 1000
DIVISIBLE_NUM = 7

odd_cubic_numbers = []

for i in range(1, MAX_NUMBER + 1, 2):
    odd_cubic_numbers.append(i ** 3)
print(f'2. Cписок из кубов нечётных чисел от 1 до {MAX_NUMBER}:\n {odd_cubic_numbers}')

# 2.a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!

sum_temp = 0
div_7_numbers = []

for val in odd_cubic_numbers:
    sum_temp = 0
    temp_val = val
    while temp_val != 0:  ## Подсчет суммы цифр числа
        sum_temp += temp_val % 10  # сумма цифр числа
        temp_val = temp_val // 10  # копия эл-та списка
    else:
        if sum_temp % DIVISIBLE_NUM == 0:  ## проверка кратности 7
            div_7_numbers.append(val)
sum_temp = 0
for val in div_7_numbers:  ## Подсчет суммы эл-тов в массиве
    sum_temp += val
print(f'2.a.Подсписок чисел, сумма цифр кот., кратна {DIVISIBLE_NUM}:\n {div_7_numbers}')
print(f'Сумма чисел подсписка: {sum_temp}')

# 2.b.К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
cubic_numbers_plus_17 = []
div_7_numbers.clear()
for val in odd_cubic_numbers:
    cubic_numbers_plus_17.append(val + 17)
for val in cubic_numbers_plus_17:
    sum_temp = 0
    temp_val = val
    while temp_val != 0:  ## Подсчет суммы цифр числа
        sum_temp += temp_val % 10  # сумма цифр числа
        temp_val = temp_val // 10  # копия эл-та списка
    else:
        # print(sum_temp)
        if sum_temp % DIVISIBLE_NUM == 0:  ## проверка кратности 7
            div_7_numbers.append(val)
sum_temp = 0
for val in div_7_numbers:
    sum_temp += val
print(f'2.b. Cписок из кубов нечётных чисел +17 от 1 до {MAX_NUMBER}:\n {cubic_numbers_plus_17}')
print(f'2.b. Подсписок чисел, сумма цифр кот., кратна {DIVISIBLE_NUM}:\n {div_7_numbers}')
print(f'Сумма чисел подсписка: {sum_temp}')

# * 2.c.Решить задачу под пунктом b, не создавая новый список.

sum_new = 0
for val in odd_cubic_numbers:
    val += 17
    sum_temp = 0  # сумма цифр числа
    temp_val = val  # копия эл-та списка
    while temp_val != 0:  ## Подсчет суммы цифр числа
        sum_temp += temp_val % 10
        temp_val = temp_val // 10
    else:
        if sum_temp % DIVISIBLE_NUM == 0:  ## проверка кратности
            sum_new += val

print(f'*2.c. Сумма чисел подсписка: {sum_new}')
