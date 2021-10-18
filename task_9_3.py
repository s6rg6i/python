# 9.3. Реализовать базовый класс Worker (работник):
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия»,
# например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker; в классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.


class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


pos_1 = Position('Robert', 'Black', 'waiter', {"wage": 3000, "bonus": 500})
pos_2 = Position('Anna', 'White', 'chef', {"wage": 6000, "bonus": 4000})
print(pos_1.name, pos_1.surname, pos_1.position, pos_1._income)
print(f'{pos_1.get_full_name()} /{pos_1.position}/ income: {pos_1.get_total_income()}')
print(pos_2.name, pos_2.surname, pos_2.position, pos_2._income)
print(f'{pos_2.get_full_name()} /{pos_2.position}/ income: {pos_2.get_total_income()}')


