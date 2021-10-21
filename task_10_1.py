# 10.1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#        3х2:          3х3:            2х4:
#      31  22        3  5 32        3  5  8  3
#      37  43        2  4  6        8  3  7  1
#      51  86       -1 64 -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и пр.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix_check()  # проверяем, что тип matrix list, все его эл-ты list и они равного размера
        self.m_rows = len(self.matrix)
        self.n_columns = len(self.matrix[0])

    def matrix_check(self):
        if type(self.matrix) is not list \
                or any(type(x) is not list for x in self.matrix) \
                or any(len(x) != len(self.matrix[0]) for x in self.matrix):
            raise ValueError('Invalid matrix')

    def get_matrix_dimension(self):
        return [self.m_rows, self.n_columns]

    def __str__(self):
        # конкатенация списков(sum) в строки (map); строка с макс. длиной(max); +2 пробела
        xx_max = len(max(list(map(str, sum(self.matrix, []))), key=len)) + 2  # длина поля для вывода значений матрицы
        s = '\n'.join([''.join([(str(i)).rjust(xx_max) for i in x]) for x in self.matrix])
        return f' матрица [{self.m_rows}x{self.n_columns}]\n{s}'

    def __add__(self, other):
        if self.get_matrix_dimension() != other.get_matrix_dimension():
            return None  # сложение матриц возможно только одной размерности
        return Matrix([[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.matrix, other.matrix)])


matrix1 = Matrix([[0, 3, 4], [100, 200, 400], [10, 20, 30], [-20, -40, -80]])
matrix2 = Matrix([[10, 11, 12], [-20, -21, -22], [100, 200, 300], [100, 200, 300]])
print(f'matrix1:{matrix1}\n matrix2:{matrix2}\n matrix1 + matrix2:{matrix1 + matrix2}')
