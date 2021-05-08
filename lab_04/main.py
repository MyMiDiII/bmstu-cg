import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView, QGraphicsScene
from PyQt5.QtGui import QPen, QColor

import matplotlib.pyplot as plt
import time

from MainWindow import Ui_MainWindow

import circle
import ellipce


SCENEWIDTH = 979
SCENEHEIGHT = 809

CENTRE = { "X" : SCENEWIDTH // 2, "Y" : SCENEHEIGHT // 2}


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
        self.scene.setSceneRect(0, 0, SCENEWIDTH, SCENEHEIGHT)
        self.graphicsView.setScene(self.scene)

        self.pen = QPen()
        self.colorCB.currentIndexChanged.connect(self.setColor)

        self.timeBtn.clicked.connect(self.getTime)
        self.clearBtn.clicked.connect(self.scene.clear)


    def getTime(self):
        funs = [
            circle.canon,
            circle.parametric,
            circle.brezenham,
            circle.midpoint,
            circle.libfunc
            ]

        for i in range(5):
            timesList = []
            rList = []
            for r in range(1, 10000, 1000):
                sumtime = 0
                for _ in range(20):
                    start = time.time()
                    funs[i](450, 400, r, self.scene, self.pen)
                    sumtime += time.time() - start

                timesList.append(sumtime / 20)
                rList.append(r)
            plt.plot(rList, timesList, label=str(funs[i]))

        plt.legend()
        plt.show()


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

        funs[self.algoCB.currentIndex()](Xc, Yc, Ra, Rb, self.scene, self.pen)


    def drawCircleSpectrum(self):
        Rb = self.cirSpRbSB.value()
        Re = self.cirSpReSB.value()
        step = self.cirSpStepSB.value()
        num = self.cirSpNumSB.value()
        curConf = self.cirSpConfCB.currentIndex()

        if curConf == 0:
            Rb = Re - step * num

            if Rb < 0:
                print("ERROR")
                return

        if curConf == 2:
            if not num:
                print("ERROR")
                return

            step = (Re - Rb) / num

            if abs(step) < 1e-6 or step < 0:
                print("ERROR")
                return

        if curConf == 3:
            if not step:
                print("ERROR")
                return

            num = (Re - Rb) // step + 1

            if num <= 0:
                print("ERROR")
                return


        funs = [
            circle.canon,
            circle.parametric,
            circle.brezenham,
            circle.midpoint,
            circle.libfunc
            ]

        R = Rb

        for _ in range(num):
            funs[self.algoCB.currentIndex()](
                CENTRE["X"],
                CENTRE["Y"],
                R,
                self.scene,
                self.pen
            )

            R += step


    def drawEllipceSpectrum(self):
        RaB = self.elSpRaSB.value()
        RbB = self.elSpRbSB.value()
        step = self.elSpStepSB.value()
        num = self.elSpNumSB.value()

        funs = [
            ellipce.canon,
            ellipce.parametric,
            ellipce.brezenham,
            ellipce.midpoint,
            ellipce.libfunc
        ]

        conf = self.elSpConfCB.currentIndex()

        Ra = RaB
        Rb = RbB
        coef = (Ra * Ra / Rb / Rb
                if conf
                else Rb * Rb / Ra / Ra)

        for _ in range(num):
            funs[self.algoCB.currentIndex()](
                CENTRE["X"],
                CENTRE["Y"],
                Ra,
                Rb,
                self.scene,
                self.pen
            )

            if conf:
                Rb += step
                Ra = Rb * coef
            else:
                Ra += step
                Rb = Ra * coef
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.move(200, 100)
    main.setFixedSize(1451, 836)
    main.show()
    sys.exit(app.exec_())
