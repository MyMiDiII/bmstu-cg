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


class Segment:
    """
        Класс отрезка
    """

    def __init__(self, point1=Point(), point2=Point()):
        """Конструктор"""
        self.begin = point1
        self.end = point2
