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
        if not entries[0].get() or not entries[1].get():
            msg.create_errorbox('Пустой ввод', 'Для добавления точки введите в окна ввода X и Y вещественные числа!')
        else:
            msg.create_errorbox('Нечисловые данные', 'Координаты точки должны быть представлены вещественными числами!')

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
        if not len(points.get_children()):
            msg.create_errorbox('Отсутствие точек', 'Список точек пуст! Добавьте точки!')
        else:
            msg.create_errorbox('Не выбрана точка', 'Для удаления точки выберете её в таблице!')


def edit_point(points, entries, buttons, btn_app):
    """
        Редактирование точки из таблицы
    """

    for button in buttons:
        button.configure(state=tk.DISABLED)

    btn_app.configure(state=tk.NORMAL)

    entries[0].delete(0, 'end')
    entries[1].delete(0, 'end')

    selected_item = points.selection()[0]

    point = points.item(selected_item)["values"]

    entries[0].insert(0, point[0])
    entries[1].insert(0, point[1])


def apply(points, entries, buttons, btn_app):
    """
        Применение редактирования точки
    """
    try:
        x = float(entries[0].get())
        y = float(entries[1].get())

        selected_point = points.selection()[0]
        points.item(selected_point, values=(x, y))

        entries[0].delete(0, 'end')
        entries[1].delete(0, 'end')

        for button in buttons:
            button.configure(state=tk.NORMAL)

        btn_app.configure(state=tk.DISABLED)
    except:
        msg.add_error()


def clean_all(points, entries, canvas):
    """
        Очистка всех элементов
        (таблицы точек, полей ввода, поля canvas)
    """

    points.delete(*points.get_children())
    entries[0].delete(0, 'end')
    entries[1].delete(0, 'end')
    canvas.delete('all')


