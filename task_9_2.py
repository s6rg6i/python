# 9.2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
#
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_surface_weight(self, thickness, grav_1sm_m2):
        return self._width * self._length * grav_1sm_m2 * thickness


new_road = Road(5000, 20)
thickn, grav_m2 = 5, 25
mas = new_road.road_surface_weight(thickn, grav_m2)
print(f'{new_road._width} м*{new_road._length} м*{grav_m2} кг*{thickn} см = {mas // 1000}т')
