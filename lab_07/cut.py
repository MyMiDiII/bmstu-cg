"""
    Модуль заполнения c затравкой
"""
from geometry import Point
from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5.QtCore import QCoreApplication, QEventLoop

BORDER_COLOR = QColor("black").name()

class Cutter:

    def __init__(self, scene, img, color):
        self.scene = scene
        self.img = img
        self.color = color

    def run(self, painter, seed, delay=0):
        pass