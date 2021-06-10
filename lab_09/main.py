import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView, QGraphicsScene
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtGui import (
    QPen, QColor, QPainter, QPixmap, QImage
)
from PyQt5.QtCore import QPoint, QSize, QTime, Qt

import copy
import time

from PyQt5.sip import delete

from MainWindow import Ui_MainWindow

from errors import callError, callInfo
from draw import Canvas, POLYGON, SELECTOR, NONE
from geometry import Point, Segment, Polygon
from cut import Cutter

BACKGROUNDSTRING = "background-color: %s;"


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
        self.setPolygonBtn.setDisabled(True)
        self.tablesInit()

        self.selector = Polygon([])
        self.polygon = Polygon([])
        self.polygons = []

        self.segColor = QColor(38, 255, 0 , 255)
        self.selColor = QColor("red")
        self.resColor = QColor("blue")

        self.segmentsColorBtn.clicked.connect(self.chooseSegColor)
        self.selectorColorBtn.clicked.connect(self.chooseSelColor)
        self.resultColorBtn.clicked.connect(self.chooseResColor)
        
        self.img = QImage(1165, 874, QImage.Format_RGB32)
        self.img.fill(QColor("white"))
        self.scene = Canvas(self, self.img, self.selector, self.polygon)
        self.scene.setSceneRect(0, 0, 1165, 874)
        self.graphicsView.setScene(self.scene)
        self.scene.addPixmap(QPixmap.fromImage(self.img))

        self.addSelVrtBtn.clicked.connect(self.handleAddSelVrt)
        self.addPolVrtBtn.clicked.connect(self.handleAddPolVrt)
        self.setSelectorBtn.clicked.connect(self.closeSel)
        self.setPolygonBtn.clicked.connect(self.closePol)

        self.selectBtn.clicked.connect(self.cut)
        self.clearBtn.clicked.connect(self.clear)
        self.roolsBtn.clicked.connect(self.rools)

    def rools(self):
        title = "Правила ввода"
        text = ("<b>ЛКМ</b> – добавление многоугольника;<br>"
                + "<b>ПКМ</b> – добавление отсекателя;<br>"
                + "<b>ЦКМ(колесико)</b> – замыкание фигуры;<br>"
                + "<b>Shift</b> – горизонтальное/вертикальное ребро.")

        callInfo(title, text)

    def tablesInit(self):
        """
            Начальные настройки таблиц
        """
        self.polygonsTable.setColumnCount(2)
        for i in range(2):
            self.polygonsTable.horizontalHeader().setSectionResizeMode(
                i,
                QHeaderView.Stretch
            )

        self.selectorTable.setColumnCount(2)
        for i in range(2):
            self.selectorTable.horizontalHeader().setSectionResizeMode(
                i,
                QHeaderView.Stretch
            ) 

    def cut(self):
        if not self.selector.isClosed:
            callError("Незамкнутый отсекатель!", "Замкните отсекатель!")
            return

        if not self.polygons:
            callError("Отсутствие многоугольников", "Добавьте многоугольник!")
            return

        painter = QPainter(self.img)
        pen = QPen()
        pen.setColor(self.resColor)
        pen.setWidth(2)
        painter.setPen(pen)

        cutter = Cutter(self.scene, painter, self.img, self.resColor)

        cutter.run(self.polygons, self.selector)

        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

    def clear(self):
        self.scene.clear()
        self.scene.mode = NONE
        self.img.fill(QColor("white"))
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        self.polygonsTable.setRowCount(0)
        self.selectorTable.setRowCount(0)
        self.selector.clear()
        self.polygon.clear()
        self.polygons = []

    def addRow(self, table, xStr, yStr):
        num = table.rowCount()
        table.setRowCount(num + 1)
        table.setItem(
            num,
            0,
            QTableWidgetItem(xStr)
        )
        table.setItem(
            num,
            1,
            QTableWidgetItem(yStr)
        )

    def addPoint(self, table, point):
        self.addRow(table, str(point.x), str(point.y))

    def handleAddSelVrt(self):
        if self.scene.mode == POLYGON:
            callInfo("Незаконченный ввод", "Закончите ввод многоугольника!")
            return

        self.scene.mode = SELECTOR

        point = Point(self.xSelSB.value(), self.ySelSB.value())

        painter = QPainter(self.img)

        if self.selector.isClosed:
            painter.setPen(QColor("white"))

            for i, pnt in enumerate(self.selector):
                painter.drawLine(
                    pnt.x,
                    pnt.y,
                    self.selector[i - 1].x,
                    self.selector[i - 1].y,
                )

            self.selectorTable.setRowCount(0)
            self.selector.clear()

        self.addPoint(self.selectorTable, point)
        painter.setPen(QColor(self.selColor))

        if not self.selector.num:
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

        self.scene.mode = NONE
        self.selector.isClosed = True
        self.setSelectorBtn.setDisabled(True)
        self.selectorColorBtn.setDisabled(False)
        self.addRow(self.selectorTable, "end", "end")

    def handleAddPolVrt(self):
        if self.scene.mode == SELECTOR:
            callInfo("Незаконченный ввод", "Закончите ввод отсекателя!")
            return

        self.scene.mode = POLYGON

        point = Point(self.xPolSB.value(), self.yPolSB.value())

        painter = QPainter(self.img)

        self.addPoint(self.polygonsTable, point)
        painter.setPen(QColor(self.segColor))

        if not self.polygon.num:
            painter.drawPoint(point.x, point.y)
        else:
            last = self.polygon.getLastPoint()
            painter.drawLine(last.x, last.y, point.x, point.y)

        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

        self.polygon.addPoint(point)
        if self.polygon.num > 2:
            self.setPolygonBtn.setDisabled(False)

    def closePol(self):
        if self.polygon.num < 3:
            self.setPolygonBtn.setDisabled(False)
            return

        painter = QPainter(self.img)
        painter.setPen(QColor(self.segColor))

        first = self.polygon.getFirstPoint()
        last = self.polygon.getLastPoint()

        painter.drawLine(last.x, last.y, first.x, first.y)

        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))

        painter.end()

        self.scene.mode = NONE
        self.polygon.isClosed = True
        self.polygons.append(copy.deepcopy(self.polygon))
        self.polygon.clear()
        self.setPolygonBtn.setDisabled(True)
        self.segmentsColorBtn.setDisabled(False)
        self.addRow(self.polygonsTable, "end", "end")

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
