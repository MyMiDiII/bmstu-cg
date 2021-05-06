"""
    Модуль отрисовки точки
"""

def drawPoint(x, y, scene, pen):
    """
        Отрисока точки
    """
    scene.addLine(x, y, x, y, pen)