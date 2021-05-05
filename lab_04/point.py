"""
    Модуль отрисовки точки
"""

def drawPoint(x, y, scene):
    """
        Отрисока точки
    """
    scene.addLine(x, y, x, y)