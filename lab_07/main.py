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
from geometry import Point, Segment
from cut import Cutter

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

# TODO формирование списка отрезков
# TODO сохранение отсекателя
# TODO selectOr

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
        self.tablesInit()
        self.selecter = [-1, -1, -1, -1]
        self.segments = []

        self.segColor = QColor("black")
        self.selColor = QColor("red")
        self.resColor = QColor("green")

        self.img = QImage(1164, 874, QImage.Format_RGB32)
        self.img.fill(QColor("white"))
        self.scene = Canvas(self, self.img)
        self.scene.setSceneRect(0, 0, 1164, 874)
        self.graphicsView.setScene(self.scene)
        self.scene.addPixmap(QPixmap.fromImage(self.img))

        self.segmentsColorBtn.clicked.connect(self.chooseSegColor)
        self.selecterColorBtn.clicked.connect(self.chooseSelColor)
        self.resultColorBtn.clicked.connect(self.chooseResColor)

        self.addSegmentBtn.clicked.connect(self.handleAddSegment)
        self.setSelecterBtn.clicked.connect(self.handleSetSegment)
        self.selectBtn.clicked.connect(self.cut)

        self.clearBtn.clicked.connect(self.clear)
        self.roolsBtn.clicked.connect(self.rools)

    def rools(self):
        title = "Правила ввода"
        text = ("<b>ЛКМ</b> – ввод отрезка;<br>"
                + "<b>ПКМ</b> – ввод отсекателя;<br>"
                + "<b>Shift</b> – горизонтальный/вертикальный отрезок.")

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

        self.selecterTable.setColumnCount(4)
        for i in range(4):
            self.selecterTable.horizontalHeader().setSectionResizeMode(
                i,
                QHeaderView.Stretch
            )

    def clear(self):
        self.scene.clear()
        self.img.fill(QColor("white"))
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        self.segmentsTable.setRowCount(0)
        self.selecterTable.setRowCount(0)
        self.selecter = [-1, -1, -1, -1]
        self.segments = []

    def cut(self):
        painter = QPainter(self.img)
        painter.setPen(QColor(self.resColor))

        cutter = Cutter(self.scene, painter, self.img, self.resColor)

        cutter.run(self.segments, self.selecter)

        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

    def addSegmentRow(self, point1Str, point2Str):
        num = self.segmentsTable.rowCount()
        self.segmentsTable.setRowCount(num + 1)
        self.segmentsTable.setItem(
            num,
            0,
            QTableWidgetItem(point1Str)
        )
        self.segmentsTable.setItem(
            num,
            1,
            QTableWidgetItem(point2Str)
        )

    def addSegment(self, seg):
        strX1 = str(seg.begin.x)
        strY1 = str(seg.begin.y)
        point1 = '(' + strX1 + ',' + strY1 + ')'
        strX2 = str(seg.end.x)
        strY2 = str(seg.end.y)
        point2 = '(' + strX2 + ',' + strY2 + ')'
        self.addSegmentRow(point1, point2)

    def handleAddSegment(self):
        point1 = Point(self.x1SB.value(), self.y1SB.value())
        point2 = Point(self.x2SB.value(), self.y2SB.value())
        segment = Segment(point1, point2)

        self.segments.append(segment)
        self.addSegment(segment)

        painter = QPainter(self.img)
        painter.setPen(QColor(self.segColor))

        painter.drawLine(
            point1.x,
            point1.y,
            point2.x,
            point2.y
        )

        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

    def setSelecterRow(self, xLeft, xRigth, yLow, yTop):
        self.selecterTable.setRowCount(1)
        self.selecterTable.setItem(
            0,
            0,
            QTableWidgetItem(xLeft)
        )
        self.selecterTable.setItem(
            0,
            1,
            QTableWidgetItem(xRigth)
        )
        self.selecterTable.setItem(
            0,
            2,
            QTableWidgetItem(yLow)
        )
        self.selecterTable.setItem(
            0,
            3,
            QTableWidgetItem(yTop)
        )

    def handleSetSegment(self):
        xLeft = self.xLeftSB.value()
        yLow = self.yLowSB.value()
        xRight = self.xRightSB.value()
        yTop = self.yTopSB.value()

        if xLeft > xRight:
            xLeft, xRight = xRight, xLeft

        if yLow > yTop:
            yLow, yTop = yTop, yLow

        self.selecter = [xLeft, xRight, yLow, yTop]

        self.setSelecterRow(
            str(xLeft),
            str(xRight),
            str(yLow),
            str(yTop)
        )

        painter = QPainter(self.img)
        painter.setPen(QColor(self.selColor))

        painter.drawLine(xLeft, yLow, xRight, yLow)
        painter.drawLine(xRight, yLow, xRight, yTop)
        painter.drawLine(xRight, yTop, xLeft, yTop)
        painter.drawLine(xLeft, yTop, xLeft, yLow)

        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

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
        self.selecterColorBtn.setStyleSheet(
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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Shift:
            self.scene.lineMode = True

        if event.key() == Qt.Key_Control:
            self.scene.seedMode = True

        if event.key() == Qt.Key_Escape:
            self.window.handleDeletePoint()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Shift:
            self.scene.lineMode = False

        if event.key() == Qt.Key_Control:
            self.scene.seedMode = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.move(250, 100)
    main.setFixedSize(1500, 900)
    main.show()
    sys.exit(app.exec_())
