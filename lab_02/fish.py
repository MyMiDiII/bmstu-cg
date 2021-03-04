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
        """
            Конструктор класса
        """
        self.body = self.create_body(22, 10)
        self.head = self.create_head()
        self.eye = self.create_eye()
        self.mouth = self.create_mouth()
        self.tail = self.create_tail()
        self.top_fin = self.create_top_fin()
        self.button_fin = self.create_button_fin()
        self.full = [self.body, self.head, self.eye, self.mouth,
                     self.tail, self.top_fin, self.button_fin]

    def reset(self):
        """
            Сброс
        """
        self.__init__()


    def create_body(self, large_sa, small_sa):
        """
            Создание эллипса (тело, голова рыбы)
        """
        body = Func([], [])
        angles = np.linspace(0, 360, 360)

        for angle in angles:
            body.x_list.append(large_sa * cos(np.radians(angle)))
            body.y_list.append(small_sa * sin(np.radians(angle)))

        for i in range(len(body.x_list)):
            print(body.x_list[i], body.y_list[i])

        return body


    def create_head(self):
        """
            Создание головы
        """
        head = self.create_body(5, 5)
        head.x_list = [x - 17 for x in head.x_list]

        return head


    def create_eye(self):
        """
            Создание глаза
        """
        eye = self.create_body(1, 1)
        eye.x_list = [x - 17 for x in eye.x_list]
        eye.y_list = [y + 2.5 for y in eye.y_list]

        return eye


    def create_mouth(self):
        """
            Создание рта
        """
        mouth = Func([], [])
        mouth.x_list = [-18, -16]
        mouth.y_list = [-2.5, -2.5]

        return mouth


    def create_tail(self):
        """
            Создание хвоста
        """
        tail = Func([], [])

        tail.x_list = [17.8, 35, 28, 38, 25, 18.4]
        tail.y_list = [-6, -6, 0, 10, 10, 5.7]

        return tail


    def create_top_fin(self):
        """
            Создание верхнего плавника
        """
        return Func([-8.5, -2, 15, 8.5], [9.2, 15, 15, 9.2])


    def create_button_fin(self):
        """
            Создание нижнего плавника
        """
        return Func([-8.5, -2, 15, 8.5], [-9.2, -15, -15, -9.2])


    def move(self, dx, dy):
        """
            Перенос изображения рыбы
        """
        print(FISHES)

        for element in self.full:
            element.x_list = [x + dx for x in element.x_list]
            element.y_list = [y + dy for y in element.y_list]


    def scaling(self, kx, ky, xc, yc):
        """
            Масштабирвание изображения
        """
        for element in self.full:
            element.x_list = [x * kx + (1 - kx) * xc for x in element.x_list]
            element.y_list = [y * ky + (1 - ky) * yc for y in element.y_list]


    def rotate(self, phi, xc, yc):
        """
            Поворот изображения
        """
        phi = -phi
        for element in self.full:
            tmp_x = [x for x in element.x_list]
            element.x_list = [xc + (x - xc) * cos(np.radians(phi)) 
                              + (element.y_list[i] - yc) * sin(np.radians(phi))
                              for i, x in enumerate(element.x_list)]
            element.y_list = [yc - (tmp_x[i] - xc) * sin(np.radians(phi)) 
                              + (y - yc) * cos(np.radians(phi))
                              for i, y in enumerate(element.y_list)]


