def canon(xc, yc, R, scene, pen):
    """
        Отрисовка окружности по
        каноническому уравнению
    """
    print("Ммм, канон!", xc, yc, R, scene)


def parametric(xc, yc, R, scene, pen):
    """
        Отрисовка окружности по
        параметрическому уравнению
    """
    print("Все связано", xc, yc, R, scene)


def brezenham(xc, yc, R, scene, pen):
    """
        Отрисовка окружности
        алгоритмом Брезенхема
    """
    print("От него не спрятаться", xc, yc, R, scene)


def midpoint(xc, yc, R, scene, pen):
    """
        Отрисовка окружности
        алгоритмом средней точки
    """
    print("Золотая середина", xc, yc, R, scene)


def libfunc(xc, yc, R, scene, pen):
    """
        Отрисовка окружности
        библиотечной функции
    """
    scene.addEllipse(xc - R, yc - R, 2 * R, 2 * R, pen)
    print("Все ради этого", xc, yc, R, scene)