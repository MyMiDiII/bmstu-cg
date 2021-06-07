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
from draw import Canvas
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

        self.selector = Polygon()
        self.polygon = Polygon()
        self.polygons = []

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

        self.addSelVrtBtn.clicked.connect(self.handleAddPoint)
        self.setSelectorBtn.clicked.connect(self.closeSel)
        #self.addSegmentBtn.clicked.connect(self.handleAddSegment)

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
    
    def conf(self, painter : QPainter):
        painter.setPen(self.selColor)
        painter.setBrush(QColor("white"))

        polygon = []
        for point in self.selector:
            polygon.append(QPoint(point.x, point.y))

        painter.drawPolygon(*polygon)

        painter.setPen(self.resColor)

    def cut(self):
        if not self.selector.isClosed:
            callError("Незамкнутый отсекатель!", "Замкните отсекатель!")
            return

        if not self.polygons:
            callError("Отсутствие многоугольников", "Добавьте многоугольник!")
            return

        painter = QPainter(self.img)
        self.conf(painter)

        cutter = Cutter(self.scene, painter, self.img, self.resColor)

        cutter.run(self.segments, self.selector)

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
        print(len(self.polygons))
        print(self.selector.num)
        self.scene.clear()
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

    def handleAddPoint(self):
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
