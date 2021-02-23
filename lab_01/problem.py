"""
    Модуль решения задачи:

    На  плоскости  дано  множество точек. Найти такой
    треугольник с вершинами в этих точках, у которого
    разность  максимального и минимального количества
    точек,  попавших  в каждый из 6-ти треугольников,
    образованных  пересечением  медиан,  максимальна.

    Сделать  в  графическом  режиме  вывод полученной
    картинки.
"""

import messages as msg


EPS = 1e-6


def create_arr(points_table):
    """
        Создание списка из данных treeview
    """

    points = []
    for child in points_table.get_children():
        points.append([float(x) for x in points_table.item(child)["values"]])

    return points


def is_triangle(point1, point2, point3):
    """
        Проверка, можно ли заданных точках
        построить треугольник
    """

    return not (abs((point3[0] - point1[0])
                  * (point2[1] - point1[1])
                  - (point2[0] - point1[0])
                  * (point3[1] - point1[1]))
                < EPS)


def ratio_point_1D(x1, x2, m, n):
    """
        Поиск координаты точки прямой, которая делит
        отрезок x1x2 в отношении m к n, считая от
        x1
    """

    return (n * x1 + m * x2) / (n + m)


def ratio_point_2D(point1, point2, m, n):
    """
        Поиск координат точки плоскости, которая делит 
        отрезок point1 point2 в отношении m к n, считая 
        от point1
    """
    return (ratio_point_1D(point1[0], point2[0], m, n),
            ratio_point_1D(point1[1], point2[1], m, n))


def find_diff(triangle, points):
    """
        Поиск разности в заданном треугольнике
    """

    if not is_triangle(points[triangle[0]],
                       points[triangle[1]],
                       points[triangle[2]]
                      ):
        return -1

    middle = ratio_point_2D(points[triangle[1]], points[triangle[2]], 1, 1)
    medians = ratio_point_2D(points[triangle[0]], middle, 2, 1)

    return 10


def solve_problem(points):
    """
        Решение задачи
    """
    length = len(points)

    if length < 3:
        return -1

    answer = {'max_diff' : -1, 'triangle' : ()}

    for first in range(length - 2):
        for second in range(1, length - 1):
            for third in range(2, length): 
                cur_diff = find_diff((first, second, third), points)
                
                if cur_diff > answer['max_diff']:
                    answer['max_diff'] = cur_diff
                    answer['triangle'] = (first, second, third)

    return answer


def call_solve_problem(points_table):
    """
        Вызов функции решения задачи
    """

    points_arr = create_arr(points_table)
    answer = solve_problem(points_arr)
    print(answer)


