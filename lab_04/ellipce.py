def canon(Xc, Yc, Ra, Rb, scene):
    """
        Отрисовка окружности по
        каноническому уравнению
    """
    print("Ммм, канон!", Xc, Yc, Ra, Rb)


def parametric(Xc, Yc, Ra, Rb, scene):
    """
        Отрисовка окружности по
        параметрическому уравнению
    """
    print("Все связано", Xc, Yc, Ra, Rb)


def brezenham(Xc, Yc, Ra, Rb, scene):
    """
        Отрисовка окружности
        алгоритмом Брезенхема
    """
    print("От него не спрятаться", Xc, Yc, Ra, Rb)


def midpoint(Xc, Yc, Ra, Rb, scene):
    """
        Отрисовка окружности
        алгоритмом средней точки
    """
    print("Золотая середина", Xc, Yc, Ra, Rb)


def libfunc(Xc, Yc, Ra, Rb, scene):
    """
        Отрисовка окружности
        библиотечной функции
    """
    scene.addEllipse(Xc - Ra, Yc - Rb, 2 * Ra, 2 * Rb)
    print("Все ради этого", Xc, Yc, Ra, Rb)