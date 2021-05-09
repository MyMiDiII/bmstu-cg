"""
    Модуль ввода с помощью мыши
"""

from PyQt5.QtWidgets import QGraphicsScene

from geometry import Point
from PyQt5.QtGui import QPainter, QPixmap

class Canvas(QGraphicsScene):
    """Класс холста"""

    def __init__(self, window, img, polygons, polygon, lineMode=False, *args, **kwargs):
        """Конструктор"""
        super(Canvas, self).__init__(*args, **kwargs)
        self.window = window
        self.img = img
        self.polygons = polygons
        self.polygon = polygon
        self.lineMode = lineMode

    def mousePressEvent(self, event):
        point = Point(
            int(event.scenePos().x()),
            int(event.scenePos().y())
        )

        painter = QPainter(self.img)

        if self.polygon.num == 0:
            painter.drawPoint(point.x, point.y)
        else:
            last = self.polygon.getLastPoint()
            painter.drawLine(last.x, last.y, point.x, point.y)

        self.clear()
        self.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

        self.polygon.addPoint(point)

        self.window.addPoint(point)
        if self.polygon.num > 2:
            self.window.closeFigBtn.setDisabled(False)
