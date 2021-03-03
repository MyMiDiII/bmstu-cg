"""
    Модуль для работы с изображением рыбы
"""

import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Fish:
    def __init__(self, *args, **kwargs):
        self.body = self.create_body(30, 20)

    def create_body(self, large_sa, small_sa):
        """
            Создание тела(эллипса) рыбы
        """
        x_list = np.arange(-large_sa, large_sa, 0.1)
        y_list = [x + 2 for x in x_list]

        return (x_list, y_list)


