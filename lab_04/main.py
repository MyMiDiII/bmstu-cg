import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView, QGraphicsScene
from PyQt5.QtGui import QPen, QColor

from MainWindow import Ui_MainWindow

import circle
import ellipce
import point


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
        self.switch()
        self.cirConf()

        self.cirSpConfCB.currentIndexChanged.connect(self.cirConf)
        self.figureCB.currentIndexChanged.connect(self.switch)

        self.cirBtn.clicked.connect(self.drawCircle)
        self.elBtn.clicked.connect(self.drawEllipce)
        self.cirSpBtn.clicked.connect(self.drawCircleSpectrum)
        self.elSpBtn.clicked.connect(self.drawEllipceSpectrum)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 979, 809)
        self.graphicsView.setScene(self.scene)

        self.pen = QPen()
        self.colorCB.currentIndexChanged.connect(self.setColor)

        self.clearBtn.clicked.connect(self.scene.clear)


    def setColor(self):
        colors = [
            "black",
            "white",
            "blue",
            "red"
        ]
        self.pen.setColor(QColor(colors[self.colorCB.currentIndex()]))


    def switch(self):
        self.figureSW.setCurrentIndex(
                self.figureCB.currentIndex()
                )
        self.spectrumSW.setCurrentIndex(
                self.figureCB.currentIndex()
                )


    def cirConf(self):
        spinBoxes = [
            self.cirSpRbSB,
            self.cirSpReSB,
            self.cirSpStepSB,
            self.cirSpNumSB
            ]

        for i, SB in enumerate(spinBoxes):
            SB.setDisabled(i == self.cirSpConfCB.currentIndex())


    def drawCircle(self):
        Xc = self.cirXcSB.value()
        Yc = self.cirYcSB.value()
        R = self.cirRSB.value()

        funs = [
            circle.canon,
            circle.parametric,
            circle.brezenham,
            circle.midpoint,
            circle.libfunc
            ]

        xy = funs[self.algoCB.currentIndex()](Xc, Yc, R, self.scene, self.pen)

        print(len(xy))
        for xandy in xy:
            print(xandy)


    def drawEllipce(self):
        Xc = self.elXcSB.value()
        Yc = self.elYcSB.value()
        Ra = self.elRaSB.value()
        Rb = self.elRbSB.value()
        funs = [
            ellipce.canon,
            ellipce.parametric,
            ellipce.brezenham,
            ellipce.midpoint,
            ellipce.libfunc
            ]

        funs[self.algoCB.currentIndex()](Xc, Yc, Ra, Rb, self.scene)


    def drawCircleSpectrum(self):
        Xc = self.cirXcSB.value()
        Yc = self.cirYcSB.value()
        R = self.cirRSB.value()
        funs = [
            circle.canon,
            circle.parametric,
            circle.brezenham,
            circle.midpoint,
            circle.libfunc
            ]

        funs[self.algoCB.currentIndex()](Xc, Yc, R)


    def drawEllipceSpectrum(self):
        Xc = self.elXcSB.value()
        Yc = self.elYcSB.value()
        Ra = self.elRaSB.value()
        Rb = self.elRbSB.value()
        funs = [
            ellipce.canon,
            ellipce.parametric,
            ellipce.brezenham,
            ellipce.midpoint,
            ellipce.libfunc]

        funs[self.algoCB.currentIndex()](Xc, Yc, Ra, Rb)
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.move(200, 100)
    main.show()
    sys.exit(app.exec_())
