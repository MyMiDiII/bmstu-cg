from math import sqrt, pi, cos, sin

import point

SQRT2 = sqrt(2)
xSigns = [1, -1, -1, 1]
ySigns = [1, 1, -1, -1]


def canon(Xc, Yc, Ra, Rb, scene, pen):
    """
        Отрисовка эллипса по
        каноническому уравнению
    if not Ra and not Rb:
        point.drawPoint(Xc, Yc, scene, pen)
        return
    """

    sqrA = Ra * Ra
    sqrB = Rb * Rb

    xRange = (round(sqrA / sqrt(sqrA + sqrB))
              if sqrA or sqrB else 0)
    sqrtCoef = Rb / Ra if Ra else 0
    x = 0

    while x <= xRange:
        y = int(round(sqrtCoef * sqrt(sqrA - x * x)))

        for i in range(4):
            point.drawPoint(
                Xc + xSigns[i] * x,
                Yc + ySigns[i] * y,
                scene,
                pen
            )

        x += 1

    y = 0
    yRange = (round(sqrB / sqrt(sqrA + sqrB))
              if sqrA or sqrB else 0)
    sqrtCoef = Ra / Rb if Rb else 0

    while y <= yRange:
        x = int(round(sqrtCoef * sqrt(sqrB - y * y)))

        for i in range(4):
            point.drawPoint(
                Xc + xSigns[i] * x,
                Yc + ySigns[i] * y,
                scene,
                pen
            )

        y += 1

    print("Ммм, канон!", Xc, Yc, Ra, Rb)


def parametric(Xc, Yc, Ra, Rb, scene, pen):
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

        for i in range(4):
            point.drawPoint(
                Xc + xSigns[i] * x,
                Yc + ySigns[i] * y,
                scene,
                pen
            )

        t += tStep

    print("Все связано", Xc, Yc, Ra, Rb)


def brezenham(Xc, Yc, Ra, Rb, scene, pen):
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
        for i in range(4):
            point.drawPoint(
                Xc + xSigns[i] * x,
                Yc + ySigns[i] * y,
                scene,
                pen
            )

        # TODO выделить функции
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


    if not Rb:
        for x in range(Xc - Ra, Xc + Ra + 1):
            point.drawPoint(x, Yc, scene, pen)

    print("От него не спрятаться", Xc, Yc, Ra, Rb)


def midpoint(Xc, Yc, Ra, Rb, scene, pen):
    """
        Отрисовка эллипса
        алгоритмом средней точки
    """
    sqrA = Ra * Ra
    sqrB = Rb * Rb

    x = 0
    y = Rb
    trialFunc = sqrB - sqrA * (Rb - 1 / 4) if Rb else 0
    xRange = (round(sqrA / sqrt(sqrA + sqrB))
              if sqrA or sqrB else 0)

    while x <= xRange:
        for i in range(4):
            point.drawPoint(
                Xc + xSigns[i] * x,
                Yc + ySigns[i] * y,
                scene,
                pen
            )

        x += 1

        if trialFunc > 0:
            y -= 1
            trialFunc -= 2 * y * sqrA

        trialFunc = trialFunc + sqrB * (2 * x + 1)

    x = Ra
    y = 0
    trialFunc = sqrA - sqrB * (Ra - 1 / 4) if Ra else 0
    yRange = (round(sqrB / sqrt(sqrA + sqrB))
              if sqrA or sqrB else 0)

    while y <= yRange:
        for i in range(4):
            point.drawPoint(
                Xc + xSigns[i] * x,
                Yc + ySigns[i] * y,
                scene,
                pen
            )

        y += 1

        if trialFunc > 0:
            x -= 1
            trialFunc -= 2 * x * sqrB

        trialFunc = trialFunc + sqrA * (2 * y + 1)

    print("Золотая середина", Xc, Yc, Ra, Rb)


def libfunc(Xc, Yc, Ra, Rb, scene, pen):
    """
        Отрисовка окружности
        библиотечной функции
    """
    scene.addEllipse(Xc - Ra, Yc - Rb, 2 * Ra, 2 * Rb, pen)
    print("Все ради этого", Xc, Yc, Ra, Rb)