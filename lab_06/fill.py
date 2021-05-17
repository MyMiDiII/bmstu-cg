"""
    Модуль заполнения сплошных областей
"""
from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QCoreApplication, QEventLoop


class Filler:

    def __init__(self, scene, img, color, polygons):
        self.scene = scene
        self.img = img
        self.color = color
        self.polygons = polygons
        self.maxY = 0
        self.minY = 1000

    def createYGroups(self):

        def getEdge(begin, end):
            if begin.y > end.y:
                begin, end = end, begin

            if end.y > self.maxY:
                self.maxY = end.y

            if begin.y < self.minY:
                self.minY = begin.y

            dy = end.y - begin.y
            dy = dy if dy else -1
            dx = (begin.x - end.x) / dy

            return end.y, [end.x, dx, dy]

        yGroups = {}

        for polygon in self.polygons:
            for i in range(polygon.num):
                y, edge = getEdge(polygon.points[i], polygon.points[i - 1])

                if edge[2] != -1:
                    if y not in yGroups:
                        yGroups[y] = [edge]
                    else:
                        yGroups[y].append(edge)

        return yGroups

    def addActiveEdges(self, activeEdges, yGroups, y):
        if y in yGroups:
            for edge in yGroups[y]:
                activeEdges.append(edge)

    def drawScanLine(self, activeEdges, y, delay):
        painter = QPainter(self.img)
        painter.setPen(self.color)

        for i in range(0, len(activeEdges), 2):
            x = int(round(activeEdges[i][0]))
            while x <= int(round(activeEdges[i + 1][0]) - 1 / 2):
                painter.drawPoint(x, y)
                x += 1

        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))

        sleepTime = QTime.currentTime().addMSecs(delay)
        while (QTime.currentTime() < sleepTime):
            QCoreApplication.processEvents(QEventLoop.AllEvents, delay)


    def updateActiveAdges(self, activeEdges):
        i = 0

        while i < len(activeEdges):
            activeEdges[i][0] += activeEdges[i][1]
            activeEdges[i][2] -= 1

            if activeEdges[i][2] < 0:
                activeEdges.pop(i)
            else:
                i += 1

        activeEdges.sort(key=lambda edge: edge[0])

    def run(self, delay=0):
        yGroups = self.createYGroups()

        activeEdges = []

        y = self.maxY

        for y in range(self.maxY, self.minY - 1, -1):
            self.updateActiveAdges(activeEdges)
            self.drawScanLine(activeEdges, y, delay)
            self.addActiveEdges(activeEdges, yGroups, y)
