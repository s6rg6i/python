# 8.4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
# и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)  # 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
#
# Примечание: сможете ли вы замаскировать работу декоратора?

import functools


def val_checker(f_arg=None):
    def val_checker_dec(func):
        @functools.wraps(func)
        def wrapper(x):
            print(f'Определение имени функции <wrapper.__name__> внутри <wrapper()>: {wrapper.__name__}')
            print(f'Определение имени функции <func.__name__> внутри <wrapper()>: {func.__name__}')
            if f_arg is None:
                return func(x)
            if not f_arg(x):
                raise ValueError(f'Wrong value {x}')
            return func(x)

        return wrapper

    return val_checker_dec


@val_checker(lambda x: x > 0)
def calc_cube(x):
    print(f'Определение имени функции<calc_cube.__name__> внутри <calc_cube()>: {calc_cube.__name__}')
    return x ** 3


#           до использования декоратора wraps из модуля functools:
# Определение имени функции <wrapper.__name__> внутри <wrapper()>: wrapper
# Определение имени функции <func.__name__> внутри <wrapper()>: calc_cube
# Определение имени функции<calc_cube.__name__> внутри <calc_cube()>: wrapper
#           после использования декоратора wraps из модуля functools:
# Определение имени функции <wrapper.__name__> внутри <wrapper()>: calc_cube
# Определение имени функции <func.__name__> внутри <wrapper()>: calc_cube
# Определение имени функции<calc_cube.__name__> внутри <calc_cube()>: calc_cube

print(calc_cube(5))
print(calc_cube(-5))
