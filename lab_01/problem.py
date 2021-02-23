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


def vector_prod(point1, point2, point3):
    """
        Поиск модуля векторного произведения
    """
    return ((point3[0] - point1[0]) * (point2[1] - point1[1])
            - (point2[0] - point1[0]) * (point3[1] - point1[1]))


def is_triangle(point1, point2, point3):
    """
        Проверка, можно ли заданных точках
        построить треугольник
    """

    return not (abs(vector_prod(point1, point2, point3)) < EPS)


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


def check_line(line, vertex, point):
    """
        Проверка, лежат ли точка и вершина
        по одну сторону от прямой, заданной
        двумя другими вершинами
    """

    cond_expr = vector_prod(*line, vertex) * vector_prod(*line, point)

    return cond_expr > 0 or abs(cond_expr) < EPS


def get_num(vertexes, points):
    """
        Поиск количества точек, находящихся
        внутри треугольника
    """
    num = 0

    for point in points:
        if (check_line((vertexes[0], vertexes[1]), vertexes[2], point)
            and check_line((vertexes[0], vertexes[2]), vertexes[1], point)
            and check_line((vertexes[1], vertexes[2]), vertexes[0], point)
            ):
            num += 1

    return num


def find_diff(triangle, points):
    """
        Поиск разности в заданном треугольнике
    """

    if not is_triangle(*triangle):
        return -1

    middles = [0, 0, 0]

    for i in range(3):
        middles[i] = ratio_point_2D(triangle[i % 2],
                                    triangle[(i + 1) // 2 + 1],
                                    1, 1)
        print(i // 2, i + 1 - i // 2) 
    medians_point = ratio_point_2D(triangle[0], middles[1], 2, 1)
    print(medians_point)

    max_num = 0
    min_num = len(points)

    for i in range(6):
        print("треугольник", i)
        #print(triangle[(i + 1) % 6 // 2])
        #print(middles[i // 2])
        #print(medians_point)
        vertexes = (triangle[(i + 1) % 6 // 2],
                    middles[i // 2],
                    medians_point) 
        in_points_num = get_num(vertexes, points)
        print("in_points_num", in_points_num)
        max_num = max(in_points_num, max_num)
        min_num = min(in_points_num, min_num)

    print("min/max", min_num, max_num)
    return max_num - min_num


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
                print("num", first, second, third)
                triangle = (points[first], points[second], points[third])
                cur_diff = find_diff(triangle, points)
                print("cur_diff", cur_diff)
                
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


