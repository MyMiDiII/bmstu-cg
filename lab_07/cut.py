"""
    Модуль заполнения c затравкой
"""
from geometry import Point
from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5.QtCore import QCoreApplication, QEventLoop

BORDER_COLOR = QColor("black").name()

class Cutter:

    def __init__(self, scene, painter, img, color):
        self.scene = scene
        self.painter = painter
        self.img = img
        self.color = color

    def run(self, segments, selecter):
        print(segments)
        print(selecter)
        pass