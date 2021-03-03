"""
    Модуль для работы с изображением рыбы
"""

import numpy as np
from math import sin, cos

class Func:
    def __init__(self, x_list, y_list):
        self.x_list = x_list
        self.y_list = y_list


class Fish:
    def __init__(self, *args, **kwargs):
        self.body = self.create_body(20, 10)
        self.scaling(2, 1, 0, 0)

    def create_body(self, large_sa, small_sa):
        """
            Создание тела(эллипса) рыбы
        """
        body = Func([], [])
        angles = np.linspace(0, 360, 360)

        for angle in angles:
            body.x_list.append(large_sa * cos(np.radians(angle)))
            body.y_list.append(small_sa * sin(np.radians(angle)))

        return body

    def transfer(self, dx, dy):
        """
            Перенос изображения рыбы
        """
        self.body.x_list = [x + dx for x in self.body.x_list]
        self.body.y_list = [y + dy for y in self.body.y_list]


    def scaling(self, kx, ky, xc, yc):
        """
            Масштабирвание изображения
        """
        self.body.x_list = [x * kx + (1 - kx) * xc for x in self.body.x_list]
        self.body.y_list = [y * ky + (1 - ky) * yc for y in self.body.y_list]


