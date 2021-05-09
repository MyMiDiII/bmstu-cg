"""
    Модуль отрисовки
"""

xSigns = [1, -1, -1, 1]
ySigns = [1, 1, -1, -1]

def drawPoint(x, y, scene, pen):
    """
        Отрисовка точки
    """
    scene.addLine(x, y, x, y, pen)


def drawCirclePoints(x, y, xc, yc, scene, pen):
    """
        Отрисовка симметричных точек окружности
    """
    for i in range(4):
        drawPoint(
            xc + xSigns[i] * x,
            yc + ySigns[i] * y,
            scene,
            pen
        )

        drawPoint(
            xc + ySigns[i] * y,
            yc + xSigns[i] * x,
            scene,
            pen
        )


def drawEllipsePoints(x, y, xc, yc, scene, pen):
    """
        Отрисовка симметричных точек эллипса
    """
    for i in range(4):
        drawPoint(
            xc + xSigns[i] * x,
            yc + ySigns[i] * y,
            scene,
            pen
        )
