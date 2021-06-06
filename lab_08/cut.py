from main import callError
from geometry import Point, Segment
from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5.QtCore import QCoreApplication, QEventLoop

class Cutter:

    def __init__(self, scene, painter, img, color):
        self.scene = scene
        self.painter = painter
        self.img = img
        self.color = color

    def cutSegment(self, seg, selector):
        print("отрезок обрезан")

    def run(self, segments, selector):
        if not selector.isConvex:
            callError(
                "Невыпуклый отсекатель!",
                "Отсекатель не является выпуклым!"
            )

        for seg in segments:
            self.cutSegment(seg, selector)
