from geometry import Point, Segment
from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5.QtCore import QCoreApplication, QEventLoop

class Cutter:

    def __init__(self, scene, painter, img, color):
        self.scene = scene
        self.painter = painter
        self.img = img
        self.color = color

    def getPointCode(self, point, selector):
        code = 0b0000

        code = code | 0b0001 if point.x < selector[0] else code
        code = code | 0b0010 if point.x > selector[1] else code
        code = code | 0b0100 if point.y < selector[2] else code
        code = code | 0b1000 if point.y > selector[3] else code

        return code

    def findVertInt(self, curPoint, selector):
        if curPoint.y < selector[2]:
            return Point(curPoint.x, selector[2])

        if curPoint.y > selector[3]:
            return Point(curPoint.x, selector[3])

        return curPoint

    def cutSegment(self, seg, selector):
        code1 = self.getPointCode(seg.begin, selector)
        code2 = self.getPointCode(seg.end, selector)

        if not code1 and not code2:
            self.painter.drawLine(
                seg.begin.x,
                seg.begin.y,
                seg.end.x,
                seg.end.y
            )
            return

        if code1 & code2:
            return

        resSeg = [None, None]

        begin = 0
        if not code1:
            begin = 1
            resSeg[0] = seg.begin
        elif not code2:
            begin = 1
            code1, code2 = code2, code1
            seg.begin, seg.end = seg.end, seg.begin
            resSeg[0] = seg.begin

        for i in range(begin, 2):
            curPoint = seg.end if i else seg.begin
            curCode = code2 if i else code1
            if seg.begin.x == seg.end.x:
                resSeg[i] = self.findVertInt(
                    curPoint,
                    selector
                )
                continue

            m = (seg.end.y - seg.begin.y) / (seg.end.x - seg.begin.x)

            if curCode & 0b0001:
                y = round(m * (selector[0] - curPoint.x) + curPoint.y)

                if y >= selector[2] and y <= selector[3]:
                    resSeg[i] = Point(selector[0], y)
                    continue

            if curCode & 0b0010:
                y = round(m * (selector[1] - curPoint.x) + curPoint.y)

                if y >= selector[2] and y <= selector[3]:
                    resSeg[i] = Point(selector[1], y)
                    continue

            if not (seg.end.y - seg.begin.y):
                continue

            if curCode & 0b0100:
                x = round((selector[2] - curPoint.y) / m + curPoint.x)

                if x >= selector[0] and x <= selector[1]:
                    resSeg[i] = Point(x, selector[2])
                    continue

            if curCode & 0b1000:
                x = round((selector[3] - curPoint.y) / m + curPoint.x)

                if x >= selector[0] and x <= selector[1]:
                    resSeg[i] = Point(x, selector[3])
                    continue


        if resSeg[0] and resSeg[1]:
            self.painter.drawLine(
                resSeg[0].x,
                resSeg[0].y,
                resSeg[1].x,
                resSeg[1].y
            )


    def run(self, segments, selector):
        for seg in segments:
            self.cutSegment(seg, selector)
