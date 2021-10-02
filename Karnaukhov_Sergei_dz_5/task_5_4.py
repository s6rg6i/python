# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# Подсказка: использовать возможности python, изученные на уроке.
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.

from time import perf_counter


def previous(li):   # Генератор для возврата предыдущего значения списка
    x0 = li[0]
    for x in li:
        yield x0
        x0 = x


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# оптимально по памяти в случае больших массивов:
result = [x1 for x0, x1 in zip(previous(src), src) if x1 > x0]
print(result)

# оптимально по скорости (?) в случае больших массивов:
result = [x1 for x0, x1 in zip(src, src[1:]) if x1 > x0]
print(result)

print('Тест скорост для 10**6 повторений: 1 для генератора, 2 для среза списка')

start = perf_counter()
for i in range(10**6):
    result = [x1 for x0, x1 in zip(previous(src), src) if x1 > x0]
print(t0 := (perf_counter() - start))

start = perf_counter()
for i in range(10**6):
    result = [x1 for x0, x1 in zip(src, src[1:]) if x1 > x0]
print(t1 := (perf_counter() - start))

print(f'генератор медленнее среза списка ~ в {(t0/t1):.2f} раза')
