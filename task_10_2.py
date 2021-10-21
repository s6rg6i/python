# 10.2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. # Основная сущность (класс)
# этого проекта — одежда, которая может иметь определённое # название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod


class AbstractClassClothes(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(AbstractClassClothes):
    def __init__(self, size):
        self.size = size

    @property
    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(AbstractClassClothes):
    def __init__(self, height):
        self.height = height

    @property
    def fabric_consumption(self):
        return 2 * self.height + 0.3


class Clothes:
    def __init__(self):
        self.clothes = []

    def __str__(self):
        s = ''
        for cl in self.clothes:
            for val in cl.__dict__:
                s += f'{type(cl).__name__}({val}={cl.__dict__[val]}) consumption: {cl.fabric_consumption:.2f}\n'
        return f'{s}'

    def add_item_of_clothing(self, item):
        self.clothes.append(item)

    @property
    def total_consumption(self):
        total = 0
        for cl in self.clothes:
            total += cl.fabric_consumption
        return total


clothes = Clothes()
clothes.add_item_of_clothing(Suit(3))
clothes.add_item_of_clothing(Coat(5))
clothes.add_item_of_clothing(Suit(10))
print(clothes)
print(f'Total consumption : {clothes.total_consumption:.2f}')
