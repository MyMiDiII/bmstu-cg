"""
    Модуль заполнения сплошных областей
    c затравкой
"""
from geometry import Point
from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QCoreApplication, QEventLoop

BORDER_COLOR = QColor("black").name()

class Filler:

    def __init__(self, scene, img, color):
        self.scene = scene
        self.img = img
        self.color = color

    # ? delete names
    def isBorder(self, x, y):
        return QColor(self.img.pixel(x, y)).name() == BORDER_COLOR

    # ! change name
    def isNew(self, x, y):
        return QColor(self.img.pixel(x, y)).name() == self.color.name()

    def getNewSeeds(self, stack, left, right, y):
        tmpX = left

        while tmpX <= right:
            flag = 0

            while (not self.isBorder(tmpX, y)
                    and not self.isNew(tmpX, y)
                    and tmpX <= right):
                flag = 1
                tmpX += 1

            if flag:
                if (tmpX <= right
                    and not self.isBorder(tmpX, y)
                    and not self.isNew(tmpX, y)):
                    stack.append(Point(tmpX, y))
                else:
                    stack.append(Point(tmpX - 1, y))
                flag = 0

            beginX = tmpX
            while ((self.isBorder(tmpX, y)
                    or self.isNew(tmpX, y))
                    and tmpX <= right):
                tmpX += 1

            if tmpX == beginX:
                tmpX += 1

        return tmpX

    def run(self, painter, seed, delay=0):
        stack = []

        stack.append(seed)

        while stack:
            curPixel = stack.pop()

            painter.drawPoint(curPixel.x, curPixel.y)

            tmpX = curPixel.x + 1

            while not self.isBorder(tmpX, curPixel.y) and tmpX < 1177:
                print("here1")
                painter.drawPoint(tmpX, curPixel.y)
                tmpX += 1

            rightX = tmpX - 1

            sleepTime = QTime.currentTime().addMSecs(delay)
            while (QTime.currentTime() < sleepTime):
                QCoreApplication.processEvents(QEventLoop.AllEvents, delay)

            self.scene.clear()
            self.scene.addPixmap(QPixmap.fromImage(self.img))

            tmpX = curPixel.x - 1

            while not self.isBorder(tmpX, curPixel.y) and tmpX > -1:
                print("here2")
                painter.drawPoint(tmpX, curPixel.y)
                tmpX -= 1

            leftX = tmpX + 1

            sleepTime = QTime.currentTime().addMSecs(delay)
            while (QTime.currentTime() < sleepTime):
                QCoreApplication.processEvents(QEventLoop.AllEvents, delay)

            self.scene.clear()
            self.scene.addPixmap(QPixmap.fromImage(self.img))

            # ! add max-min check
            # ? нужен ли tmpX

            if curPixel.y < 873:
                tmpX = self.getNewSeeds(stack, leftX, rightX, curPixel.y + 1)

            if curPixel.y > 0:
                tmpX = self.getNewSeeds(stack, leftX, rightX, curPixel.y - 1)
