"""
    Модуль отрисоки 3D-функций
    алгоритмом плавающего горизонта
"""

from math import isclose
from PyQt5.QtGui import QColor, QImage, QPainter
from geometry import Range

EPS = 1e-6

def sign(num):
    if isclose(num, 0, abs_tol=EPS):
        return 0

    if num > 0:
        return 1
    
    return -1

class Func3DDrawer:

    def __init__(self, painter : QPainter, color : QColor,
                 width, height, xRange : Range, zRange : Range, 
                 func):
        self.painter = painter
        self.color = color
        self.width = width
        self.height = height
        self.xRange = xRange
        self.zRange = zRange
        self.func = func

    def isVisible(self, x, y, up, low):
        if y > up[x] or isclose(y, up[x], abs_tol=EPS):
            return 1

        if y < low[x] or isclose(y, low[x], abs_tol=EPS):
            return -1

        return 0

    def horizon(self, x1, y1, x2, y2, up, low):
        if isclose(x2 - x1, 0, abs_tol=EPS):
            up[x2] = max(up[x2], y2)
            low[x2] = min(low[x2], y2)
        else:
            coef = (y2 - y1) / (x2 - x1)
            
            x = x1
            while x < x2 + 1.5:
                y = coef * (x - x1) + y1
                up[x] = max(up[x], y)
                low[x] = min(low[x], y)
                x += 1

    def edgeHorizon(self, x, y, edgeX, edgeY, up, low):
        if edgeX != 1:
            self.horizon(edgeX, edgeY, x, y, up, low)

        edgeX = x
        edgeY = y
        
        return edgeX, edgeY

    def intersection(x1, y1, x2, y2, horizon):
        if isclose(x2 - x1, 0, abs_tol=EPS):
            return x2, horizon[x2]

        else:
            coef = (y2 - y1) / (x2 - x1)
            ySign = sign(y1 + coef - horizon[x1 + 1])
            curSign = ySign

            yRes = y1 + coef
            xRes = x1 + 1
            
            while ySign == curSign:
                yRes = y1 + coef
                xRes = x1 + 1
                curSign = sign(yRes - horizon[xRes])

            if abs(yRes - coef - horizon[xRes - 1]) <= abs(yRes - horizon[xRes]):
                yRes -= coef
                xRes -= 1

            return xRes, yRes

    def run(self):
        xLeft, yLeft, xRight, yRight = -1, -1, -1, -1

        upHorizon = [0 for x in range(self.width + 1)]
        lowHorizon = [self.height for x in range(self.width + 1)]

        z = self.zRange.end

        while z > self.zRange.begin - self.zRange.step / 2:
            xPrev = self.xRange.begin
            yPrev = self.func(xPrev, z) 

            xLeft, yLeft = self.edgeHorizon(xPrev, yPrev, xLeft, yLeft, upHorizon, lowHorizon)
            prevVis = self.isVisible(xPrev, yPrev, upHorizon, lowHorizon)

            x = self.xRange.begin

            while x < self.xRange.end + self.xRange.step / 2:
                y = self.func(x, z)

                curVis = self.isVisible(x, y, upHorizon, lowHorizon)

                if prevVis == curVis:
                    if curVis != 0:
                        self.painter.drawLine(xPrev, yPrev, x, y)
                        self.horizon(xPrev, yPrev, x, y, up, low)

                else if 



