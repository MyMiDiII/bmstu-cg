from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5.QtCore import QCoreApplication, QEventLoop

from math import isclose

from geometry import Point, Segment, Vector
from errors import callInfo, callError

EPS = 1e-6

class Cutter:

    def __init__(self, scene, painter, img, color):
        self.scene = scene
        self.painter = painter
        self.img = img
        self.color = color

    def getNormal(self, selector, index):
        edgeVec = Vector(
            selector[index],
            selector[(index + 1) % len(selector)]
        )

        normal = Vector(1, 0) if not edgeVec.x else Vector(-edgeVec.y / edgeVec.x, 1)

        if Vector(
            selector[(index + 1) % len(selector)],
            selector[(index + 2) % len(selector)]
        ).scalarProd(normal) < 0:
            normal.neg()

        return normal

    def cutSegment(self, seg, selector):
        tIn = 0
        tOut = 1
        vecDir = Vector(seg.begin, seg.end)
        vertNum = len(selector)

        for i in range(vertNum):
            weight = Vector(selector[i], seg.begin)

            normal = self.getNormal(selector, i)

            Dsc = vecDir.scalarProd(normal)
            Wsc = weight.scalarProd(normal)

            if isclose(Dsc, 0, abs_tol=EPS):
                if Wsc < 0 and not isclose(Wsc, 0, abs_tol=EPS):
                    return
                else:
                    continue

            t = - Wsc / Dsc
            if Dsc > 0:
                if t > tIn:
                    tIn = t
            else:
                if t < tOut:
                    tOut = t

        if tIn < tOut:
            p1 = Point(
                round(seg.begin.x + vecDir.x * tIn),
                round(seg.begin.y + vecDir.y * tIn)
            )
            p2 = Point(
                round(seg.begin.x + vecDir.x * tOut),
                round(seg.begin.y + vecDir.y * tOut)
            )
            self.painter.drawLine(
                p1.x,
                p1.y,
                p2.x,
                p2.y
            )


    def run(self, segments, selector):
        if not selector.isConvex():
            callError(
                "Невыпуклый отсекатель!",
                "Отсекатель не является выпуклым!"
            )
            return

        for seg in segments:
            self.cutSegment(seg, selector)
