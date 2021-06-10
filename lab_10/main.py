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
from geometry import Point

BACKGROUNDSTRING = "background-color: %s;"

SCENEWIDTH = 1474
SCENEHEIGHT = 759

CENTRE = Point(SCENEWIDTH // 2, SCENEHEIGHT // 2)

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

        self.img = QImage(SCENEWIDTH, SCENEHEIGHT, QImage.Format_RGB32)
        self.img.fill(QColor("white"))
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, SCENEWIDTH, SCENEHEIGHT)
        self.scene.addPixmap(QPixmap.fromImage(self.img))
        self.graphicsView.setScene(self.scene)

        self.color = QColor(92, 53, 102)
        self.colorBtn.clicked.connect(self.chooseColor)

        self.clearBtn.clicked.connect(self.clear)


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
