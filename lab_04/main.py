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
import math


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
            ]

        plt.figure(figsize=(14.6, 7.9))
        plt.get_current_fig_manager().window.move(250, 100)
        for i in range(4):
            timesList = []
            rList = []
            for r in range(0, 10000, 1000):
                sumtime = 0
                for _ in range(50):
                    start = time.time()
                    funs[i](450, 400, r, self.scene, self.pen, False)
                    sumtime += time.time() - start

                timesList.append(sumtime / 50)
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

        funs[self.algoCB.currentIndex()](Xc, Yc, R, self.scene, self.pen)


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
                callError(
                    "Ошибка в значениях параметров!",
                    "При заданных значениях некоторые радиусы"
                    + " окружностей в спектре будут отрицательны!"
                )
                return

        if curConf == 2 and num:
            step = (Re - Rb) / num


        if curConf == 3:
            if not step:
                callError(
                    "Нулевой шаг!",
                    "Шаг спектра должен быть отличен от нуля!"
                )
                return

            num = abs(Re - Rb) // step + 1


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
            R = int(math.ceil(R))


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
        coef = (Ra / Rb
                if conf
                else Rb / Ra)

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
                Ra = int(math.ceil(Rb * coef))
            else:
                Ra += step
                Rb = int(math.ceil(Ra * coef))
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.move(250, 100)
    main.setFixedSize(1451, 836)
    main.show()
    sys.exit(app.exec_())
