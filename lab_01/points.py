"""
    Модуль для работы с множеством точек
"""

import tkinter as tk

import messages as msg

def add_point(points, entries):
    """
        Добавление точки в таблицу
    """

    try:
        x = float(entries[0].get())
        y = float(entries[1].get())
    except:
        msg.add_error()
    else:
        cur_index = len(points.get_children('')) + 1
        points.insert('', index='end', text=cur_index, values=(x, y))


def index_update(points):
    """
        Обновление номеров точек
    """

    for i, point in enumerate(points.get_children()):
        points.item(point, text=i + 1)


def delete_point(points):
    """
        Удалениe точки из таблицы
    """

    try:
        points.delete(points.selection()[0])
        index_update(points)
    except IndexError:
        msg.delete_error()


def clean_all(points, entries, canvas):
    """
        Очистка всех элементов
        (таблицы точек, полей ввода, поля canvas)
    """

    points.delete(*points.get_children())
    entries[0].delete(0, 'end')
    entries[1].delete(0, 'end')
    canvas.delete('all')
