"""
    Модуль ввода с помощью мыши
"""

from PyQt5.QtWidgets import QGraphicsScene

from geometry import Point
from PyQt5.QtGui import QPainter, QPixmap, QImage
from PyQt5.QtCore import Qt

import copy


class Canvas(QGraphicsScene):
    """Класс холста"""

    def __init__(self, window, img, polygon,
                 lineMode=False, seedMode=False,
                 *args, **kwargs):
        """Конструктор"""
        super(Canvas, self).__init__(*args, **kwargs)
        self.window = window
        self.img = img
        self.polygon = polygon
        self.lineMode = lineMode
        self.seedMode = seedMode

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Shift:
            self.lineMode = True

        if event.key() == Qt.Key_Control:
            self.seedMode = True

        if event.key() == Qt.Key_Escape:
            self.window.handleDeletePoint()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Shift:
            self.lineMode = False

        if event.key() == Qt.Key_Control:
            self.seedMode = False

    def getHorOrVerLine(self, last, point):
        dx = abs(point.x - last.x)
        dy = abs(point.y - last.y)

        if dy > dx:
            point.x = last.x
        else:
            point.y = last.y

        return point

    def mousePressEvent(self, event):
        point = Point(
            int(event.scenePos().x()),
            int(event.scenePos().y())
        )

        if self.seedMode:
            self.window.setSeed(point)

            return

        if event.button() == Qt.RightButton:
            if self.polygon.num < 3:
                return

            first = self.polygon.getFirstPoint()
            last = self.polygon.getLastPoint()

            painter = QPainter(self.img)
            painter.drawLine(last.x, last.y, first.x, first.y)
            painter.end()

            self.clear()
            self.addPixmap(QPixmap.fromImage(self.img))

            self.window.polygons.append(copy.deepcopy(self.polygon))
            self.polygon.clear()

            self.window.closeFigBtn.setDisabled(True)
            self.window.deletePointBtn.setDisabled(True)
            self.window.addRow("end", "end")

            return

        painter = QPainter(self.img)

        if self.polygon.num == 0:
            painter.drawPoint(point.x, point.y)
            self.window.deletePointBtn.setDisabled(False)
        else:
            last = self.polygon.getLastPoint()

            if self.lineMode:
                point = self.getHorOrVerLine(last, point)

            painter.drawLine(last.x, last.y, point.x, point.y)

        self.clear()
        self.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

        self.polygon.addPoint(point)

        self.window.addPoint(point)
        if self.polygon.num > 2:
            self.window.closeFigBtn.setDisabled(False)

    def mouseMoveEvent(self, event):
        if self.polygon.num == 0:
            return

        tmpImg = QImage(self.img)

        painter = QPainter(tmpImg)

        last = self.polygon.getLastPoint()

        point = Point(
            event.scenePos().x(),
            event.scenePos().y()
        )

        if self.lineMode:
            point = self.getHorOrVerLine(last, point)

        painter.drawLine(last.x, last.y, point.x, point.y)

        self.clear()
        self.addPixmap(QPixmap.fromImage(tmpImg))

        painter.end()
