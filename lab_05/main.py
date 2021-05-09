import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView, QGraphicsScene
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtGui import (
    QPen, QColor, QPainter, QPixmap, QImage
)
from PyQt5.QtCore import QSize

from MainWindow import Ui_MainWindow

from geometry import Point, Edge, Polygon

BACKGROUNDSTRING = ("background-color: qlineargradient(spread:pad, "
                   + "x1:0, y1:0, x2:0, y2:0, stop:0 %s"
                   + ", stop:1 rgba(255, 255, 255, 255));")


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

        self.polygons = []
        self.polygon = Polygon()
        
        self.colorBtn.clicked.connect(self.chooseColor)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 1185, 874)
        self.graphicsView.setScene(self.scene)
        self.img = QImage(1185, 874, QImage.Format_RGB32)
        self.img.fill(QColor("white"))
        self.scene.addPixmap(QPixmap.fromImage(self.img))

        self.addPointBtn.clicked.connect(self.addPoint)
        #self.closeFigBtn.clicked.connect(self.closeFigBtn)

        self.clearBtn.clicked.connect(self.clear)

        self.draw()

    def clear(self):
        self.scene.clear()
        self.img.fill(QColor("white"))
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        self.pointsTable.setRowCount(0)

    def addPoint(self):
        """
            Добавление вершины
        """
        point = Point(self.xSB.value(), self.ySB.value())

        num = self.pointsTable.rowCount()
        self.pointsTable.setRowCount(num + 1)
        self.pointsTable.setItem(
            num,
            0,
            QTableWidgetItem(str(point.x))
        )
        self.pointsTable.setItem(
            num,
            1,
            QTableWidgetItem(str(point.y))
        )

        painter = QPainter(self.img)

        if self.polygon.num == 0:
            painter.drawPoint(point.x, point.y)
        else:
            last = self.polygon.getLastPoint()
            painter.drawLine(last.x, last.y, point.x, point.y)

        self.scene.addPixmap(QPixmap.fromImage(self.img))
        painter.end()

        self.polygon.addPoint(point)


    def chooseColor(self):
        """
            Выбор цвета
        """
        self.color = QColorDialog.getColor()
        self.colorBtn.setStyleSheet(BACKGROUNDSTRING % self.color.name())

    def draw(self):
        for x in range(0, 100):
            self.img.setPixelColor(x, 100, QColor("black"))

        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))

        print(self.img.pixelColor(0, 100).name())
        print(self.img.pixelColor(0, 101).name())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.move(250, 100)
    main.setFixedSize(1500, 900)
    main.show()
    sys.exit(app.exec_())
