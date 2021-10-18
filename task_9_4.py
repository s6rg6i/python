# 9.4. Реализуйте базовый класс Car:
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# Методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        print(f'машина повернула {direction}')

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'зафиксировано превышение скорости на {self.speed - 60}')
        return self.speed


class SportCar(Car):  # чтобы не был пустым, добавил атрибут max_speed
    def __init__(self, speed, color, name, max_speed):
        self.max_speed = max_speed
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'зафиксировано превышение скорости на {self.speed - 40}')
        return self.speed


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town_car = TownCar(70, 'Бежевый "Titanium", металлик', 'Volkswagen Golf VII')
sport_car = SportCar(100, 'LeMans Blue', 'BMW M3', 350)
work_car = WorkCar(60, 'Серый базальт', 'Lada Largus')
police_car = PoliceCar(90, 'Белый с синей полосой', 'UAZ Hunter')

# печать всех атрибутов и выполнение всех методов созданных экземпляров классов
for cl, nam in zip((town_car, sport_car, work_car, police_car), ('town_car', 'sport_car', 'work_car', 'police_car')):
    print(f'{"-" * 10} Экземпляр класса {type(cl).__name__}: {nam}')
    print(f'speed:{cl.speed}, name:{cl.name}, color:{cl.color}, is_police:{cl.is_police}'
          f' {", max_speed:" + str(cl.max_speed) if isinstance(cl, SportCar) else ""}')
    print('Method go():', end=' ')
    cl.go()
    print('Method stop():', end=' ')
    cl.stop()
    print('Method turn():', end=' ')
    cl.turn('right')
    print(f'Method show_speed():', end=' ')
    print(cl.show_speed())
