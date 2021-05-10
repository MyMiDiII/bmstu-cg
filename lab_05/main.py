import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView, QGraphicsScene
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtGui import (
    QPen, QColor, QPainter, QPixmap, QImage
)
from PyQt5.QtCore import QSize

import copy

from MainWindow import Ui_MainWindow

from draw import Canvas
from geometry import Point, Edge, Polygon
from fill import Filler

BACKGROUNDSTRING = ("background-color: qlineargradient(spread:pad, "
                   + "x1:0, y1:0, x2:0, y2:0, stop:0 %s"
                   + ", stop:1 rgba(255, 255, 255, 255));")


# TODO
#// холст

def callError(title, text):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.exec_()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """
        Класс главного окна
    """

    def __init__(self, *args, **kwargs):
        """
            Инициализация главного окна
        """
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.graphicsView.setMouseTracking(True)

        self.polygons = []
        self.polygon = Polygon()
        self.color = QColor("black")
        
        self.colorBtn.clicked.connect(self.chooseColor)

        self.img = QImage(1185, 874, QImage.Format_RGB32)
        self.img.fill(QColor("white"))
        self.scene = Canvas(self, self.img, self.polygon)
        self.scene.setSceneRect(0, 0, 1185, 874)
        self.graphicsView.setScene(self.scene)
        self.scene.addPixmap(QPixmap.fromImage(self.img))

        self.addPointBtn.clicked.connect(self.handleAddPoint)
        self.closeFigBtn.setDisabled(True)
        self.closeFigBtn.clicked.connect(self.closeFig)

        self.paintBtn.clicked.connect(self.fill)
        self.clearBtn.clicked.connect(self.clear)

    def fill(self):
        filler = Filler(
            self.scene,
            self.img,
            self.color,
            self.polygons
        )

        delay = self.delaySB.value()

        filler.run(delay)
    
    def closeFig(self):
        if self.polygon.num < 3:
            self.closeFigBtn.setDisabled(False)
            return

        self.addRow("end", "end")

        painter = QPainter(self.img)

        first = self.polygon.getFirstPoint()
        last = self.polygon.getLastPoint()

        painter.drawLine(last.x, last.y, first.x, first.y)

        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))

        painter.end()

        self.polygons.append(copy.deepcopy(self.polygon))
        self.polygon.clear()

        self.closeFigBtn.setDisabled(True)

    def clear(self):
        self.scene.clear()
        self.img.fill(QColor("white"))
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        self.pointsTable.setRowCount(0)
        self.polygons = []
        self.polygon.clear()

    def addRow(self, xStr, yStr):
        num = self.pointsTable.rowCount()
        self.pointsTable.setRowCount(num + 1)
        self.pointsTable.setItem(
            num,
            0,
            QTableWidgetItem(xStr)
        )
        self.pointsTable.setItem(
            num,
            1,
            QTableWidgetItem(yStr)
        )

    def addPoint(self, point):
        self.addRow(str(point.x), str(point.y))

    def handleAddPoint(self):
        """
            Добавление вершины
        """
        point = Point(self.xSB.value(), self.ySB.value())

        self.addPoint(point)

        painter = QPainter(self.img)

        if self.polygon.num == 0:
            painter.drawPoint(point.x, point.y)
        else:
            last = self.polygon.getLastPoint()
            painter.drawLine(last.x, last.y, point.x, point.y)

        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

        self.polygon.addPoint(point)
        if self.polygon.num > 2:
            self.closeFigBtn.setDisabled(False)

    def chooseColor(self):
        """
            Выбор цвета
        """
        self.color = QColorDialog.getColor()
        self.colorBtn.setStyleSheet(BACKGROUNDSTRING % self.color.name())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.move(250, 100)
    main.setFixedSize(1500, 900)
    main.show()
    sys.exit(app.exec_())
