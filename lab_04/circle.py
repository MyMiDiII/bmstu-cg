from math import sqrt, pi, cos, sin

import draw

SQRT2 = sqrt(2)

def canon(xc, yc, R, scene, pen):
    """
        Отрисовка окружности по
        каноническому уравнению
    """
    if not R:
        draw.drawPoint(xc, yc, scene, pen)
        return

    xRange = int(round(R / SQRT2))
    rSecPow = R * R
    x = 0

    while x <= xRange:
        y = int(round(sqrt(rSecPow - x * x)))

        draw.drawCirclePoints(x, y, xc, yc, scene, pen)

        x += 1


def parametric(xc, yc, R, scene, pen):
    """
        Отрисовка окружности по
        параметрическому уравнению
    """
    if not R:
        draw.drawPoint(xc, yc, scene, pen)
        return

    tRange = pi / 4
    tStep = 1 / R
    t = 0

    while t < tRange + tStep:
        x = int(round(R * cos(t)))
        y = int(round(R * sin(t)))

        draw.drawCirclePoints(x, y, xc, yc, scene, pen)

        t += tStep


def brezenham(xc, yc, R, scene, pen):
    """
        Отрисовка окружности
        алгоритмом Брезенхема
    """
    x = 0
    y = R
    capDelta = 2 * (1 - R)

    while y >= x:
        draw.drawCirclePoints(x, y, xc, yc, scene, pen)

        # TODO выделить функции
        if capDelta < 0:
            delta = 2 * capDelta + 2 * y - 1

            if delta <= 0:
                x += 1
                capDelta = capDelta + 2 * x + 1
            else:
                x += 1
                y -= 1
                capDelta = capDelta + 2 * x - 2 * y + 2

        elif capDelta > 0:
            delta = 2 * capDelta - 2 * x - 1

            if delta <= 0:
                x += 1
                y -= 1
                capDelta = capDelta + 2 * x - 2 * y + 2
            else:
                y -= 1
                capDelta = capDelta - 2 * y + 1

        else:
            x += 1
            y -= 1
            capDelta = capDelta + 2 * x - 2 * y + 2


def midpoint(xc, yc, R, scene, pen):
    """
        Отрисовка окружности
        алгоритмом средней точки
    """
    x = 0
    y = R
    trialFunc = 1.25 - R

    while x <= y:
        draw.drawCirclePoints(x, y, xc, yc, scene, pen)
        
        x += 1

        if trialFunc > 0:
            y -= 1
            trialFunc -= 2 * y

        trialFunc = trialFunc + 2 * x + 1


def libfunc(xc, yc, R, scene, pen):
    """
        Отрисовка окружности
        библиотечной функции
    """
    scene.addEllipse(xc - R, yc - R, 2 * R, 2 * R, pen)