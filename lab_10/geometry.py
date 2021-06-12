"""
    Модуль геометрических объектов
"""
from math import isclose
from itertools import combinations

EPS = 1e-6

from PyQt5.QtGui import QPainter

class Point:
    """
        Класс точки в трехмерном пространстве
    """

    def __init__(self, x=0, y=0, z=0):
        """Конструктор"""
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        """ Оператор == """
        return self.x == other.x and self.y == other.y and self.z == self.z

    def __ne__(self, other):
        """ Оператор != """
        return not self == other

    def transform(self, matrix):
        pointVector = [self.x, self.y, self.z, 1]
        resPointVector = [0, 0, 0, 0]

        for i in range(4):
            for j in range(4):
                resPointVector[i] += pointVector[j] * matrix[j][i]

        self.x = resPointVector[0]
        self.y = resPointVector[1]
        self.z = resPointVector[2]


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

    def __init__(self, *args):
        """ Конструктор """
        if isinstance(args[0], (int, float)):
            self.x = args[0]
            self.y = args[1]
        else:
            self.x = args[1].x - args[0].x
            self.y = args[1].y - args[0].y

    def isZero(self):
        return (isclose(self.x, 0, abs_tol=EPS)
                and isclose(self.y, 0, abs_tol=EPS))

    def neg(self):
        self.x = -self.x
        self.y = -self.y

    def vecProd(self, vector):
        return self.x * vector.y - self.y * vector.x

    def scalarProd(self, vector):
        return self.x * vector.x + self.y * vector.y


class Polygon:
    """
        Класс многоугольной области
    """

    def __init__(self, points=[], isClosed=False):
        """Конструктор"""
        self.points = points
        self.num = len(points)
        self.isClosed = isClosed

    def __len__(self):
        return self.num

    def __getitem__(self, key):
        return self.points[key]

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

    def isPoint(self):
        if not self.num:
            return False

        prev = self[0]
        for pnt in self:
            if prev != pnt:
                return False

        return True

    def isAdjacent(self, edge1, edge2):
        return (edge1[0] == edge2[0]
                or edge1[0] == edge2[1]
                or edge1[1] == edge2[0]
                or edge1[1] == edge2[1])

    def onSeg(self, point, edge):
        vecEdge = Vector(edge[0], edge[1])
        toPVec = Vector(edge[0], point)
        pToF = Vector(point, edge[0])
        pToS = Vector(point, edge[1])

        if isclose(vecEdge.vecProd(toPVec), 0, abs_tol=EPS):
            scPr = pToF.scalarProd(pToS)
            if scPr < 0 or isclose(scPr, 0, abs_tol=EPS):
                return True

        return False

    def isInters(self, edge1, edge2):
        edgeVec = Vector(edge1[0], edge1[1])
        edgeToF = Vector(edge1[0], edge2[0])
        edgeToS = Vector(edge1[0], edge2[1])

        prod1 = edgeVec.vecProd(edgeToF)
        prod2 = edgeVec.vecProd(edgeToS)

        res = prod1 * prod2

        if res < 0 and not isclose(res, 0, abs_tol=EPS):
            return True

        if res > 0 and not isclose(res, 0, abs_tol=EPS):
            return False

        if self.onSeg(edge1[0], edge2):
            return True

        if self.onSeg(edge1[1], edge2):
            return True

        if self.onSeg(edge2[0], edge1):
            return True

        if self.onSeg(edge2[1], edge1):
            return True

        return False


    def noInters(self):
        edges = []

        for i in range(len(self)):
            edges.append([self[i - 1], self[i]])

        combs = list(combinations(edges, 2))

        for i in range(len(combs)):
            edge1 = combs[i][0]
            edge2 = combs[i][1]

            if self.isAdjacent(edge1, edge2):
                continue

            if self.isInters(edge1, edge2):
                return False

        return True

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
    
        return self.noInters()

    def clear(self):
        self.points = []
        self.num = 0
        self.isClosed = False

    def draw(self, painter : QPainter):
        for i in range(len(self)):
            painter.drawLine(self[i].x, self[i].y,
                             self[i - 1].x, self[i - 1].y)

class Range:

    def __init__(self, begin, end, step):
        self.begin = begin
        self.end = end
        self.step = step
