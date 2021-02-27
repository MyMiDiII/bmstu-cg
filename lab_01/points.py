"""
    Модуль для работы с множеством точек
"""

import tkinter as tk

import messages as msg


EMPTY_ENTRY = ('Для добавления точки введите в окна\n'
               + 'ввода X и Y вещественные числа!')
EMPTY_APP_ENTRY = ('При редактировании нельзя оставлять\n'
                   + 'поля ввода пустыми!')
NOT_FLOAT = ('Координаты точки должны быть\n'
             + 'представлены вещественными числами!')
NO_POINTS = 'Список точек пуст! Добавьте точки!'
NO_DEL_SELECTION = 'Для удаления точки выберете её в таблице!'
NO_EDIT_SELECTION = 'Для редактирования точки выберете её в таблице!'


def add_point(points, entries):
    """
        Добавление точки в таблицу
    """
    try:
        x = float(entries[0].get())
        y = float(entries[1].get())
    except:
        if not entries[0].get() or not entries[1].get():
            msg.create_errorbox('Пустой ввод', EMPTY_ENTRY)
        else:
            msg.create_errorbox('Нечисловые данные', NOT_FLOAT)

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
            msg.create_errorbox('Отсутствие точек', NO_POINTS)
        else:
            msg.create_errorbox('Не выбрана точка', NO_DEL_SELECTION)


def edit_point(points, entries, buttons, btn_app):
    """
        Редактирование точки из таблицы
    """

    try:
        selected_item = points.selection()[0]
        point = points.item(selected_item)["values"]

        entries[0].delete(0, 'end')
        entries[1].delete(0, 'end')

        entries[0].insert(0, point[0])
        entries[1].insert(0, point[1])

        for button in buttons:
            button.configure(state=tk.DISABLED)

        btn_app.configure(state=tk.NORMAL)
        points.configure(selectmode='none')

    except IndexError:
        if not len(points.get_children()):
            msg.create_errorbox('Отсутствие точек', NO_POINTS)
        else:
            msg.create_errorbox('Не выбрана точка', NO_EDIT_SELECTION)



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
        points.configure(selectmode='browse')
    except:
        if not entries[0].get() or not entries[1].get():
            msg.create_errorbox('Пустой ввод', EMPTY_APP_ENTRY)
        else:
            msg.create_errorbox('Нечисловые данные', NOT_FLOAT)


def clean_all(points, entries, canvas):
    """
        Очистка всех элементов
        (таблицы точек, полей ввода, поля canvas)
    """

    points.delete(*points.get_children())
    entries[0].delete(0, 'end')
    entries[1].delete(0, 'end')
    canvas.delete('all')


