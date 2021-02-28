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


def fild_ratio_point(point1, point2, m, n):
    """
        Поиск координат точки, которая делит отрезок
        point1 point2 в отношении m к n, считая от point1
    """
    ratio_point = []

    for i in range(len(point1)):
        ratio_point.append((n * point1[i] + m * point2[i]) / (n + m))

    return ratio_point


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
        Поиск точек, находящихся внутри треугольника
    """
    in_points = []

    for point in points:
        if (check_line((vertexes[0], vertexes[1]), vertexes[2], point)
            and check_line((vertexes[0], vertexes[2]), vertexes[1], point)
            and check_line((vertexes[1], vertexes[2]), vertexes[0], point)
        ):
            in_points.append(tuple(point))

    return in_points


def find_diff(triangle, points):
    """
        Поиск разности в заданном треугольнике
    """

    if not is_triangle(*triangle):
        return -1, (), []

    middles = [0, 0, 0]

    for i in range(3):
        middles[i] = fild_ratio_point(triangle[i % 2],
                                      triangle[(i + 1) // 2 + 1],
                                      1, 1)
    medians_point = fild_ratio_point(triangle[0], middles[1], 2, 1)

    max_num = 0
    max_ind = 0

    min_num = len(points)
    min_ind = 0

    all_in_points = set()

    for i in range(6):
        # print("треугольник", i)
        # print(triangle[(i + 1) % 6 // 2])
        # print(middles[i // 2])
        # print(medians_point)
        vertexes = (triangle[(i + 1) % 6 // 2],
                    middles[i // 2],
                    medians_point)
        in_points = get_num(vertexes, points)

        for in_point in in_points:
            # print(in_point)
            all_in_points.add(in_point)

        # print("in_points", in_points)
        if max_num < len(in_points):
            max_num = len(in_points)
            max_ind = i

        if min_num > len(in_points):
            min_num = len(in_points)
            min_ind = i

    if min_ind == max_ind and max_num == min_num:
        min_ind = (min_ind + 1) % 6
    # print("min/max", min_num, max_num)
    # print("in_points", all_in_points)
    return max_num - min_num, (max_ind, min_ind), all_in_points


def solve_problem(points):
    """
        Решение задачи
    """
    length = len(points)

    answer = {'max_diff': -1, 'max_min': (),'in_points': [],
              'nums': (), 'triangle': ()}

    for first in range(length - 2):
        for second in range(1, length - 1):
            for third in range(2, length):
                # print("num", first, second, third)
                triangle = (points[first], points[second], points[third])
                # print("find_diff", find_diff(triangle, points))
                cur_diff, max_min, in_points = find_diff(triangle, points)
                # print("cur_diff", cur_diff)

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


def call_solve_problem(points_table, canvas):
    """
        Вызов функции решения задачи
    """

    points_arr = create_arr(points_table)

    if len(points_arr) == 0:
        msg.create_errorbox('Пустой список точек', EMPTY_TABLE)
        return
    elif len(points_arr) < 3:
        msg.create_errorbox('Недостаточно точек', LESS3)
        return
    answer = solve_problem(points_arr)

    if answer["max_diff"] == -1:
        msg.create_errorbox('Нет треугольников', NO_TRIANGLES)
        return

    canvas.delete('all')
    msg.create_infobox('Решение', form_text(answer))

    triangle_copy = copy.deepcopy(answer["triangle"])
    graphic.full_scale(canvas, answer["triangle"])
    graphic.full_scale(canvas, answer["in_points"])

    middles = [0, 0, 0]
    for i in range(3):
        middles[i] = fild_ratio_point(answer["triangle"][i % 2],
                                      answer["triangle"][(i + 1) // 2 + 1],
                                      1, 1)
    medians_point = fild_ratio_point(answer["triangle"][0], middles[1], 2, 1)

    for i, ind in enumerate(answer["max_min"]):
        canvas.create_polygon(answer["triangle"][(ind + 1) % 6 // 2], middles[ind // 2], medians_point,
                              fill="yellow" if i else "red")

    graphic.print_point_info(canvas, answer["nums"], answer["triangle"], triangle_copy)
    graphic.create_triangle(canvas, answer["triangle"])

    for i in range(3):
        canvas.create_line(answer["triangle"][(i + 2) % 3], middles[i], width=4)

    for point in answer["in_points"]:
        graphic.create_point(canvas, point)
