from math import sqrt, pi, cos, sin

import point

SQRT2 = sqrt(2)
xSigns = [1, -1, -1, 1]
ySigns = [1, 1, -1, -1]


def canon(Xc, Yc, Ra, Rb, scene, pen):
    """
        Отрисовка окружности по
        каноническому уравнению
    """
    doubleA = Ra * Ra
    doubleB = Rb * Rb
    xRange = doubleA / sqrt(doubleA + doubleB)
    sqrtCoef = Rb / Ra
    x = 0

    while x <= xRange:
        y = int(round(sqrtCoef * sqrt(doubleA - x * x)))

        for i in range(4):
            point.drawPoint(
                Xc + xSigns[i] * x,
                Yc + ySigns[i] * y,
                scene,
                pen
            )

        x += 1

    y = 0
    yRange = doubleB / sqrt(doubleA + doubleB)
    sqrtCoef = Ra / Rb

    while y <= yRange:
        x = int(round(sqrtCoef * sqrt(doubleB - y * y)))

        for i in range(4):
            point.drawPoint(
                Xc + xSigns[i] * x,
                Yc + ySigns[i] * y,
                scene,
                pen
            )

        y += 1

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


def libfunc(Xc, Yc, Ra, Rb, scene, pen):
    """
        Отрисовка окружности
        библиотечной функции
    """
    scene.addEllipse(Xc - Ra, Yc - Rb, 2 * Ra, 2 * Rb, pen)
    print("Все ради этого", Xc, Yc, Ra, Rb)