"""
    Модуль ввода с помощью мыши
"""

from PyQt5.QtWidgets import QGraphicsScene

from geometry import Point
from PyQt5.QtGui import QPainter, QPixmap, QImage, QColor
from PyQt5.QtCore import Qt

import copy


class Canvas(QGraphicsScene):
    """Класс холста"""

    def __init__(self, window, img,
                 polygon, lineMode=False,
                 *args, **kwargs):
        """Конструктор"""
        super(Canvas, self).__init__(*args, **kwargs)
        self.window = window
        self.img = img
        self.polygon = polygon
        self.lineMode = lineMode

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

        if event.button() == Qt.MiddleButton:
            print("замыкаем")
            if self.polygon.num < 3:
                return

            first = self.polygon.getFirstPoint()
            last = self.polygon.getLastPoint()

            painter = QPainter(self.img)
            painter.setPen(QColor(self.window.selColor))
            painter.drawLine(last.x, last.y, first.x, first.y)
            painter.end()

            self.clear()
            self.addPixmap(QPixmap.fromImage(self.img))

            self.polygon.isClosed = True
            self.window.setSelectorBtn.setDisabled(True)
            self.window.selectorColorBtn.setDisabled(False)

            return

        if event.button() == Qt.RightButton:
            painter = QPainter(self.img)

            if self.polygon.isClosed:
                painter.setPen(QColor("white"))

                for i, pnt in enumerate(self.polygon.points):
                    painter.drawLine(
                        pnt.x,
                        pnt.y,
                        self.polygon.points[i - 1].x,
                        self.polygon.points[i - 1].y,
                    )

                self.window.selectorTable.setRowCount(0)
                self.polygon.clear()

            painter.setPen(QColor(self.window.selColor))

            if self.polygon.num == 0:
                self.window.selectorColorBtn.setDisabled(True)
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

            self.window.addPoint(point)
            print("количество вершин", self.polygon.num)
            if self.polygon.num > 2:
                self.window.setSelectorBtn.setDisabled(False)


    def mouseMoveEvent(self, event):
        if self.polygon.num == 0 or self.polygon.isClosed:
            return

        tmpImg = QImage(self.img)

        painter = QPainter(tmpImg)
        painter.setPen(QColor(self.window.selColor))

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
