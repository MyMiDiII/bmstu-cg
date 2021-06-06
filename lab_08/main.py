import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView, QGraphicsScene
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtGui import (
    QPen, QColor, QPainter, QPixmap, QImage
)
from PyQt5.QtCore import QSize, QTime, Qt

import copy
import time

from PyQt5.sip import delete

from MainWindow import Ui_MainWindow

from draw import Canvas
from geometry import Point, Edge, Polygon
from fill import Filler

BACKGROUNDSTRING = "background-color: %s;"


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

        self.setSelectorBtn.setDisabled(True)
        self.tablesInit()

        self.selector = Polygon()
        self.segColor = QColor(38, 255, 0 , 255)
        self.selColor = QColor("red")
        self.resColor = QColor("blue")

        self.segmentsColorBtn.clicked.connect(self.chooseSegColor)
        self.selectorColorBtn.clicked.connect(self.chooseSelColor)
        self.resultColorBtn.clicked.connect(self.chooseResColor)
        
        self.img = QImage(1165, 874, QImage.Format_RGB32)
        self.img.fill(QColor("white"))
        self.scene = Canvas(self, self.img, self.selector)
        self.scene.setSceneRect(0, 0, 1165, 874)
        self.graphicsView.setScene(self.scene)
        self.scene.addPixmap(QPixmap.fromImage(self.img))

        self.addVertexBtn.clicked.connect(self.handleAddPoint)
        self.setSelectorBtn.clicked.connect(self.closeSel)

        self.clearBtn.clicked.connect(self.clear)

    def rools(self):
        title = "Правила ввода"
        text = ("<b>ЛКМ</b> – добавление вершины;<br>"
                + "<b>ПКМ</b> – замкнуть фигуру;<br>"
                + "<b>Ctrl+ЛКМ</b> – установить затравку;<br>"
                + "<b>Shift</b> – горизонтальное/вертикальное ребро.")

        callInfo(title, text)

    def tablesInit(self):
        """
            Начальные настройки таблиц
        """
        self.segmentsTable.setColumnCount(2)
        for i in range(2):
            self.segmentsTable.horizontalHeader().setSectionResizeMode(
                i,
                QHeaderView.Stretch
            )

        self.selectorTable.setColumnCount(2)
        for i in range(2):
            self.selectorTable.horizontalHeader().setSectionResizeMode(
                i,
                QHeaderView.Stretch
            ) 

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
            callError("Незамкнутая область!", "Область не замкнута!")
            return

        self.setBtnsState(True)

        filler = Filler(
            self.scene,
            self.img,
            self.color
        )

        delay = self.delaySB.value()
        painter = QPainter(self.img)
        painter.setPen(QColor(self.color))

        dt = time.time()
        filler.run(painter, self.seed, delay)
        dt = time.time() - dt

        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

    def closeSel(self):
        if self.selector.num < 3:
            self.setSelectorBtn.setDisabled(False)
            return

        painter = QPainter(self.img)
        painter.setPen(QColor(self.selColor))

        first = self.selector.getFirstPoint()
        last = self.selector.getLastPoint()

        painter.drawLine(last.x, last.y, first.x, first.y)

        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))

        painter.end()

        self.selector.isClosed = True
        self.setSelectorBtn.setDisabled(True)
        self.selectorColorBtn.setDisabled(False)


    def clear(self):
        self.scene.clear()
        self.img.fill(QColor("white"))
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        self.segmentsTable.setRowCount(0)
        self.selectorTable.setRowCount(0)
        self.selector.clear()

    def addRow(self, xStr, yStr):
        num = self.selectorTable.rowCount()
        self.selectorTable.setRowCount(num + 1)
        self.selectorTable.setItem(
            num,
            0,
            QTableWidgetItem(xStr)
        )
        self.selectorTable.setItem(
            num,
            1,
            QTableWidgetItem(yStr)
        )

    def addPoint(self, point):
        self.addRow(str(point.x), str(point.y))

    def handleAddPoint(self):
        point = Point(self.xSelSB.value(), self.ySelSB.value())

        painter = QPainter(self.img)

        if self.selector.isClosed:
            painter.setPen(QColor("white"))

            for i, pnt in enumerate(self.selector.points):
                painter.drawLine(
                    pnt.x,
                    pnt.y,
                    self.selector.points[i - 1].x,
                    self.selector.points[i - 1].y,
                )

            self.selectorTable.setRowCount(0)
            self.selector.clear()

        self.addPoint(point)
        painter.setPen(QColor(self.selColor))
        if self.selector.num == 0:
            painter.drawPoint(point.x, point.y)
        else:
            last = self.selector.getLastPoint()
            painter.drawLine(last.x, last.y, point.x, point.y)

        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

        self.selector.addPoint(point)
        if self.selector.num > 2:
            self.setSelectorBtn.setDisabled(False)

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
        else:
            prev = self.polygon.getLastPoint()
            painter.drawLine(last.x, last.y, prev.x, prev.y)

        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

    def chooseSegColor(self):
        """
            Выбор цвета отрезков
        """
        self.segColor = QColorDialog.getColor()
        self.segmentsColorBtn.setStyleSheet(
            BACKGROUNDSTRING % self.segColor.name()
        )

    def chooseSelColor(self):
        """
            Выбор цвета отсекателя
        """
        self.selColor = QColorDialog.getColor()
        self.selectorColorBtn.setStyleSheet(
            BACKGROUNDSTRING % self.selColor.name()
        )

    def chooseResColor(self):
        """
            Выбор цвета результата
        """
        self.resColor = QColorDialog.getColor()
        self.resultColorBtn.setStyleSheet(
            BACKGROUNDSTRING % self.resColor.name()
        ) 

    def chooseColor(self):
        """
            Выбор цвета
        """
        self.color = QColorDialog.getColor()
        self.colorBtn.setStyleSheet(BACKGROUNDSTRING % self.color.name())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Shift:
            self.scene.lineMode = True

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Shift:
            self.scene.lineMode = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.move(250, 100)
    main.setFixedSize(1500, 900)
    main.show()
    sys.exit(app.exec_())
