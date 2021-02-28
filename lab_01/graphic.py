"""
    Модуль для вывода решения задачи:

    На  плоскости  дано  множество точек. Найти такой
    треугольник с вершинами в этих точках, у которого
    разность  максимального и минимального количества
    точек,  попавших  в каждый из 6-ти треугольников,
    образованных  пересечением  медиан,  максимальна.

    Сделать  в  графическом  режиме  вывод полученной
    картинки.
"""

import tkinter as tk
import copy
from math import atan2


def full_scale(canvas, points):
    """
        Преобразование координат для вывода
        изображения в максимально возможном
        масштабе
    """

    max_x = max(point[0] for point in points)
    min_x = min(point[0] for point in points)

    max_y = max(point[1] for point in points)
    min_y = min(point[1] for point in points)
    
    width = canvas.winfo_reqwidth()
    height = canvas.winfo_reqheight()

    x_coef = (width - width / 5) / (max_x - min_x)
    y_coef = (height - height / 5) / (max_y - min_y) 

    for point in points:
        point[0] = (point[0] - min_x) * x_coef + width / 10
        point[1] = height - ((point[1] - min_y) * y_coef + height / 10)


def create_point(canvas, point):
    """
        Функция отрисовки точки
    """
    size = canvas.winfo_height() / 150

    x1, y1 = (point[0] - size), (point[1] - size)
    x2, y2 = (point[0] + size), (point[1] + size)

    canvas.create_oval(x1, y1, x2, y2, fill="#476042")


def create_triangle(canvas, vertexes):
    """
        Функция отрисовки треугольника
    """

    canvas.create_polygon(*vertexes, outline="#000000", fill="", width=4)


def point_place(base_point, point):
    """
        Определение положения точки point
        относительно base_point
    """

    if (point[0] < base_point[0]):
        if (point[1] > base_point[1]):
            return 0

        return 3

    if (point[1] > base_point[1]):
        return 1

    return 2


def find_text_zone(zone1, zone2, points, i):
    """
        Поиск положения информации о точки
        по положениям двух других
    """
    if zone1 == zone2:
        return (zone1 + 2) % 4

    if abs(zone1 - zone2) % 2 == 1:
        code = zone1 * 2 + zone2
        if code in [1, 2]:
            return 4
        
        if code in [4, 5]:
            return 5

        if code in [7, 8]:
            return 6

        return 7

    cp_pnts = copy.deepcopy(points)
    fi = (i + 1) % 3
    si = (i + 2) % 3
    if zone1 > zone2:
        zone1, zone2 = zone2, zone1
        cp_pnts[fi][0], cp_pnts[si][0] = cp_pnts[si][0], cp_pnts[fi][0]
        cp_pnts[fi][1], cp_pnts[si][1] = cp_pnts[si][1], cp_pnts[fi][1]

    vec1 = (cp_pnts[fi][0] - cp_pnts[i][0], cp_pnts[fi][1] - cp_pnts[i][1])
    vec2 = (cp_pnts[si][0] - cp_pnts[i][0], cp_pnts[si][1] - cp_pnts[i][1])

    dot = vec1[0]*vec2[0] + vec1[1]*vec2[1]
    det = vec1[0]*vec2[1] - vec1[1]*vec2[0]
    angle = atan2(det, dot)

    if zone1 + zone2 == 4:
        if angle > 0:
            return 2
        return 0

    if angle > 0:
        return 1
    return 3


def update_place(x, y, size, zone):
    """
        Обновление координат положения текста
    """
    print("zone", zone)
    if zone == 0:
        return x - size, y + size
    elif zone == 1:
        return x + size, y + size
    elif zone == 2:
        return x + size, y - size
    elif zone == 3:
        return x - size, y - size
    elif zone == 4:
        return x, y - size
    elif zone == 5:
        return x - 1.5 * size, y
    elif zone == 6:
        return x, y + size
    elif zone == 7:
        return x + 1.3 * size, y


def print_point_info(canvas, nums, canvas_points, true_points):
    """
        Вывод номеров и координат точек
    """

    for i, point in enumerate(true_points):
        print("i =", i)
        info = "{:d}({:.2f},\n   {:.2f})".format(nums[i] + 1, point[0], point[1])

        x_place = canvas_points[i][0]
        y_place = canvas_points[i][1]

        point_place1 = point_place(canvas_points[i], canvas_points[(i + 1) % 3])
        point_place2 = point_place(canvas_points[i], canvas_points[(i + 2) % 3])

        zone = find_text_zone(point_place1, point_place2, canvas_points, i)

        size = canvas.winfo_reqheight() / 25

        x_place, y_place = update_place(x_place, y_place, size, zone)

        canvas.create_text(x_place, y_place, text=info,
                           anchor=tk.CENTER, font=('Dyuthi', 12))
        #canvas.create_rectangle(canvas.bbox(info), fill="black")
