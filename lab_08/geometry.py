"""
    Модуль геометрических объектов
"""

class Point:
    """
        Класс точки в двумерном пространстве
    """

    def __init__(self, x=0, y=0):
        """Конструктор"""
        self.x = x
        self.y = y

    def __eq__(self, other):
        """ Оператор == """
        return self.x == other.x and self.y == other.y


class Edge:
    """
        Класс ребра
    """

    def __init__(self, point1=Point(), point2=Point()):
        """Конструктор"""
        self.begin = point1
        self.end = point2


class Polygon:
    """
        Класс многоугольной области
    """

    def __init__(self, points=[], isClosed=False):
        """Конструктор"""
        self.points = points
        self.num = len(points)
        self.isClosed = isClosed

    def addPoint(self, point):
        self.points.append(point)
        self.num += 1

    def deletePoint(self):
        self.points.pop()
        self.num -= 1

    def getLastPoint(self):
        return self.points[self.num - 1] if self.num else None

    def getFirstPoint(self):
        return self.points[0] if self.num else None

    def clear(self):
        self.points = []
        self.num = 0
        self.isClosed = False