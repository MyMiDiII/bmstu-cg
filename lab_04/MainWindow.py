# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1451, 836)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 440, 813))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.colorGB = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.colorGB.setObjectName("colorGB")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.colorGB)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.colorCB = QtWidgets.QComboBox(self.colorGB)
        self.colorCB.setObjectName("colorCB")
        self.colorCB.addItem("")
        self.colorCB.addItem("")
        self.colorCB.addItem("")
        self.colorCB.addItem("")
        self.horizontalLayout_3.addWidget(self.colorCB)
        self.verticalLayout.addWidget(self.colorGB)
        self.algoGB = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.algoGB.setObjectName("algoGB")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.algoGB)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.algoCB = QtWidgets.QComboBox(self.algoGB)
        self.algoCB.setObjectName("algoCB")
        self.algoCB.addItem("")
        self.algoCB.addItem("")
        self.algoCB.addItem("")
        self.algoCB.addItem("")
        self.algoCB.addItem("")
        self.horizontalLayout.addWidget(self.algoCB)
        self.verticalLayout.addWidget(self.algoGB)
        self.figureGB = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.figureGB.setObjectName("figureGB")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.figureGB)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.figureCB = QtWidgets.QComboBox(self.figureGB)
        self.figureCB.setObjectName("figureCB")
        self.figureCB.addItem("")
        self.figureCB.addItem("")
        self.horizontalLayout_2.addWidget(self.figureCB)
        self.verticalLayout.addWidget(self.figureGB)
        self.figureSetGB = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.figureSetGB.setObjectName("figureSetGB")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.figureSetGB)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.figureSW = QtWidgets.QStackedWidget(self.figureSetGB)
        self.figureSW.setObjectName("figureSW")
        self.cirPage = QtWidgets.QWidget()
        self.cirPage.setObjectName("cirPage")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.cirPage)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.cirXcLbl = QtWidgets.QLabel(self.cirPage)
        self.cirXcLbl.setObjectName("cirXcLbl")
        self.gridLayout_6.addWidget(self.cirXcLbl, 0, 0, 1, 1)
        self.cirXcSB = QtWidgets.QSpinBox(self.cirPage)
        self.cirXcSB.setMaximum(981)
        self.cirXcSB.setObjectName("cirXcSB")
        self.gridLayout_6.addWidget(self.cirXcSB, 0, 1, 1, 1)
        self.cirCentreBtn = QtWidgets.QPushButton(self.cirPage)
        self.cirCentreBtn.setObjectName("cirCentreBtn")
        self.gridLayout_6.addWidget(self.cirCentreBtn, 0, 2, 2, 1)
        self.cirYcLbl = QtWidgets.QLabel(self.cirPage)
        self.cirYcLbl.setObjectName("cirYcLbl")
        self.gridLayout_6.addWidget(self.cirYcLbl, 1, 0, 1, 1)
        self.cirYcSB = QtWidgets.QSpinBox(self.cirPage)
        self.cirYcSB.setMaximum(811)
        self.cirYcSB.setObjectName("cirYcSB")
        self.gridLayout_6.addWidget(self.cirYcSB, 1, 1, 1, 1)
        self.cirRLbl = QtWidgets.QLabel(self.cirPage)
        self.cirRLbl.setObjectName("cirRLbl")
        self.gridLayout_6.addWidget(self.cirRLbl, 2, 0, 1, 1)
        self.cirRSB = QtWidgets.QSpinBox(self.cirPage)
        self.cirRSB.setMaximum(1000)
        self.cirRSB.setObjectName("cirRSB")
        self.gridLayout_6.addWidget(self.cirRSB, 2, 1, 1, 2)
        self.cirBtn = QtWidgets.QPushButton(self.cirPage)
        self.cirBtn.setObjectName("cirBtn")
        self.gridLayout_6.addWidget(self.cirBtn, 3, 0, 1, 3)
        self.figureSW.addWidget(self.cirPage)
        self.elPage = QtWidgets.QWidget()
        self.elPage.setObjectName("elPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.elPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.elXcLbl = QtWidgets.QLabel(self.elPage)
        self.elXcLbl.setObjectName("elXcLbl")
        self.gridLayout_2.addWidget(self.elXcLbl, 0, 0, 1, 1)
        self.elXcSB = QtWidgets.QSpinBox(self.elPage)
        self.elXcSB.setMaximum(981)
        self.elXcSB.setObjectName("elXcSB")
        self.gridLayout_2.addWidget(self.elXcSB, 0, 1, 1, 1)
        self.elYcLbl = QtWidgets.QLabel(self.elPage)
        self.elYcLbl.setObjectName("elYcLbl")
        self.gridLayout_2.addWidget(self.elYcLbl, 0, 2, 1, 1)
        self.elYcSB = QtWidgets.QSpinBox(self.elPage)
        self.elYcSB.setMaximum(811)
        self.elYcSB.setObjectName("elYcSB")
        self.gridLayout_2.addWidget(self.elYcSB, 0, 3, 1, 2)
        self.elCentreBtn = QtWidgets.QPushButton(self.elPage)
        self.elCentreBtn.setObjectName("elCentreBtn")
        self.gridLayout_2.addWidget(self.elCentreBtn, 0, 5, 1, 1)
        self.elRaLbl = QtWidgets.QLabel(self.elPage)
        self.elRaLbl.setObjectName("elRaLbl")
        self.gridLayout_2.addWidget(self.elRaLbl, 1, 0, 1, 1)
        self.elRaSB = QtWidgets.QSpinBox(self.elPage)
        self.elRaSB.setMaximum(1000)
        self.elRaSB.setObjectName("elRaSB")
        self.gridLayout_2.addWidget(self.elRaSB, 1, 1, 1, 1)
        self.elRbLbl = QtWidgets.QLabel(self.elPage)
        self.elRbLbl.setObjectName("elRbLbl")
        self.gridLayout_2.addWidget(self.elRbLbl, 1, 2, 1, 2)
        self.elRbSB = QtWidgets.QSpinBox(self.elPage)
        self.elRbSB.setMaximum(1000)
        self.elRbSB.setObjectName("elRbSB")
        self.gridLayout_2.addWidget(self.elRbSB, 1, 4, 1, 2)
        self.elBtn = QtWidgets.QPushButton(self.elPage)
        self.elBtn.setObjectName("elBtn")
        self.gridLayout_2.addWidget(self.elBtn, 2, 0, 1, 6)
        self.figureSW.addWidget(self.elPage)
        self.gridLayout_3.addWidget(self.figureSW, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.figureSetGB)
        self.spectrumGB = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.spectrumGB.setObjectName("spectrumGB")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.spectrumGB)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.spectrumSW = QtWidgets.QStackedWidget(self.spectrumGB)
        self.spectrumSW.setObjectName("spectrumSW")
        self.cirSpPage = QtWidgets.QWidget()
        self.cirSpPage.setObjectName("cirSpPage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.cirSpPage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.cirSpNumLbl = QtWidgets.QLabel(self.cirSpPage)
        self.cirSpNumLbl.setObjectName("cirSpNumLbl")
        self.gridLayout_4.addWidget(self.cirSpNumLbl, 2, 2, 1, 2)
        self.cirSpRbLbl = QtWidgets.QLabel(self.cirSpPage)
        self.cirSpRbLbl.setObjectName("cirSpRbLbl")
        self.gridLayout_4.addWidget(self.cirSpRbLbl, 1, 0, 1, 1)
        self.cirSpStepLbl = QtWidgets.QLabel(self.cirSpPage)
        self.cirSpStepLbl.setObjectName("cirSpStepLbl")
        self.gridLayout_4.addWidget(self.cirSpStepLbl, 1, 2, 1, 2)
        self.cirSpStepSB = QtWidgets.QSpinBox(self.cirSpPage)
        self.cirSpStepSB.setMinimum(1)
        self.cirSpStepSB.setMaximum(10000)
        self.cirSpStepSB.setObjectName("cirSpStepSB")
        self.gridLayout_4.addWidget(self.cirSpStepSB, 1, 4, 1, 1)
        self.cirSpReLbl = QtWidgets.QLabel(self.cirSpPage)
        self.cirSpReLbl.setObjectName("cirSpReLbl")
        self.gridLayout_4.addWidget(self.cirSpReLbl, 2, 0, 1, 1)
        self.cirSpReSB = QtWidgets.QSpinBox(self.cirSpPage)
        self.cirSpReSB.setMaximum(10000)
        self.cirSpReSB.setObjectName("cirSpReSB")
        self.gridLayout_4.addWidget(self.cirSpReSB, 2, 1, 1, 1)
        self.cirSpRbSB = QtWidgets.QSpinBox(self.cirSpPage)
        self.cirSpRbSB.setMaximum(10000)
        self.cirSpRbSB.setObjectName("cirSpRbSB")
        self.gridLayout_4.addWidget(self.cirSpRbSB, 1, 1, 1, 1)
        self.cirSpNumSB = QtWidgets.QSpinBox(self.cirSpPage)
        self.cirSpNumSB.setMinimum(1)
        self.cirSpNumSB.setMaximum(10000)
        self.cirSpNumSB.setObjectName("cirSpNumSB")
        self.gridLayout_4.addWidget(self.cirSpNumSB, 2, 4, 1, 1)
        self.cirSpBtn = QtWidgets.QPushButton(self.cirSpPage)
        self.cirSpBtn.setObjectName("cirSpBtn")
        self.gridLayout_4.addWidget(self.cirSpBtn, 3, 0, 1, 5)
        self.cirSpConfLbl = QtWidgets.QLabel(self.cirSpPage)
        self.cirSpConfLbl.setObjectName("cirSpConfLbl")
        self.gridLayout_4.addWidget(self.cirSpConfLbl, 0, 0, 1, 2)
        self.cirSpConfCB = QtWidgets.QComboBox(self.cirSpPage)
        self.cirSpConfCB.setObjectName("cirSpConfCB")
        self.cirSpConfCB.addItem("")
        self.cirSpConfCB.addItem("")
        self.cirSpConfCB.addItem("")
        self.cirSpConfCB.addItem("")
        self.gridLayout_4.addWidget(self.cirSpConfCB, 0, 2, 1, 3)
        self.spectrumSW.addWidget(self.cirSpPage)
        self.elSpPage = QtWidgets.QWidget()
        self.elSpPage.setObjectName("elSpPage")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.elSpPage)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.elSpRbSB = QtWidgets.QSpinBox(self.elSpPage)
        self.elSpRbSB.setMaximum(10000)
        self.elSpRbSB.setObjectName("elSpRbSB")
        self.gridLayout_5.addWidget(self.elSpRbSB, 2, 1, 1, 1)
        self.elSpRaLbl = QtWidgets.QLabel(self.elSpPage)
        self.elSpRaLbl.setObjectName("elSpRaLbl")
        self.gridLayout_5.addWidget(self.elSpRaLbl, 1, 0, 1, 1)
        self.elSpNumSB = QtWidgets.QSpinBox(self.elSpPage)
        self.elSpNumSB.setMinimum(1)
        self.elSpNumSB.setMaximum(10000)
        self.elSpNumSB.setObjectName("elSpNumSB")
        self.gridLayout_5.addWidget(self.elSpNumSB, 2, 4, 1, 1)
        self.elSpConfLbl = QtWidgets.QLabel(self.elSpPage)
        self.elSpConfLbl.setObjectName("elSpConfLbl")
        self.gridLayout_5.addWidget(self.elSpConfLbl, 0, 0, 1, 2)
        self.elSpStepLbl = QtWidgets.QLabel(self.elSpPage)
        self.elSpStepLbl.setObjectName("elSpStepLbl")
        self.gridLayout_5.addWidget(self.elSpStepLbl, 1, 2, 1, 1)
        self.elSpRaSB = QtWidgets.QSpinBox(self.elSpPage)
        self.elSpRaSB.setMaximum(10000)
        self.elSpRaSB.setObjectName("elSpRaSB")
        self.gridLayout_5.addWidget(self.elSpRaSB, 1, 1, 1, 1)
        self.elSpRbLbl = QtWidgets.QLabel(self.elSpPage)
        self.elSpRbLbl.setObjectName("elSpRbLbl")
        self.gridLayout_5.addWidget(self.elSpRbLbl, 2, 0, 1, 1)
        self.elSpStepSB = QtWidgets.QSpinBox(self.elSpPage)
        self.elSpStepSB.setMinimum(1)
        self.elSpStepSB.setMaximum(10000)
        self.elSpStepSB.setObjectName("elSpStepSB")
        self.gridLayout_5.addWidget(self.elSpStepSB, 1, 4, 1, 1)
        self.elSpConfCB = QtWidgets.QComboBox(self.elSpPage)
        self.elSpConfCB.setObjectName("elSpConfCB")
        self.elSpConfCB.addItem("")
        self.elSpConfCB.addItem("")
        self.gridLayout_5.addWidget(self.elSpConfCB, 0, 2, 1, 3)
        self.elSpNumLbl = QtWidgets.QLabel(self.elSpPage)
        self.elSpNumLbl.setObjectName("elSpNumLbl")
        self.gridLayout_5.addWidget(self.elSpNumLbl, 2, 2, 1, 2)
        self.elSpBtn = QtWidgets.QPushButton(self.elSpPage)
        self.elSpBtn.setObjectName("elSpBtn")
        self.gridLayout_5.addWidget(self.elSpBtn, 3, 0, 1, 5)
        self.spectrumSW.addWidget(self.elSpPage)
        self.horizontalLayout_4.addWidget(self.spectrumSW)
        self.verticalLayout.addWidget(self.spectrumGB)
        self.generalLayout = QtWidgets.QHBoxLayout()
        self.generalLayout.setObjectName("generalLayout")
        self.timeBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.timeBtn.setObjectName("timeBtn")
        self.generalLayout.addWidget(self.timeBtn)
        self.clearBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clearBtn.setObjectName("clearBtn")
        self.generalLayout.addWidget(self.clearBtn)
        self.verticalLayout.addLayout(self.generalLayout)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(460, 10, 981, 811))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.figureSW.setCurrentIndex(0)
        self.spectrumSW.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Maslova Lab04"))
        self.colorGB.setTitle(_translate("MainWindow", "Цвет"))
        self.colorCB.setItemText(0, _translate("MainWindow", "Черный"))
        self.colorCB.setItemText(1, _translate("MainWindow", "Белый (фон)"))
        self.colorCB.setItemText(2, _translate("MainWindow", "Синий"))
        self.colorCB.setItemText(3, _translate("MainWindow", "Красный"))
        self.algoGB.setTitle(_translate("MainWindow", "Алгоритм"))
        self.algoCB.setItemText(0, _translate("MainWindow", "Каноническое уравнение"))
        self.algoCB.setItemText(1, _translate("MainWindow", "Параметрическое уравнение"))
        self.algoCB.setItemText(2, _translate("MainWindow", "Алгоритм Брезенхема"))
        self.algoCB.setItemText(3, _translate("MainWindow", "Алгоритм средней точки"))
        self.algoCB.setItemText(4, _translate("MainWindow", "Библиотечная функция"))
        self.figureGB.setTitle(_translate("MainWindow", "Фигура"))
        self.figureCB.setItemText(0, _translate("MainWindow", "Окружность"))
        self.figureCB.setItemText(1, _translate("MainWindow", "Эллипс"))
        self.figureSetGB.setTitle(_translate("MainWindow", "Одиночная фигура"))
        self.cirXcLbl.setText(_translate("MainWindow", "Xc:"))
        self.cirCentreBtn.setText(_translate("MainWindow", "Центр\n"
"холста"))
        self.cirYcLbl.setText(_translate("MainWindow", "Yc:"))
        self.cirRLbl.setText(_translate("MainWindow", "R:"))
        self.cirBtn.setText(_translate("MainWindow", "Построить"))
        self.elXcLbl.setText(_translate("MainWindow", "Xc:"))
        self.elYcLbl.setText(_translate("MainWindow", "Yc:"))
        self.elCentreBtn.setText(_translate("MainWindow", "Центр холста"))
        self.elRaLbl.setText(_translate("MainWindow", "Ra:"))
        self.elRbLbl.setText(_translate("MainWindow", "Rb:"))
        self.elBtn.setText(_translate("MainWindow", "Построить"))
        self.spectrumGB.setTitle(_translate("MainWindow", "Спектр"))
        self.cirSpNumLbl.setText(_translate("MainWindow", "Количество"))
        self.cirSpRbLbl.setText(_translate("MainWindow", "Rнач"))
        self.cirSpStepLbl.setText(_translate("MainWindow", "Шаг"))
        self.cirSpReLbl.setText(_translate("MainWindow", "Rкон"))
        self.cirSpBtn.setText(_translate("MainWindow", "Построить"))
        self.cirSpConfLbl.setText(_translate("MainWindow", "Параметры"))
        self.cirSpConfCB.setItemText(0, _translate("MainWindow", "Без Rнач"))
        self.cirSpConfCB.setItemText(1, _translate("MainWindow", "Без Rкон"))
        self.cirSpConfCB.setItemText(2, _translate("MainWindow", "Без шага"))
        self.cirSpConfCB.setItemText(3, _translate("MainWindow", "Без количества"))
        self.elSpRaLbl.setText(_translate("MainWindow", "Ra нач"))
        self.elSpConfLbl.setText(_translate("MainWindow", "Параметры"))
        self.elSpStepLbl.setText(_translate("MainWindow", "Шаг"))
        self.elSpRbLbl.setText(_translate("MainWindow", "Rb нач"))
        self.elSpConfCB.setItemText(0, _translate("MainWindow", "Шаг по Ra"))
        self.elSpConfCB.setItemText(1, _translate("MainWindow", "Шаг по Rb"))
        self.elSpNumLbl.setText(_translate("MainWindow", "Количество"))
        self.elSpBtn.setText(_translate("MainWindow", "Построить"))
        self.timeBtn.setText(_translate("MainWindow", "Сравнить время"))
        self.clearBtn.setText(_translate("MainWindow", "Очистить холст"))