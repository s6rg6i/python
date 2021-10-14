# 8.3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
# @type_logger
# def calc_cube(x):
#    return x ** 3
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

import datetime
import functools


def type_logger(func):
    @functools.wraps(func)
    def define_type(x):
        y = func(x)
        print(f'Декоратор "{define_type.__name__}" выполнил функцию: {func.__name__}({x}:'
              f' {type(x)}) значение функции: {y}: {type(y)}')
        return y

    return define_type


print(f'{"Декоратор с одним аргументом:":>50}')


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(5))


def type_logger_2(func):
    @functools.wraps(func)
    def define_type(*args):
        args[1][1] = datetime.datetime.strptime(args[1][1], "%d/%b/%Y:%X")
        for val in args:
            print(f'{val}: {type(val)}')
            if type(val) is list:
                for val1 in val:
                    print(f'{val1}: {type(val1)}')
        return func(*args)

    return define_type


@type_logger_2
def make_dict(key, x_dict):
    return {key: x_dict}


print(f'{"Декоратор с несколькими аргументами:":>50}')
# Декоратор меняет текстовое представление даты в datetime
d = make_dict('user', ['188.138.60.101', '17/may/2021:08:05:49', 30000])
print(d)

