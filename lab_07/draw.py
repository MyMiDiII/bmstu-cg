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
        self.firstCorner = None

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

        if event.button() == Qt.RightButton:
            if self.prevPoint:
                return

            painter = QPainter(self.img)

            if not self.firstCorner:
                self.firstCorner = point
                prevSelecter = self.window.selecter

                xLeft = prevSelecter[0]
                xRight = prevSelecter[1]
                yLow = prevSelecter[2]
                yTop = prevSelecter[3]

                # TODO очистка таблицы

                painter.setPen(QColor("white"))

                painter.drawLine(xLeft, yLow, xRight, yLow)
                painter.drawLine(xRight, yLow, xRight, yTop)
                painter.drawLine(xRight, yTop, xLeft, yTop)
                painter.drawLine(xLeft, yTop, xLeft, yLow)

                self.clear()
                self.addPixmap(QPixmap.fromImage(self.img))
            
            else:
                xLeft = self.firstCorner.x
                xRight = point.x
                yLow = self.firstCorner.y
                yTop = point.y

                if xLeft > xRight:
                    xLeft, xRight = xRight, xLeft

                if yLow > yTop:
                    yLow, yTop = yTop, yLow

                self.window.selecter = [xLeft, xRight, yLow, yTop]

                self.window.setSelecterRow(
                    str(xLeft),
                    str(xRight),
                    str(yLow),
                    str(yTop)
                )

                painter.setPen(QColor(self.window.selColor))

                painter.drawLine(xLeft, yLow, xRight, yLow)
                painter.drawLine(xRight, yLow, xRight, yTop)
                painter.drawLine(xRight, yTop, xLeft, yTop)
                painter.drawLine(xLeft, yTop, xLeft, yLow)

                self.firstCorner = None


            painter.end()

            self.clear()
            self.addPixmap(QPixmap.fromImage(self.img))

            return

        if self.firstCorner:
            return

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
            self.window.segments.append(seg)
            self.window.addSegment(seg)
            self.prevPoint = None

        self.clear()
        self.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

    def mouseMoveEvent(self, event):
        if not self.prevPoint and not self.firstCorner:
            return

        point = Point(
            event.scenePos().x(),
            event.scenePos().y()
        )

        tmpImg = QImage(self.img)

        painter = QPainter(tmpImg)

        if self.firstCorner:
            painter.setPen(QColor(self.window.selColor))

            painter.drawLine(
                self.firstCorner.x,
                self.firstCorner.y,
                point.x,
                self.firstCorner.y,
            )

            painter.drawLine(
                point.x,
                self.firstCorner.y,
                point.x,
                point.y
            )

            painter.drawLine(
                point.x,
                point.y,
                self.firstCorner.x,
                point.y
            )

            painter.drawLine(
                self.firstCorner.x,
                point.y,
                self.firstCorner.x,
                self.firstCorner.y
            )

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
