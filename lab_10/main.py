from math import cos, isclose, pi, sin
import sys
from copy import deepcopy

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

        self.xAngle = 0
        self.yAngle = 0
        self.zAngle = 0

        self.img = QImage(self.sceneWidth, self.sceneHeight, QImage.Format_RGB32)
        self.img.fill(QColor("white"))
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, self.sceneWidth, self.sceneHeight)
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        self.graphicsView.setScene(self.scene)

        self.color = QColor(92, 53, 102)
        self.colorBtn.clicked.connect(self.chooseColor)

        self.funcCB.currentIndexChanged.connect(self.clearTurn)

        self.clearBtn.clicked.connect(self.clear)
        self.drawBtn.clicked.connect(self.handleDraw)
        self.scaleBtn.clicked.connect(self.draw)
        self.xRotateBtn.clicked.connect(self.xRotate)
        self.yRotateBtn.clicked.connect(self.yRotate)
        self.zRotateBtn.clicked.connect(self.zRotate)

    def readXRange(self):
        begin = self.xFromDSB.value()
        end = self.xToDSB.value()
        step = self.xStepDSB.value()

        if isclose(step, 0, abs_tol=EPS):
            return None
        
        num = (end - begin) / step

        if num < 0 or isclose(num, 0, abs_tol=EPS):
            return None

        if step < 0:
            begin, end = end, begin
            step = -step

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

        if step < 0:
            begin, end = end, begin
            step = -step

        return Range(begin, end, step)

    def addTransform(self, matrix1, matrix2):
        result = [[0 for i in range(4)] for j in range(4)]

        for i in range(4):
            for j in range(4):
                for k in range(4):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

        for i in range(4):
            for j in range(4):
                matrix1[i][j] = result[i][j]
        matrix1 = result

    def xRotate(self):
        self.xAngle += self.rotateDSB.value() / 180 * pi
        self.draw()

    def yRotate(self):
        self.yAngle += self.rotateDSB.value() / 180 * pi
        self.draw()

    def zRotate(self):
        self.zAngle += self.rotateDSB.value() / 180 * pi
        self.draw()

    def getTransformMatrix(self):
        scale = self.scaleCoefSB.value()
        result = [[int(i == j) for i in range(4)] for j in range(4)]

        xRotateMatrix = [[1, 0, 0, 0],
                         [0, cos(self.xAngle), sin(self.xAngle), 0],
                         [0, -sin(self.xAngle), cos(self.xAngle), 0],
                         [0, 0, 0, 1]]
        self.addTransform(result, xRotateMatrix)

        yRotateMatrix = [[cos(self.yAngle), 0, -sin(self.yAngle), 0],
                        [0, 1, 0, 0],
                        [sin(self.yAngle), 0, cos(self.yAngle), 0],
                        [0, 0, 0, 1] ]
        self.addTransform(result, yRotateMatrix)

        zRotateMatrix = [[cos(self.zAngle), sin(self.zAngle), 0, 0],
                        [-sin(self.zAngle), cos(self.zAngle), 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]]
        self.addTransform(result, zRotateMatrix)

        scaleMatrix = [[scale, 0, 0, 0],
                       [0, scale, 0, 0],
                       [0, 0, scale, 0],
                       [0, 0, 0, 1]]
        self.addTransform(result, scaleMatrix)

        result[3][0] = self.centre.x
        result[3][1] = self.centre.y

        return result

    def handleDraw(self):
        self.clearTurn()
        self.draw()

    def draw(self):
        xRange = self.readXRange()
        zRange = self.readZRange()
        func = funcs[self.funcCB.currentIndex()]
        
        matrix = self.getTransformMatrix()

        if not xRange or not zRange:
            callError("Недопустимые интервалы",
                      "Проверьте корректность введенных интервалов!")
            return

        self.img.fill(QColor("white"))
        painter = QPainter(self.img)
        painter.setPen(self.color)

        drawer = Func3DDrawer(
            painter,
            self.color,
            self.sceneWidth,
            self.sceneHeight,
            matrix,
            xRange,
            zRange,
            func
        )

        drawer.run()
        
        painter.end()
        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.img))

    def clearTurn(self):
        self.xAngle = 0
        self.yAngle = 0
        self.zAngle = 0

    def clear(self):
        """
            Очистка
        """
        self.scene.clear()
        self.img.fill(QColor("white"))
        self.scene.addPixmap(QPixmap.fromImage(self.img))

        self.clearTurn()


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
