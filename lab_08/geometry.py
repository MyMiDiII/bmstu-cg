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

class Vector:
    """
        Класс свободного вектора
    """

    def __init__(self, begin=Point(), end=Point):
        """ Конструктор """
        self.x = end.x - begin.x
        self.y = end.y - begin.y

    def vecProd(self, vector):
        return self.x * vector.y - self.y * vector.x


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

    def isConvex(self):
        if self.num < 3:  
            return False  

        vec1 = Vector(self.points[1], self.points[2])
        vec2 = Vector(self.points[0], self.points[1])

        sign = 1 if vec1.vecProd(vec2) > 0 else -1  

        for i in range(self.num):  
            vec1 = Vector(self.points[i - 1], self.points[i])
            vec2 = Vector(self.points[i - 2], self.points[i - 1])

            if sign * vec1.vecProd(vec2) < 0:  
                return False  
    
        if sign < 0:  
            self.points.reverse()  
    
        return True 

    def clear(self):
        self.points = []
        self.num = 0
        self.isClosed = False