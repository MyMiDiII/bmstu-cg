import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView, QGraphicsScene
from PyQt5.QtWidgets import QColorDialog, QGraphicsColorizeEffect
from PyQt5.QtGui import QPen, QColor, QPalette

from MainWindow import Ui_MainWindow


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
        
        self.colorBtn.clicked.connect(self.chooseColor)

    def chooseColor(self):
        """
            Выбор цвета
        """
        color = QColorDialog.getColor()
        self.colorBtn.setStyleSheet("background-color: " + color.name() + ";")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.move(250, 100)
    main.setFixedSize(1500, 900)
    main.show()
    sys.exit(app.exec_())
