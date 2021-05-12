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
        MainWindow.resize(1500, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pointsTable = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pointsTable.sizePolicy().hasHeightForWidth())
        self.pointsTable.setSizePolicy(sizePolicy)
        self.pointsTable.setMinimumSize(QtCore.QSize(281, 351))
        self.pointsTable.setMaximumSize(QtCore.QSize(281, 351))
        self.pointsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pointsTable.setObjectName("pointsTable")
        self.pointsTable.setColumnCount(2)
        self.pointsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.pointsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pointsTable.setHorizontalHeaderItem(1, item)
        self.pointsTable.verticalHeader().setDefaultSectionSize(41)
        self.pointsTable.verticalHeader().setMinimumSectionSize(21)
        self.gridLayout.addWidget(self.pointsTable, 0, 0, 1, 5)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 5, 11, 1)
        self.xLbl = QtWidgets.QLabel(self.centralwidget)
        self.xLbl.setObjectName("xLbl")
        self.gridLayout.addWidget(self.xLbl, 1, 0, 1, 1)
        self.xSB = QtWidgets.QSpinBox(self.centralwidget)
        self.xSB.setMaximum(1184)
        self.xSB.setObjectName("xSB")
        self.gridLayout.addWidget(self.xSB, 1, 1, 1, 1)
        self.addPointBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addPointBtn.sizePolicy().hasHeightForWidth())
        self.addPointBtn.setSizePolicy(sizePolicy)
        self.addPointBtn.setMinimumSize(QtCore.QSize(141, 91))
        self.addPointBtn.setMaximumSize(QtCore.QSize(141, 91))
        self.addPointBtn.setObjectName("addPointBtn")
        self.gridLayout.addWidget(self.addPointBtn, 1, 2, 2, 3)
        self.yLbl = QtWidgets.QLabel(self.centralwidget)
        self.yLbl.setObjectName("yLbl")
        self.gridLayout.addWidget(self.yLbl, 2, 0, 1, 1)
        self.ySB = QtWidgets.QSpinBox(self.centralwidget)
        self.ySB.setMaximum(873)
        self.ySB.setObjectName("ySB")
        self.gridLayout.addWidget(self.ySB, 2, 1, 1, 1)
        self.deletePointBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deletePointBtn.sizePolicy().hasHeightForWidth())
        self.deletePointBtn.setSizePolicy(sizePolicy)
        self.deletePointBtn.setObjectName("deletePointBtn")
        self.gridLayout.addWidget(self.deletePointBtn, 3, 0, 1, 5)
        self.closeFigBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeFigBtn.sizePolicy().hasHeightForWidth())
        self.closeFigBtn.setSizePolicy(sizePolicy)
        self.closeFigBtn.setObjectName("closeFigBtn")
        self.gridLayout.addWidget(self.closeFigBtn, 4, 0, 1, 5)
        self.colorLbl = QtWidgets.QLabel(self.centralwidget)
        self.colorLbl.setObjectName("colorLbl")
        self.gridLayout.addWidget(self.colorLbl, 5, 0, 1, 3)
        self.colorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.colorBtn.setEnabled(True)
        self.colorBtn.setAutoFillBackground(False)
        self.colorBtn.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.colorBtn.setText("")
        self.colorBtn.setAutoExclusive(False)
        self.colorBtn.setAutoDefault(False)
        self.colorBtn.setDefault(True)
        self.colorBtn.setFlat(False)
        self.colorBtn.setObjectName("colorBtn")
        self.gridLayout.addWidget(self.colorBtn, 5, 3, 1, 2)
        self.delayLbl = QtWidgets.QLabel(self.centralwidget)
        self.delayLbl.setObjectName("delayLbl")
        self.gridLayout.addWidget(self.delayLbl, 6, 0, 1, 2)
        self.delaySB = QtWidgets.QSpinBox(self.centralwidget)
        self.delaySB.setMaximum(50)
        self.delaySB.setObjectName("delaySB")
        self.gridLayout.addWidget(self.delaySB, 6, 2, 1, 2)
        self.msLbl = QtWidgets.QLabel(self.centralwidget)
        self.msLbl.setObjectName("msLbl")
        self.gridLayout.addWidget(self.msLbl, 6, 4, 1, 1)
        self.paintBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paintBtn.sizePolicy().hasHeightForWidth())
        self.paintBtn.setSizePolicy(sizePolicy)
        self.paintBtn.setObjectName("paintBtn")
        self.gridLayout.addWidget(self.paintBtn, 7, 0, 1, 5)
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearBtn.sizePolicy().hasHeightForWidth())
        self.clearBtn.setSizePolicy(sizePolicy)
        self.clearBtn.setObjectName("clearBtn")
        self.gridLayout.addWidget(self.clearBtn, 8, 0, 1, 5)
        self.roolsBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roolsBtn.sizePolicy().hasHeightForWidth())
        self.roolsBtn.setSizePolicy(sizePolicy)
        self.roolsBtn.setObjectName("roolsBtn")
        self.gridLayout.addWidget(self.roolsBtn, 10, 0, 1, 5)
        self.timeLbl = QtWidgets.QLabel(self.centralwidget)
        self.timeLbl.setObjectName("timeLbl")
        self.gridLayout.addWidget(self.timeLbl, 9, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.pointsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X"))
        item = self.pointsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y"))
        self.xLbl.setText(_translate("MainWindow", "X:"))
        self.addPointBtn.setText(_translate("MainWindow", "Добавить\n"
"вершину"))
        self.yLbl.setText(_translate("MainWindow", "Y:"))
        self.deletePointBtn.setText(_translate("MainWindow", "Удалить последнюю\n"
"вершину"))
        self.closeFigBtn.setText(_translate("MainWindow", "Замкнуть фигуру"))
        self.colorLbl.setText(_translate("MainWindow", "Цвет заполнения:"))
        self.delayLbl.setText(_translate("MainWindow", "Задержка:"))
        self.msLbl.setText(_translate("MainWindow", "мс"))
        self.paintBtn.setText(_translate("MainWindow", "Закрасить"))
        self.clearBtn.setText(_translate("MainWindow", "Очистить"))
        self.roolsBtn.setText(_translate("MainWindow", "Правила ввода"))
        self.timeLbl.setText(_translate("MainWindow", "Время заполнения:"))
