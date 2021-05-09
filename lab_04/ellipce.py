from math import sqrt, pi, cos, sin

import draw


def canon(Xc, Yc, Ra, Rb, scene, pen, drawFlag=True):
    """
        Отрисовка эллипса по
        каноническому уравнению
    """

    sqrA = Ra * Ra
    sqrB = Rb * Rb

    xRange = (int(round(sqrA / sqrt(sqrA + sqrB)))
              if sqrA or sqrB else 0)
    sqrtCoef = Rb / Ra if Ra else 0
    x = 0

    while x <= xRange:
        y = int(round(sqrtCoef * sqrt(sqrA - x * x)))

        if drawFlag:
            draw.drawEllipsePoints(x, y, Xc, Yc, scene, pen)

        x += 1

    y = 0
    yRange = (int(round(sqrB / sqrt(sqrA + sqrB)))
              if sqrA or sqrB else 0)
    sqrtCoef = Ra / Rb if Rb else 0

    while y <= yRange:
        x = int(round(sqrtCoef * sqrt(sqrB - y * y)))

        if drawFlag:
            draw.drawEllipsePoints(x, y, Xc, Yc, scene, pen)

        y += 1


def parametric(Xc, Yc, Ra, Rb, scene, pen, drawFlag=True):
    """
        Отрисовка эллипса по
        параметрическому уравнению
    """
    tRange = pi / 2
    tStep = 1 / max(Ra, Rb) if Ra or Rb else 1
    t = 0

    while t < tRange + tStep:
        x = int(round(Ra * cos(t)))
        y = int(round(Rb * sin(t)))

        if drawFlag:
            draw.drawEllipsePoints(x, y, Xc, Yc, scene, pen)

        t += tStep


def brezenham(Xc, Yc, Ra, Rb, scene, pen, drawFlag=True):
    """
        Отрисовка эллипса
        алгоритмом Брезенхема
    """
    sqrA = Ra * Ra
    sqrB = Rb * Rb

    x = 0
    y = Rb
    capDelta = sqrB - sqrA * (2 * Rb - 1)

    while y >= 0:
        if drawFlag:
            draw.drawEllipsePoints(x, y, Xc, Yc, scene, pen)

        if capDelta < 0:
            delta = 2 * capDelta + sqrA * (2 * y - 1)

            if delta <= 0:
                x += 1
                capDelta = capDelta + sqrB * (2 * x + 1)
            else:
                x += 1
                y -= 1
                capDelta = capDelta + 2 * x * sqrB - 2 * y * sqrA + sqrA + sqrB

        elif capDelta > 0:
            delta = 2 * capDelta - sqrB * (2 * x + 1)

            if delta <= 0:
                x += 1
                y -= 1
                capDelta = capDelta + 2 * x * sqrB - 2 * y * sqrA + sqrA + sqrB
            else:
                y -= 1
                capDelta = capDelta + sqrA * (- 2 * y + 1)

        else:
            x += 1
            y -= 1
            capDelta = capDelta + 2 * x * sqrB - 2 * y * sqrA + sqrA + sqrB


    if not Rb and drawFlag:
        for x in range(Xc - Ra, Xc + Ra + 1):
            draw.drawPoint(x, Yc, scene, pen)


def midpoint(Xc, Yc, Ra, Rb, scene, pen, drawFlag=True):
    """
        Отрисовка эллипса
        алгоритмом средней точки
    """
    sqrA = Ra * Ra
    sqrB = Rb * Rb

    x = 0
    y = Rb
    trialFunc = sqrB - sqrA * (Rb - 1 / 4) if Rb else 0
    xRange = (int(round(sqrA / sqrt(sqrA + sqrB)))
              if sqrA or sqrB else 0)

    while x <= xRange:
        if drawFlag:
            draw.drawEllipsePoints(x, y, Xc, Yc, scene, pen)

        x += 1

        if trialFunc > 0:
            y -= 1
            trialFunc -= 2 * y * sqrA

        trialFunc = trialFunc + sqrB * (2 * x + 1)

    x = Ra
    y = 0
    trialFunc = sqrA - sqrB * (Ra - 1 / 4) if Ra else 0
    yRange = (int(round(sqrB / sqrt(sqrA + sqrB)))
              if sqrA or sqrB else 0)

    while y <= yRange:
        if drawFlag:
            draw.drawEllipsePoints(x, y, Xc, Yc, scene, pen)

        y += 1

        if trialFunc > 0:
            x -= 1
            trialFunc -= 2 * x * sqrB

        trialFunc = trialFunc + sqrA * (2 * y + 1)


def libfunc(Xc, Yc, Ra, Rb, scene, pen):
    """
        Отрисовка окружности
        библиотечной функции
    """
    scene.addEllipse(Xc - Ra, Yc - Rb, 2 * Ra, 2 * Rb, pen)