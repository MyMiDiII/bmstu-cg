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


def full_scale(canvas, points):
    """
        Преобразование координат для вывода
        изображения в максимально возможном
        масштабе
    """

    max_x = max(point[0] for point in points)
    min_x = min(points, key=lambda x: x[0])[0]

    max_y = max(points, key=lambda x: x[1])[1]
    min_y = min(points, key=lambda x: x[1])[1]

    print(canvas.winfo_reqwidth())
    print(canvas.winfo_reqheight())
    x_coef = (canvas.winfo_reqwidth() - canvas.winfo_reqwidth() / 5) / (max_x - min_x)
    y_coef = (canvas.winfo_reqheight() - canvas.winfo_reqheight() / 5) / (max_y - min_y) 
    print(x_coef, y_coef)

    for point in points:
        point[0] = (point[0] - min_x) * x_coef + canvas.winfo_reqwidth() / 10
        point[1] = canvas.winfo_reqheight() - ((point[1] - min_y) * y_coef + canvas.winfo_reqheight() / 10)


def create_point(canvas, point):
    """
        Функция отрисовки точки
    """
    # print(point)
    size = canvas.winfo_height() / 150

    x1, y1 = (point[0] - size), (point[1] - size)
    x2, y2 = (point[0] + size), (point[1] + size)

    canvas.create_oval(x1, y1, x2, y2, fill="#476042")


def create_triangle(canvas, vertexes):
    """
        Функция отрисовки треугольника
    """

    canvas.create_polygon(*vertexes, outline="#000000", fill="#ffffff", width=4)


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


def print_point_info(canvas, nums, canvas_points, true_points):
    """
        Вывод номеров и координат точек
    """

    for i, point in enumerate(true_points):
        info = "{:3d}({:6.2f}, {:6.2f})".format(nums[i] + 1, point[0], point[1])

        x_place = canvas_points[i][0] 
        y_place = canvas_points[i][1]

        point_place1 = point_place(canvas_points[i], canvas_points[(i + 1) % 3])
        point_place2 = point_place(canvas_points[i], canvas_points[(i + 2) % 3])

        print('pp1', point_place1)
        print('pp2', point_place2)

        zone = 3
        if point_place1 == point_place2:
            zone = (point_place1 + 2) % 4


        if zone == 0:
            print('zone', 0)
            x_place -= 50
            y_place += 50
        elif zone == 1:
            print('zone', 1)
            x_place += 50
            y_place += 50
        elif zone == 2:
            print('zone', 2)
            x_place += 50
            y_place -= 50
        else:
            print('zone', 3)
            x_place -= 50
            y_place -= 50

        print(x_place, y_place)

        canvas.create_text(x_place, y_place, text=info, font=('Courier', 10))
