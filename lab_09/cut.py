from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5.QtCore import QCoreApplication, QEventLoop

from math import isclose

from geometry import Point, Polygon, Segment, Vector
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
    
    def isVisible(self, point, edge):
        edgeVect = Vector(edge.begin, edge.end)
        toPointVect = Vector(edge.begin, point)
        prod = edgeVect.vecProd(toPointVect)
        return prod < 0 or isclose(prod, 0, abs_tol=EPS)

    def findIntersection(self, seg, edge, normal):
        segVect = Vector(seg.begin, seg.end)
        weight = Vector(edge.begin, seg.begin)

        Dsc = segVect.scalarProd(normal)
        Wsc = weight.scalarProd(normal)

        t = -Wsc / Dsc

        return Point(seg.begin.x + segVect.x * t, seg.begin.y + segVect.y * t)

    def cutPolyByEdge(self, poly, edge, normal):
        result = Polygon([])
        if len(poly) < 3:
            return result

        prevPoint = poly[0]
        prevVis = self.isVisible(prevPoint, edge)

        for i in range(1, len(poly) + 1):
            curPoint = poly[i % len(poly)]

            curVis = self.isVisible(curPoint, edge)

            if prevVis:
                if curVis:
                    result.addPoint(curPoint)
                else:
                    seg = Segment(prevPoint, curPoint)
                    result.addPoint(self.findIntersection(
                        seg,
                        edge,
                        normal
                    ))

            else:
                if curVis:
                    seg = Segment(prevPoint, curPoint)
                    result.addPoint(self.findIntersection(
                        seg,
                        edge,
                        normal
                    ))
                    result.addPoint(curPoint)

            prevPoint = curPoint
            prevVis = curVis

        return result

    def selectorVisible(self, selector, polygon):
        for i in range(len(polygon)):
            edge = Segment(polygon[i - 1], polygon[i])

            if not self.isVisible(selector[0], edge):
                return Polygon([])

        return selector

    def cutPolygon(self, polygon, selector):
        if selector.isPoint():
            polygon.isConvex()
            return self.selectorVisible(selector, polygon)

        result = polygon

        for i in range(len(selector)):
            normal = self.getNormal(selector, i)
            edge = Segment(selector[i],
                        selector[(i + 1) % len(selector)])
            result = self.cutPolyByEdge(result, edge, normal)

            if len(result) < 3:
                return Polygon([])

        return result

    def run(self, polygons, selector):
        if not selector.isConvex():
            callError(
                "Невыпуклый отсекатель!",
                "Отсекатель не является выпуклым!"
            )
            return

        for poly in polygons:
            res = self.cutPolygon(poly, selector)
            res.draw(self.painter)
