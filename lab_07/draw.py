"""
    Модуль ввода с помощью мыши
"""

from PyQt5.QtWidgets import QGraphicsScene

from geometry import Point, Segment
from PyQt5.QtGui import QPainter, QPixmap, QImage, QColor
from PyQt5.QtCore import Qt

import copy


class Canvas(QGraphicsScene):
    """Класс холста"""

    def __init__(self, window, img,
                 lineMode=False,
                 *args, **kwargs):
        """Конструктор"""
        super(Canvas, self).__init__(*args, **kwargs)
        self.window = window
        self.img = img
        self.lineMode = lineMode
        self.prevPoint = None

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
        point = Point(
            int(event.scenePos().x()),
            int(event.scenePos().y())
        )

        """
        TODO обработка отсекателя
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
            self.window.addRow("end", "end")

            return
        """
        painter = QPainter(self.img)
        painter.setPen(QColor(self.window.segColor))

        if not self.prevPoint:
            painter.drawPoint(point.x, point.y)
            self.prevPoint = point

        else:
            prev = self.prevPoint

            if self.lineMode:
                point = self.getHorOrVerLine(prev, point)

            painter.drawLine(prev.x, prev.y, point.x, point.y)

            seg = Segment(self.prevPoint, point)
            self.window.addSegment(seg)
            self.prevPoint = None

        self.clear()
        self.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

    def mouseMoveEvent(self, event):
        if not self.prevPoint:
            return

        tmpImg = QImage(self.img)

        painter = QPainter(tmpImg)
        painter.setPen(QColor(self.window.segColor))

        prev = self.prevPoint

        point = Point(
            event.scenePos().x(),
            event.scenePos().y()
        )

        if self.lineMode:
            point = self.getHorOrVerLine(prev, point)

        painter.drawLine(prev.x, prev.y, point.x, point.y)

        self.clear()
        self.addPixmap(QPixmap.fromImage(tmpImg))

        painter.end()
