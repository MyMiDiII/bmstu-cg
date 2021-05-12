import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView, QGraphicsScene
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtGui import (
    QPen, QColor, QPainter, QPixmap, QImage
)
from PyQt5.QtCore import QSize, QTime

import copy
import time

from PyQt5.sip import delete

from MainWindow import Ui_MainWindow

from draw import Canvas
from geometry import Point, Edge, Polygon
from fill import Filler

BACKGROUNDSTRING = ("background-color: qlineargradient(spread:pad, "
                   + "x1:0, y1:0, x2:0, y2:0, stop:0 %s"
                   + ", stop:1 rgba(255, 255, 255, 255));")


def callError(title, text):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.exec_()

def callInfo(title, text):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
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
        self.deletePointBtn.setDisabled(True)
        self.deletePointBtn.clicked.connect(self.handleDeletePoint)
        self.closeFigBtn.setDisabled(True)
        self.closeFigBtn.clicked.connect(self.closeFig)

        self.paintBtn.clicked.connect(self.fill)
        self.clearBtn.clicked.connect(self.clear)
        self.roolsBtn.clicked.connect(self.rools)

    def rools(self):
        title = "Правила ввода"
        text = ("<b>ЛКМ</b> – добавление вершины;<br>"
                + "<b>ПКМ</b> – замкнуть фигуру;<br>"
                + "<b>Shift</b> – горизонтальное/вертикальное ребро;<br>"
                + "<b>Esc</b> – удаление последней вершины.")

        callInfo(title, text)

    def setBtnsState(self, state):
        btns = [
            self.addPointBtn,
            self.paintBtn,
            self.clearBtn
        ]

        for btn in btns:
            btn.setDisabled(state)

    def fill(self):
        if self.polygon.points:
            callError("Незамкнутая облать!", "Область не замкнута!")
            return

        self.setBtnsState(True)

        filler = Filler(
            self.scene,
            self.img,
            self.color,
            self.polygons
        )

        delay = self.delaySB.value()

        dt = time.time()
        filler.run(delay)
        dt = time.time() - dt

        painter = QPainter(self.img)
        for pol in self.polygons:
            for i in range(pol.num):
                f = pol.points[i]
                s = pol.points[i - 1]
                painter.drawLine(f.x, f.y, s.x, s.y)

        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))

        self.timeLbl.setText("Время заполнения: {:.2f} c".format(dt))
        self.setBtnsState(False)

    
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
        self.deletePointBtn.setDisabled(True)

    def clear(self):
        self.scene.clear()
        self.img.fill(QColor("white"))
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        self.pointsTable.setRowCount(0)
        self.polygons = []
        self.polygon.clear()
        self.timeLbl.setText("Время заполнения:")

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
        point = Point(self.xSB.value(), self.ySB.value())

        self.addPoint(point)

        painter = QPainter(self.img)

        if self.polygon.num == 0:
            painter.drawPoint(point.x, point.y)
            self.deletePointBtn.setDisabled(False)
        else:
            last = self.polygon.getLastPoint()
            painter.drawLine(last.x, last.y, point.x, point.y)

        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

        self.polygon.addPoint(point)
        if self.polygon.num > 2:
            self.closeFigBtn.setDisabled(False)

    def deleteRow(self):
        num = self.pointsTable.rowCount()
        self.pointsTable.setRowCount(num - 1)

    def handleDeletePoint(self):
        self.deleteRow()

        painter = QPainter(self.img)
        painter.setPen(QColor("white"))

        last = self.polygon.getLastPoint()

        if self.polygon.points:
            self.polygon.deletePoint()

        if self.polygon.num == 0:
            painter.drawPoint(last.x, last.y)
            self.deletePointBtn.setDisabled(True)
        else:
            prev = self.polygon.getLastPoint()
            painter.drawLine(last.x, last.y, prev.x, prev.y)

        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

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
