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

    x1, y1 = (point[0] - 5), (point[1] - 5)
    x2, y2 = (point[0] + 5), (point[1] + 5)

    canvas.create_oval(x1, y1, x2, y2, fill="#476042")


def create_triangle(canvas, vertexes):
    """
        Функция отрисовки треугольника
    """

    canvas.create_polygon(*vertexes, outline="#000000", fill="#ffffff", width=4)


def print_point_info(canvas, nums, canvas_points, true_points):
    """
        Вывод номеров и координат точек
    """

    for i, point in enumerate(true_points):
        info = "{:3d}({:6.2f}, {:6.2f})".format(nums[i] + 1, point[0], point[1])
        canvas.create_text(canvas_points[i], text=info)
