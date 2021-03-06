"""
    Модуль для обновления изображения
"""

import tkinter as tk
import tkinter.messagebox as box
import copy

class History:
    def __init__(self, index, buf):
        self.index = index
        self.buf = buf

    
    def add(self, func):
        self.index += 1
        self.buf = self.buf[:self.index] + [func]


    def back(self):
        self.index -= 1


    def forward(self):
        self.index += 1


def move(window, fish, fishes):
    """
        Запуск переноса
    """
    try:
        dx = float(window.ent_dx.get())
        dy = float(window.ent_dy.get())
    except ValueError:
        box.showerror("ЧИСЛААААА", "Ну там чиселки должны быть ;)")
    else:
        fish.move(dx, dy)
        fishes.add(copy.deepcopy(fish))
        window.funcs = fish.full
        window.create_matplotlib()
        window.lbl_figure_centre.configure(
                font=('DejaVu Sans Mono', 12),
                text="X:{:7.2f}; Y:{:7.2f}".format(window.funcs[7].x_list[0],
                                                     window.funcs[7].y_list[0])
                )


def scale(window, fish, fishes):
    """
        Запуск масштабирования
    """
    try:
        kx = float(window.Entry1_1.get())
        ky = float(window.Entry2_1.get())
        xc = float(window.Entry3.get())
        yc = float(window.Entry3_1.get())

    except ValueError:
        box.showerror("ЧИСЛААААА", "Ну там чиселки должны быть ;)")

    else:
        fish.scaling(kx, ky, xc, yc)
        fishes.add(copy.deepcopy(fish))
        window.funcs = fish.full
        window.create_matplotlib()
        window.lbl_figure_centre.configure(
                font=('DejaVu Sans Mono', 12),
                text="X:{:7.2f}; Y:{:7.2f}".format(window.funcs[7].x_list[0],
                                                     window.funcs[7].y_list[0])
                )


def turn(window, fish, fishes):
    """
        Запуск масштабирования
    """
    try:
        phi = float(window.Entry1_1_1.get())
        xc = float(window.Entry3.get())
        yc = float(window.Entry3_1.get())
        
    except ValueError:
        box.showerror("ЧИСЛААААА", "Ну там чиселки должны быть ;)")

    else:
        fish.rotate(phi, xc, yc)
        fishes.add(copy.deepcopy(fish))
        window.funcs = fish.full
        window.create_matplotlib()
        window.lbl_figure_centre.configure(
                font=('DejaVu Sans Mono', 12),
                text="X:{:7.2f}; Y:{:7.2f}".format(window.funcs[7].x_list[0],
                                                     window.funcs[7].y_list[0])
                )


def reset(window, fish, fishes):
    """
        Возвращение к исходному изображению
        с сохранением предыдущего состояния
    """
    fish.reset()
    window.funcs = fish.full
    window.create_matplotlib()
    fishes.add(copy.deepcopy(fish))
    window.Button2.configure(state=tk.NORMAL)
    window.Button2_1.configure(state=tk.DISABLED)
    window.lbl_figure_centre.configure(
            font=('DejaVu Sans Mono', 12),
            text="X:{:7.2f}; Y:{:7.2f}".format(window.funcs[7].x_list[0],
                                                 window.funcs[7].y_list[0])
            )


def undo(window, fish, fishes):
    """
        Возвращение к предыдущему состоянию изображения
    """
    print(fishes.index, fishes.buf)
    if fishes.index:
        fishes.back()
        fish = fishes.buf[fishes.index]
        window.funcs = fish.full
        window.create_matplotlib()
        window.Button2_1.configure(state=tk.NORMAL)
        window.lbl_figure_centre.configure(
                font=('DejaVu Sans Mono', 12),
                text="X:{:7.2f}; Y:{:7.2f}".format(window.funcs[7].x_list[0],
                                                     window.funcs[7].y_list[0])
                )

    if not fishes.index:
        window.Button2.configure(state=tk.DISABLED)
    print(fishes.index, fishes.buf)


def redo(window, fish, fishes):
    """
        Возвращение к предыдущему состоянию изображения
    """
    print(fishes.index, fishes.buf)
    if fishes.index < len(fishes.buf):
        fishes.forward()
        fish = fishes.buf[fishes.index]
        window.funcs = fish.full
        window.create_matplotlib()
        window.Button2.configure(state=tk.NORMAL)
        window.lbl_figure_centre.configure(
                font=('DejaVu Sans Mono', 12),
                text="X:{:7.2f}; Y: {:7.2f}".format(window.funcs[7].x_list[0],
                                                     window.funcs[7].y_list[0])
                )

    if fishes.index == len(fishes.buf) - 1:
        window.Button2_1.configure(state=tk.DISABLED)
    print(fishes.index, fishes.buf)
