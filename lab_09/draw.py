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
                 polygon, lineMode=False,
                 *args, **kwargs):
        """Конструктор"""
        super(Canvas, self).__init__(*args, **kwargs)
        self.window = window
        self.img = img
        self.polygon = polygon
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

        if self.mode == SELECTOR:
            print("here1")
            painter.setPen(self.window.selColor)
        else:
            print("here2")
            painter.setPen(self.window.segColor)

        if event.button() == Qt.MiddleButton:
            if self.polygon.num < 3:
                return

            first = self.polygon.getFirstPoint()
            last = self.polygon.getLastPoint()

            painter.drawLine(last.x, last.y, first.x, first.y)
            painter.end()

            self.clear()
            self.addPixmap(QPixmap.fromImage(self.img))

            self.polygon.isClosed = True

            if self.mode == SELECTOR:
                self.window.setSelectorBtn.setDisabled(True)
                self.window.addRow(self.window.selectorTable, "end", "end")
                self.window.selector = copy.deepcopy(self.polygon)

            if self.mode == POLYGON:
                self.window.setPolygonBtn.setDisabled(True)
                self.window.addRow(self.window.polygonsTable, "end", "end")
                self.window.polygon.clear()
                self.window.polygons.append(copy.deepcopy(self.polygon))

            self.mode = NONE
            self.polygon.clear()

            return

        point = Point(
            int(event.scenePos().x()),
            int(event.scenePos().y())
        )

        if event.button() == Qt.RightButton:
            if len(self.polygon) and self.mode == POLYGON:
                return

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
            if len(self.polygon) and self.mode == SELECTOR:
                return

            self.mode = POLYGON
            painter.setPen(self.window.segColor)

        print("I'm drawing")
        if self.polygon.num == 0:
            painter.drawPoint(point.x, point.y)
        else:
            last = self.polygon.getLastPoint()

            if self.lineMode:
                point = self.getHorOrVerLine(last, point)

            painter.drawLine(last.x, last.y, point.x, point.y)

        self.clear()
        self.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

        self.polygon.addPoint(point)

        if event.button() == Qt.RightButton:
            self.window.selector = copy.deepcopy(self.polygon)
            self.window.addPoint(self.window.selectorTable, point)

            if self.polygon.num > 2:
                self.window.setSelectorBtn.setDisabled(False)

        if event.button() == Qt.LeftButton:
            self.window.polygon = copy.deepcopy(self.polygon)
            self.window.addPoint(self.window.polygonsTable, point)

            if self.polygon.num > 2:
                self.window.setPolygonBtn.setDisabled(False)

    def mouseMoveEvent(self, event):
        if (not self.prevPoint 
            and (not self.polygon.num
            or self.polygon.isClosed)):
            return

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

            last = self.polygon.getLastPoint()

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
