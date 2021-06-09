"""
    Модуль ввода с помощью мыши
"""

from MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QGraphicsScene

from geometry import Point, Polygon, Segment
from PyQt5.QtGui import QPainter, QPixmap, QImage, QColor
from PyQt5.QtCore import Qt

import copy

NONE = 0
POLYGON = 1
SELECTOR = 2

class Canvas(QGraphicsScene):
    """Класс холста"""

    def __init__(self, window: Ui_MainWindow, img,
                 selector, polygon, lineMode=False,
                 *args, **kwargs):
        """Конструктор"""
        super(Canvas, self).__init__(*args, **kwargs)
        self.window = window
        self.img = img
        self.polygon = polygon
        self.selector = selector
        self.lineMode = lineMode
        self.prevPoint = None
        self.mode = NONE

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Shift:
            self.lineMode = True

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Shift:
            self.lineMode = False

    def getHorOrVerLine(self, last, point):
        dx = abs(point.x - last.x)
        dy = abs(point.y - last.y)

        if dy > dx:
            point.x = last.x
        else:
            point.y = last.y

        return point

    def mousePressEvent(self, event):
        painter = QPainter(self.img)
        curPoly = None

        if self.mode == SELECTOR:
            painter.setPen(self.window.selColor)
            curPoly = self.selector
        else:
            painter.setPen(self.window.segColor)
            curPoly = self.polygon

        if event.button() == Qt.MiddleButton:
            if curPoly.num < 3:
                return

            first = curPoly.getFirstPoint()
            last = curPoly.getLastPoint()

            painter.drawLine(last.x, last.y, first.x, first.y)
            painter.end()

            self.clear()
            self.addPixmap(QPixmap.fromImage(self.img))

            curPoly.isClosed = True

            if self.mode == SELECTOR:
                self.window.setSelectorBtn.setDisabled(True)
                self.window.addRow(self.window.selectorTable, "end", "end")

            if self.mode == POLYGON:
                self.window.setPolygonBtn.setDisabled(True)
                self.window.addRow(self.window.polygonsTable, "end", "end")
                self.window.polygons.append(copy.deepcopy(self.polygon))
                self.window.polygon.clear()
                self.polygon.clear()

            self.mode = NONE

            return

        point = Point(
            int(event.scenePos().x()),
            int(event.scenePos().y())
        )

        if event.button() == Qt.RightButton:
            if len(self.polygon) and self.mode == POLYGON:
                return

            curPoly = self.selector
            self.mode = SELECTOR

            if self.window.selector.isClosed:
                painter.setPen(QColor("white"))

                for i, pnt in enumerate(self.window.selector):
                    painter.drawLine(
                        pnt.x,
                        pnt.y,
                        self.window.selector[i - 1].x,
                        self.window.selector[i - 1].y,
                    )

                self.window.selectorTable.setRowCount(0)
                self.window.selector.clear()

            painter.setPen(self.window.selColor)

        if event.button() == Qt.LeftButton:
            if len(self.selector) and self.mode == SELECTOR:
                return

            self.mode = POLYGON
            curPoly = self.polygon
            painter.setPen(self.window.segColor)

        if curPoly.num == 0:
            painter.drawPoint(point.x, point.y)
        else:
            last = curPoly.getLastPoint()

            if self.lineMode:
                point = self.getHorOrVerLine(last, point)

            painter.drawLine(last.x, last.y, point.x, point.y)

        self.clear()
        self.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

        curPoly.addPoint(point)

        if event.button() == Qt.RightButton:
            self.window.addPoint(self.window.selectorTable, point)

            if curPoly.num > 2:
                self.window.setSelectorBtn.setDisabled(False)

        if event.button() == Qt.LeftButton:
            self.window.addPoint(self.window.polygonsTable, point)

            if curPoly.num > 2:
                self.window.setPolygonBtn.setDisabled(False)

    def mouseMoveEvent(self, event):
        if (not self.prevPoint 
            and (not self.polygon.num
            or self.polygon.isClosed)
            and (not self.selector.num
            or self.selector.isClosed)):
            return

        curPoly = self.selector if self.mode == SELECTOR else self.polygon

        tmpImg = QImage(self.img)

        point = Point(
            event.scenePos().x(),
            event.scenePos().y()
        )

        painter = QPainter(tmpImg)

        if not self.prevPoint:
            color = (self.window.selColor
                     if self.mode == SELECTOR
                     else self.window.segColor)
            painter.setPen(color)

            last = curPoly.getLastPoint()

            if self.lineMode:
                point = self.getHorOrVerLine(last, point)

            painter.drawLine(last.x, last.y, point.x, point.y)

            self.clear()
            self.addPixmap(QPixmap.fromImage(tmpImg))

            painter.end()

            return

        painter.setPen(QColor(self.window.segColor))

        prev = self.prevPoint

        if self.lineMode:
            point = self.getHorOrVerLine(prev, point)

        painter.drawLine(prev.x, prev.y, point.x, point.y)

        self.clear()
        self.addPixmap(QPixmap.fromImage(tmpImg))

        painter.end()
