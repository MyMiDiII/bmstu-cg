from math import isclose
import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView, QGraphicsScene
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtGui import (
    QPen, QColor, QPainter, QPixmap, QImage
)
from PyQt5.QtCore import QPoint, QSize, QTime, Qt

from MainWindow import Ui_MainWindow

from errors import callError, callInfo
from geometry import Point, Range
from Func3DDrawer import Func3DDrawer
from funcs import funcs

BACKGROUNDSTRING = "background-color: %s;"
EPS = 1e-6

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
        self.sceneWidth = 1474 
        self.sceneHeight = 759
        self.centre = Point(self.sceneWidth // 2, self.sceneHeight // 2)

        self.img = QImage(self.sceneWidth, self.sceneHeight, QImage.Format_RGB32)
        self.img.fill(QColor("white"))
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, self.sceneWidth, self.sceneHeight)
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        self.graphicsView.setScene(self.scene)

        self.color = QColor(92, 53, 102)
        self.colorBtn.clicked.connect(self.chooseColor)

        self.clearBtn.clicked.connect(self.clear)
        self.drawBtn.clicked.connect(self.draw)

    def readXRange(self):
        begin = self.xFromDSB.value()
        end = self.xToDSB.value()
        step = self.xStepDSB.value()

        if isclose(step, 0, abs_tol=EPS):
            return None

        if (end - begin) / step < 0:
            return None

        return Range(begin, end, step)


    def readZRange(self):
        begin = self.zFromDSB.value()
        end = self.zToDSB.value()
        step = self.zStepDSB.value()

        if isclose(step, 0, abs_tol=EPS):
            return None

        num = (end - begin) / step

        if num < 0 or isclose(num, 0, abs_tol=EPS):
            return None

        return Range(begin, end, step)


    def draw(self):
        xRange = self.readXRange()
        zRange = self.readZRange()
        func = funcs[self.funcCB.currentIndex()]

        if not xRange or not zRange:
            callError("Недопустимые интервалы",
                      "Проверьте корректность введенных интервалов!")
            return

        self.img.fill(QColor("white"))
        painter = QPainter(self.img)

        drawer = Func3DDrawer(
            self.img,
            self.sceneWidth,
            self.sceneHeight,
            self.color,
            xRange,
            zRange
        )

        drawer.run()
        
        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))

    def clear(self):
        """
            Очистка
        """
        DBSs = [
            self.xFromDSB,
            self.xToDSB,
            self.xStepDSB,
            self.zFromDSB,
            self.zToDSB,
            self.zStepDSB,
            self.rotateDSB
        ]

        for DSB in DBSs:
            DSB.setValue(0)

        self.scene.clear()
        self.img.fill(QColor("white"))
        self.scene.addPixmap(QPixmap.fromImage(self.img))


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
