"""
    Модуль отрисоки 3D-функций
    алгоритмом плавающего горизонта
"""

from math import cos, isclose, sin
from PyQt5.QtGui import QColor, QImage, QPainter
from PyQt5.sip import setdeleted
from geometry import Point, Range

EPS = 1e-6

def sign(num):
    if isclose(num, 0, abs_tol=EPS):
        return 0

    if num > 0:
        return 1
    
    return -1

class Func3DDrawer:

    def __init__(self, painter : QPainter, color : QColor,
                 width, heigth, matrix, xRange : Range, zRange : Range, 
                 func):
        self.painter = painter
        self.color = color
        self.width = width
        self.height = heigth
        self.matrix = matrix
        self.xRange = xRange
        self.zRange = zRange
        self.func = func

    def drawPointByHorizon(self, x, y, up, low):
        if not (0 <= x <= self.width and 0 <= y <= self.height):
            return False

        if y > up[x]:
            up[x] = y
            self.painter.drawPoint(x, y)
        
        if y < low[x]:
            low[x] = y
            self.painter.drawPoint(x, y)

        return True


    def drawLineByHorizon(self, begin, end, up, low):
        if begin == end:
            self.drawPointByHorizon(int(round(begin.x)), int(round(begin.y)), up, low)
            return

        if end.y < begin.y:
            begin, end = end, begin

        dx = end.x - begin.x
        dy = end.y - begin.y
        coef = abs(dx) if abs(dx) > abs(dy) else abs(dy)

        if isclose(coef, 0, abs_tol=EPS):
            return

        dx /= coef
        dy /= coef

        x, y = begin.x, begin.y
        isDraw = True
        _ = 0
        
        while isDraw and _ <= coef:
            isDraw = self.drawPointByHorizon(int(round(x)), int(round(y)), up, low)
            x += dx
            y += dy
            _ += 1

    def run(self):
        upHorizon = [0 for x in range(self.width + 1)]
        lowHorizon = [self.height for x in range(self.width + 1)]

        left = Point(-1, -1)
        right = Point(-1, -1)

        z = self.zRange.end

        while z > self.zRange.begin - self.zRange.step / 2:
            prevPoint = None            

            curPoint = Point(
                self.xRange.begin,
                self.func(self.xRange.begin, z),
                z
            )
            curPoint.transform(self.matrix)

            if left.x != -1:
                self.drawLineByHorizon(
                    curPoint,
                    left,
                    upHorizon,
                    lowHorizon
                )

            left = curPoint

            x = self.xRange.begin

            while x < self.xRange.end + self.xRange.step / 2:
                y = self.func(x, z)

                curPoint = Point(x, y, z)
                curPoint.transform(self.matrix)

                if prevPoint:
                    self.drawLineByHorizon(prevPoint, curPoint, upHorizon, lowHorizon)

                prevPoint = curPoint

                x += self.xRange.step

            if right.x != -1:
                self.drawLineByHorizon(prevPoint, right, upHorizon, lowHorizon)

            right = prevPoint

            z -= self.zRange.step
