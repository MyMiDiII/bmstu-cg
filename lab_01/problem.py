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

import copy

import messages as msg
import graphic


EPS = 1e-6

LESS3 = ('Недостаточное количество!\n'
         + 'Добавьте хотя бы 3 точки!')
EMPTY_TABLE = 'Список точек пуст!\nДобавьте точки!'
NO_TRIANGLES = ('На заданных точках нельзя построить\n'
                + 'ни один треугольник, так как точки\n'
                + 'либо лежат на одной прямой, либо\n'
                + 'совпадают!')
HINT_TEXT = ('красный – треугольник с максимальным\n'
             + '          количеством точек,\n'
             + 'желтый  – с минимальным.')


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

    return not abs(vector_prod(point1, point2, point3)) < EPS


def check_line(line, vertex, point):
    """
        Проверка, лежат ли точка и вершина
        по одну сторону от прямой, заданной
        двумя другими вершинами
    """

    cond_expr = vector_prod(*line, vertex) * vector_prod(*line, point)

    return cond_expr > 0 or abs(cond_expr) < EPS


def get_num(vrts, points):
    """
        Поиск точек, находящихся внутри треугольника
    """
    in_points = []

    for point in points:
        if (check_line((vrts[0], vrts[1]), vrts[2], point)
                and check_line((vrts[0], vrts[2]), vrts[1], point)
                and check_line((vrts[1], vrts[2]), vrts[0], point)):
            in_points.append(tuple(point))

    return in_points


def fild_ratio_point(point1, point2, m, n):
    """
        Поиск координат точки, которая делит отрезок
        point1 point2 в отношении m к n, считая от point1
    """
    ratio_point = []

    for i in range(len(point1)):
        ratio_point.append((n * point1[i] + m * point2[i]) / (n + m))

    return ratio_point


def find_middles(triangle):
    """
        Поиск координат середин сторон
    """
    middles = [0, 0, 0]

    for i in range(3):
        middles[i] = fild_ratio_point(triangle[i % 2],
                                      triangle[(i + 1) // 2 + 1],
                                      1, 1)

    return middles


def find_diff(triangle, points):
    """
        Поиск разности в заданном треугольнике
    """

    if not is_triangle(*triangle):
        return -1, (), []

    middles = find_middles(triangle)
    medians_point = fild_ratio_point(triangle[0], middles[1], 2, 1)

    max_num = 0
    max_ind = 0

    min_num = len(points)
    min_ind = 0

    all_in_points = set()

    for i in range(6):
        vertexes = (triangle[(i + 1) % 6 // 2],
                    middles[i // 2],
                    medians_point)
        in_points = get_num(vertexes, points)

        for in_point in in_points:
            all_in_points.add(in_point)

        if max_num < len(in_points):
            max_num = len(in_points)
            max_ind = i

        if min_num > len(in_points):
            min_num = len(in_points)
            min_ind = i

    if min_ind == max_ind and max_num == min_num:
        min_ind = (min_ind + 1) % 6

    return max_num - min_num, (max_ind, min_ind), all_in_points


def solve_problem(points):
    """
        Решение задачи
    """
    length = len(points)

    answer = {'max_diff': -1, 'max_min': (), 'in_points': [],
              'nums': (), 'triangle': ()}

    for first in range(length - 2):
        for second in range(1, length - 1):
            for third in range(2, length):
                triangle = (points[first], points[second], points[third])
                cur_diff, max_min, in_points = find_diff(triangle, points)

                if cur_diff > answer['max_diff']:
                    answer['max_diff'] = cur_diff
                    answer['in_points'] = [list(x) for x in in_points]
                    answer['nums'] = (first, second, third)
                    answer['triangle'] = triangle
                    answer['max_min'] = max_min

    return answer


def form_text(answer):
    """
        Формирование сообщения с решением
    """
    text = ('Треугольник с максимальной искомой\nразностью, '
            + 'равной {:3d}, построен на\nточках:\n'.format(answer["max_diff"])
            )

    for i, point in enumerate(answer["triangle"]):
        text += '     %3d(' % (answer["nums"][i] + 1)
        text += '%6.2f, ' % (point[0])
        text += '%6.2f)\n' % (point[1])

    return text


def is_correct_len(points_arr):
    """
        Проверка количества добавленных точек
    """
    if len(points_arr) == 0:
        msg.create_errorbox('Пустой список точек', EMPTY_TABLE)
        return 0

    if len(points_arr) < 3:
        msg.create_errorbox('Недостаточно точек', LESS3)
        return 0

    return 1


def are_triangles(answer):
    """
        Проверка на наличие треугольников в ответе
    """
    if answer["max_diff"] == -1:
        msg.create_errorbox('Нет треугольников', NO_TRIANGLES)
        return 0

    return 1


def call_solve_problem(points_table, canvas):
    """
        Вызов функции решения задачи
    """

    msg.destroy_toplevels()
    points_arr = create_arr(points_table)

    if not is_correct_len(points_arr):
        return

    answer = solve_problem(points_arr)

    if not are_triangles(answer):
        return

    canvas.delete('all')
    msg.create_infobox('Решение', form_text(answer))
    msg.create_hintbox('Обозначения', HINT_TEXT)

    triangle_copy = copy.deepcopy(answer["triangle"])
    graphic.full_scale(canvas, answer["triangle"])
    graphic.full_scale(canvas, answer["in_points"])

    middles = find_middles(answer["triangle"])
    medians_point = fild_ratio_point(answer["triangle"][0], middles[1], 2, 1)

    graphic.create_max_min_triangles(canvas, answer, middles, medians_point)
    graphic.create_triangle(canvas, answer["triangle"])
    graphic.create_medians(canvas, answer["triangle"], middles)
    graphic.print_point_info(canvas, answer["nums"],
                             answer["triangle"], triangle_copy)
    graphic.create_points(canvas, answer["in_points"])
