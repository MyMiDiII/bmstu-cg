"""
    Модуль для вывода сообщений
"""

import tkinter as tk
import tkinter.messagebox as box
from PIL import ImageTk, Image

NAME = 'Маслова Марина'
GROUP = 'ИУ7-43Б'
AUTHOR = NAME + '\n' + GROUP

IMAGE_PATH = 'images/'
MSGS_PATH = IMAGE_PATH + 'msg_icons/'
INFO_ICON = MSGS_PATH + 'info_icon.png'
ERROR_ICON = MSGS_PATH + 'error_icon.png'

PROBLEM_TEXT = (  'На  плоскости  дано  множество точек. Найти такой\n'
                + 'треугольник с вершинами в этих точках, у которого\n'
                + 'разность  максимального и минимального количества\n'
                + 'точек,  попавших  в каждый из 6-ти треугольников,\n'
                + 'образованных  пересечением  медиан,  максимальна.\n'
                + 'Сделать  в  графическом  режиме  вывод полученной\n'
                + 'картинки.')


def create_okbox(title, text, image_path):
    """
        Создание сообщения с одной кнопкой OK
    """
    infobox = tk.Toplevel()
    infobox.title(title)
    infobox.geometry('+700+450')

    pil_img = Image.open(image_path).resize((60, 60))
    img = ImageTk.PhotoImage(pil_img)

    lbl_img = tk.Label(infobox)
    lbl_img.grid(row=1, column=1)
    lbl_img.image = img
    lbl_img.configure(image=img)

    lbl_text = tk.Label(infobox)
    lbl_text.grid(row=1, column=3)
    lbl_text.configure(text=text, justify=tk.LEFT, font=('Courier', 12))

    btn_ok = tk.Button(infobox)
    btn_ok.grid(row=3, column=0, columnspan=5)
    btn_ok.configure(text='OK')
    btn_ok.configure(command=infobox.destroy)


def create_infobox(title, text):
    """
        Создание информационного сообщения
    """
    create_okbox(title, text, INFO_ICON)


def create_errorbox(title, text):
    """
        Создание сообщения об ошибке
    """
    create_okbox(title, text, ERROR_ICON)


def author():
    """
        Вывод сообщения об авторе
    """
    create_infobox('Об авторе', AUTHOR)


def problem():
    """
        Вывод условия задачи
    """
    create_infobox('Условие задачи', PROBLEM_TEXT)


def add_error():
    """
        Вывод сообщения об ошибке при вводе точки
    """
    create_errorbox('Ошибка', 'Ошибка при добавлении точки!')


def delete_error():
    """
        Вывод сообщения об ошибке при удалении точки
    """
    create_errorbox('Не выбрана точка', "Для удаления выберете точку в списке!")
