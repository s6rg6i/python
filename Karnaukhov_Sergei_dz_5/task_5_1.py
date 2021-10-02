# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next()
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...


def odd_nums(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


odd_to_15 = odd_nums(15)
for x in odd_to_15:
    print(x)
print('Следующая итерация next() вызовет ошибку')
next(odd_to_15)
