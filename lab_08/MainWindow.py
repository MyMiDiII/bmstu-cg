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
        self.segmentsTable = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.segmentsTable.sizePolicy().hasHeightForWidth())
        self.segmentsTable.setSizePolicy(sizePolicy)
        self.segmentsTable.setMinimumSize(QtCore.QSize(301, 141))
        self.segmentsTable.setMaximumSize(QtCore.QSize(301, 141))
        self.segmentsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.segmentsTable.setObjectName("segmentsTable")
        self.segmentsTable.setColumnCount(2)
        self.segmentsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.segmentsTable.setHorizontalHeaderItem(1, item)
        self.segmentsTable.verticalHeader().setDefaultSectionSize(41)
        self.segmentsTable.verticalHeader().setMinimumSectionSize(21)
        self.gridLayout.addWidget(self.segmentsTable, 0, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 1, 8, 1)
        self.segmentsLayout = QtWidgets.QVBoxLayout()
        self.segmentsLayout.setObjectName("segmentsLayout")
        self.segmentLayout = QtWidgets.QGridLayout()
        self.segmentLayout.setObjectName("segmentLayout")
        self.x1SB = QtWidgets.QSpinBox(self.centralwidget)
        self.x1SB.setMaximum(1164)
        self.x1SB.setObjectName("x1SB")
        self.segmentLayout.addWidget(self.x1SB, 0, 1, 1, 1)
        self.x2SB = QtWidgets.QSpinBox(self.centralwidget)
        self.x2SB.setMaximum(1164)
        self.x2SB.setObjectName("x2SB")
        self.segmentLayout.addWidget(self.x2SB, 1, 1, 1, 1)
        self.y2SB = QtWidgets.QSpinBox(self.centralwidget)
        self.y2SB.setMaximum(874)
        self.y2SB.setObjectName("y2SB")
        self.segmentLayout.addWidget(self.y2SB, 1, 3, 1, 1)
        self.y1SB = QtWidgets.QSpinBox(self.centralwidget)
        self.y1SB.setMaximum(874)
        self.y1SB.setObjectName("y1SB")
        self.segmentLayout.addWidget(self.y1SB, 0, 3, 1, 1)
        self.y2Lbl = QtWidgets.QLabel(self.centralwidget)
        self.y2Lbl.setObjectName("y2Lbl")
        self.segmentLayout.addWidget(self.y2Lbl, 1, 2, 1, 1)
        self.x1Lbl = QtWidgets.QLabel(self.centralwidget)
        self.x1Lbl.setObjectName("x1Lbl")
        self.segmentLayout.addWidget(self.x1Lbl, 0, 0, 1, 1)
        self.y1Lbl = QtWidgets.QLabel(self.centralwidget)
        self.y1Lbl.setObjectName("y1Lbl")
        self.segmentLayout.addWidget(self.y1Lbl, 0, 2, 1, 1)
        self.x2Lbl = QtWidgets.QLabel(self.centralwidget)
        self.x2Lbl.setObjectName("x2Lbl")
        self.segmentLayout.addWidget(self.x2Lbl, 1, 0, 1, 1)
        self.segmentsLayout.addLayout(self.segmentLayout)
        self.addSegmentBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addSegmentBtn.sizePolicy().hasHeightForWidth())
        self.addSegmentBtn.setSizePolicy(sizePolicy)
        self.addSegmentBtn.setObjectName("addSegmentBtn")
        self.segmentsLayout.addWidget(self.addSegmentBtn)
        self.gridLayout.addLayout(self.segmentsLayout, 1, 0, 1, 1)
        self.selectorTable = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectorTable.sizePolicy().hasHeightForWidth())
        self.selectorTable.setSizePolicy(sizePolicy)
        self.selectorTable.setMinimumSize(QtCore.QSize(301, 141))
        self.selectorTable.setMaximumSize(QtCore.QSize(301, 141))
        self.selectorTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.selectorTable.setObjectName("selectorTable")
        self.selectorTable.setColumnCount(2)
        self.selectorTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.selectorTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.selectorTable.setHorizontalHeaderItem(1, item)
        self.selectorTable.verticalHeader().setDefaultSectionSize(41)
        self.selectorTable.verticalHeader().setMinimumSectionSize(21)
        self.gridLayout.addWidget(self.selectorTable, 2, 0, 1, 1)
        self.selectersLayout = QtWidgets.QVBoxLayout()
        self.selectersLayout.setObjectName("selectersLayout")
        self.selecterLayout = QtWidgets.QGridLayout()
        self.selecterLayout.setObjectName("selecterLayout")
        self.xSelSB = QtWidgets.QSpinBox(self.centralwidget)
        self.xSelSB.setMaximum(1164)
        self.xSelSB.setObjectName("xSelSB")
        self.selecterLayout.addWidget(self.xSelSB, 0, 1, 1, 1)
        self.xSelLbl = QtWidgets.QLabel(self.centralwidget)
        self.xSelLbl.setObjectName("xSelLbl")
        self.selecterLayout.addWidget(self.xSelLbl, 0, 0, 1, 1)
        self.ySelSB = QtWidgets.QSpinBox(self.centralwidget)
        self.ySelSB.setMaximum(874)
        self.ySelSB.setObjectName("ySelSB")
        self.selecterLayout.addWidget(self.ySelSB, 0, 3, 1, 1)
        self.ySelLbl = QtWidgets.QLabel(self.centralwidget)
        self.ySelLbl.setObjectName("ySelLbl")
        self.selecterLayout.addWidget(self.ySelLbl, 0, 2, 1, 1)
        self.selectersLayout.addLayout(self.selecterLayout)
        self.addVertexBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addVertexBtn.setObjectName("addVertexBtn")
        self.selectersLayout.addWidget(self.addVertexBtn)
        self.setSelectorBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setSelectorBtn.sizePolicy().hasHeightForWidth())
        self.setSelectorBtn.setSizePolicy(sizePolicy)
        self.setSelectorBtn.setObjectName("setSelectorBtn")
        self.selectersLayout.addWidget(self.setSelectorBtn)
        self.gridLayout.addLayout(self.selectersLayout, 3, 0, 1, 1)
        self.colorLayout = QtWidgets.QGridLayout()
        self.colorLayout.setObjectName("colorLayout")
        self.segmentsColorLbl = QtWidgets.QLabel(self.centralwidget)
        self.segmentsColorLbl.setObjectName("segmentsColorLbl")
        self.colorLayout.addWidget(self.segmentsColorLbl, 1, 0, 1, 1)
        self.selectorColorLbl = QtWidgets.QLabel(self.centralwidget)
        self.selectorColorLbl.setObjectName("selectorColorLbl")
        self.colorLayout.addWidget(self.selectorColorLbl, 0, 0, 1, 1)
        self.segmentsColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.segmentsColorBtn.setEnabled(True)
        self.segmentsColorBtn.setMinimumSize(QtCore.QSize(62, 33))
        self.segmentsColorBtn.setMaximumSize(QtCore.QSize(62, 33))
        self.segmentsColorBtn.setAutoFillBackground(False)
        self.segmentsColorBtn.setStyleSheet("background-color: rgb(65, 255, 0);")
        self.segmentsColorBtn.setText("")
        self.segmentsColorBtn.setAutoExclusive(False)
        self.segmentsColorBtn.setAutoDefault(False)
        self.segmentsColorBtn.setDefault(True)
        self.segmentsColorBtn.setFlat(False)
        self.segmentsColorBtn.setObjectName("segmentsColorBtn")
        self.colorLayout.addWidget(self.segmentsColorBtn, 1, 1, 1, 1)
        self.selectorColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectorColorBtn.setEnabled(True)
        self.selectorColorBtn.setMinimumSize(QtCore.QSize(62, 33))
        self.selectorColorBtn.setMaximumSize(QtCore.QSize(62, 33))
        self.selectorColorBtn.setAutoFillBackground(False)
        self.selectorColorBtn.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.selectorColorBtn.setText("")
        self.selectorColorBtn.setAutoExclusive(False)
        self.selectorColorBtn.setAutoDefault(False)
        self.selectorColorBtn.setDefault(True)
        self.selectorColorBtn.setFlat(False)
        self.selectorColorBtn.setObjectName("selectorColorBtn")
        self.colorLayout.addWidget(self.selectorColorBtn, 0, 1, 1, 1)
        self.resultColorLbl = QtWidgets.QLabel(self.centralwidget)
        self.resultColorLbl.setObjectName("resultColorLbl")
        self.colorLayout.addWidget(self.resultColorLbl, 2, 0, 1, 1)
        self.resultColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resultColorBtn.setEnabled(True)
        self.resultColorBtn.setMinimumSize(QtCore.QSize(62, 33))
        self.resultColorBtn.setMaximumSize(QtCore.QSize(62, 33))
        self.resultColorBtn.setAutoFillBackground(False)
        self.resultColorBtn.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.resultColorBtn.setText("")
        self.resultColorBtn.setAutoExclusive(False)
        self.resultColorBtn.setAutoDefault(False)
        self.resultColorBtn.setDefault(True)
        self.resultColorBtn.setFlat(False)
        self.resultColorBtn.setObjectName("resultColorBtn")
        self.colorLayout.addWidget(self.resultColorBtn, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.colorLayout, 4, 0, 1, 1)
        self.selectBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectBtn.sizePolicy().hasHeightForWidth())
        self.selectBtn.setSizePolicy(sizePolicy)
        self.selectBtn.setObjectName("selectBtn")
        self.gridLayout.addWidget(self.selectBtn, 5, 0, 1, 1)
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearBtn.sizePolicy().hasHeightForWidth())
        self.clearBtn.setSizePolicy(sizePolicy)
        self.clearBtn.setObjectName("clearBtn")
        self.gridLayout.addWidget(self.clearBtn, 6, 0, 1, 1)
        self.roolsBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roolsBtn.sizePolicy().hasHeightForWidth())
        self.roolsBtn.setSizePolicy(sizePolicy)
        self.roolsBtn.setObjectName("roolsBtn")
        self.gridLayout.addWidget(self.roolsBtn, 7, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Maslova Lab08"))
        item = self.segmentsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "(X1, Y1)"))
        item = self.segmentsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "(X2, Y2)"))
        self.y2Lbl.setText(_translate("MainWindow", "Y2:"))
        self.x1Lbl.setText(_translate("MainWindow", "X1:"))
        self.y1Lbl.setText(_translate("MainWindow", "Y1:"))
        self.x2Lbl.setText(_translate("MainWindow", "X2:"))
        self.addSegmentBtn.setText(_translate("MainWindow", "Добавить\n"
"отрезок"))
        item = self.selectorTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X"))
        item = self.selectorTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y"))
        self.xSelLbl.setText(_translate("MainWindow", "X:"))
        self.ySelLbl.setText(_translate("MainWindow", "Y:"))
        self.addVertexBtn.setText(_translate("MainWindow", "Добавить вершину"))
        self.setSelectorBtn.setText(_translate("MainWindow", "Замкнуть\n"
"отсекатель"))
        self.segmentsColorLbl.setText(_translate("MainWindow", "Цвет отрезков:"))
        self.selectorColorLbl.setText(_translate("MainWindow", "Цвет отсекателя:"))
        self.resultColorLbl.setText(_translate("MainWindow", "Цвет результата:"))
        self.selectBtn.setText(_translate("MainWindow", "Отсечь"))
        self.clearBtn.setText(_translate("MainWindow", "Очистить"))
        self.roolsBtn.setText(_translate("MainWindow", "Правила ввода"))