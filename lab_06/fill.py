"""
    Модуль заполнения сплошных областей
    c затравкой
"""
from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QCoreApplication, QEventLoop


class Filler:

    def __init__(self, scene, img, color):
        self.scene = scene
        self.img = img
        self.color = color

    def run(self, delay=0):
        print("Тут будет твориться магия!!!")
        pass
