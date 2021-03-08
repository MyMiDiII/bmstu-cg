"""
    Модуль запуска приложения
"""

import tkinter as tk
import tkinter.messagebox as box
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import copy

import fish
import update


matplotlib.use('TkAgg')


AUTHOR_TITLE = 'Об авторе'
AUTHOR = 'Маслова Марина\nИУ7-43Б'


class root_window():
    """
        Класс главного окна
    """

    def __init__(self):
        """
            Конструктор класса
        """
        self.root = tk.Tk()
        self.root.geometry("1200x790+350+130")
        self.root.minsize(500, 100)
        self.root.resizable(True, True)
        self.root.title("ЛР2")


    def crt_menu(self):
        """
            Создание меню
        """
        self.menu = tk.Menu(self.root, font="TkMenuFont")

        self.menu.add_command(label=AUTHOR_TITLE,
                         command=lambda: box.showinfo(AUTHOR_TITLE, AUTHOR))
        self.menu.add_command(label='Выход', command=self.root.destroy)

        self.root.configure(menu=self.menu)


    def crtwdg_figure_centre(self):
        """
            Создание виджетов центра фигуры
        """
        self.lblfrm_figure_centre = tk.LabelFrame(self.root)
        self.lblfrm_figure_centre.place(relx=0.017, rely=0.013,
                                        relheight=0.109, relwidth=0.25)
        self.lblfrm_figure_centre.configure(
                relief='sunken',
                font=('DejaVu Sans', 12),
                text="Центр фигуры"
                )

        self.lbl_figure_centre = tk.Label(self.lblfrm_figure_centre)
        self.lbl_figure_centre.place(relx=0.007, rely=0.370,
                                     relheight=0.5, relwidth=0.98,
                                     bordermode='ignore')
        self.lbl_figure_centre.configure(
                font=('DejaVu Sans Mono', 12),
                text="X:{:7.2f}; Y:{:7.2f}".format(self.funcs[7].x_list[0],
                                                   self.funcs[7].y_list[0])
                )


    def crtwdg_transfer(self):
        """
            Создание виджетов переноса
        """
        self.lblfrm_transfer = tk.LabelFrame(self.root)
        self.lblfrm_transfer.place(relx=0.017, rely=0.133,
                                   relheight=0.157, relwidth=0.25)
        self.lblfrm_transfer.configure(relief='groove')
        self.lblfrm_transfer.configure(font=('DejaVu Sans', 12))
        self.lblfrm_transfer.configure(text="Перенос")

        self.lbl_dx = tk.Label(self.lblfrm_transfer)
        self.lbl_dx.place(relx=0.007, rely=0.29, height=29, width=53,
                          bordermode='ignore')
        self.lbl_dx.configure(font=('DejaVu Sans', 12))
        self.lbl_dx.configure(text="dx:")

        self.lbl_dy = tk.Label(self.lblfrm_transfer)
        self.lbl_dy.place(relx=0.007, rely=0.637, height=30, width=53,
                          bordermode='ignore')
        self.lbl_dy.configure(font=('DejaVu Sans', 12))
        self.lbl_dy.configure(text="dy:")

        self.ent_dx = tk.Entry(self.lblfrm_transfer)
        self.ent_dx.place(relx=0.164, rely=0.29, height=29, relwidth=0.389,
                          bordermode='ignore')
        self.ent_dx.configure(background="white")
        self.ent_dx.configure(font="TkFixedFont")
        self.ent_dx.configure(selectbackground="blue")
        self.ent_dx.configure(selectforeground="white")

        self.ent_dy = tk.Entry(self.lblfrm_transfer)
        self.ent_dy.place(relx=0.171, rely=0.645, height=29, relwidth=0.389,
                          bordermode='ignore')
        self.ent_dy.configure(background="white")
        self.ent_dy.configure(font="TkFixedFont")
        self.ent_dy.configure(selectbackground="blue")
        self.ent_dy.configure(selectforeground="white")

        self.btn_transfer = tk.Button(self.lblfrm_transfer)
        self.btn_transfer.place(relx=0.57, rely=0.282, height=77, width=120,
                           bordermode='ignore')
        self.btn_transfer.configure(activebackground="#f9f9f9")
        self.btn_transfer.configure(text="Перенести")
        self.btn_transfer.configure(command=lambda: update.move(self, FISH, FISHES))


    def crtwdg_trans_centre(self):
        """
            Создание виджетов центра преобразований
        """
        self.lblfrm_centre = tk.LabelFrame(self.root)
        self.lblfrm_centre.place(relx=0.017, rely=0.308,
                               relheight=0.147, relwidth=0.25)
        self.lblfrm_centre.configure(relief='groove')
        self.lblfrm_centre.configure(font=('DejaVu Sans', 12))
        self.lblfrm_centre.configure(text="Центр преобразований")

        self.lbl_xc = tk.Label(self.lblfrm_centre)
        self.lbl_xc.place(relx=0.017, rely=0.259, height=38, width=53,
                          bordermode='ignore')
        self.lbl_xc.configure(font=('DejaVu Sans', 12))
        self.lbl_xc.configure(text="Xc:")

        self.lbl_yc = tk.Label(self.lblfrm_centre)
        self.lbl_yc.place(relx=0.02, rely=0.612, height=37, width=53,
                            bordermode='ignore')
        self.lbl_yc.configure(activebackground="#f9f9f9")
        self.lbl_yc.configure(font=('DejaVu Sans', 12))
        self.lbl_yc.configure(text="Yc:")

        self.ent_xc = tk.Entry(self.lblfrm_centre)
        self.ent_xc.place(relx=0.208, rely=0.284, height=29, relwidth=0.725,
                          bordermode='ignore')
        self.ent_xc.configure(background="white")
        self.ent_xc.configure(font="TkFixedFont")
        self.ent_xc.insert(0, "0.00")

        self.ent_yc = tk.Entry(self.lblfrm_centre)
        self.ent_yc.place(relx=0.208, rely=0.638, height=29, relwidth=0.725,
                            bordermode='ignore')
        self.ent_yc.configure(background="white")
        self.ent_yc.configure(font="TkFixedFont")
        self.ent_yc.configure(selectbackground="blue")
        self.ent_yc.configure(selectforeground="white")
        self.ent_yc.insert(0, "0.00")


    def crtwdg_scaling(self):
        """
            Создание виджетов масштабирования
        """
        self.lblfrm_scaling = tk.LabelFrame(self.root)
        self.lblfrm_scaling.place(relx=0.017, rely=0.472, relheight=0.157,
                                 relwidth=0.25)
        self.lblfrm_scaling.configure(relief='groove')
        self.lblfrm_scaling.configure(font=('DejaVu Sans', 12))
        self.lblfrm_scaling.configure(text="Масштабирование")

        self.lbl_kx = tk.Label(self.lblfrm_scaling)
        self.lbl_kx.place(relx=0.007, rely=0.29, height=29, width=53
                , bordermode='ignore')
        self.lbl_kx.configure(activebackground="#f9f9f9")
        self.lbl_kx.configure(font=('DejaVu Sans', 12))
        self.lbl_kx.configure(text="Kx:")

        self.lbl_ky = tk.Label(self.lblfrm_scaling)
        self.lbl_ky.place(relx=0.507, rely=0.29, height=30, width=53
                , bordermode='ignore')
        self.lbl_ky.configure(activebackground="#f9f9f9")
        self.lbl_ky.configure(font=('DejaVu Sans', 12))
        self.lbl_ky.configure(text="Ky:")

        self.ent_kx = tk.Entry(self.lblfrm_scaling)
        self.ent_kx.place(relx=0.164, rely=0.29, height=29, relwidth=0.3
                , bordermode='ignore')
        self.ent_kx.configure(background="white")
        self.ent_kx.configure(font="TkFixedFont")
        self.ent_kx.configure(selectbackground="blue")
        self.ent_kx.configure(selectforeground="white")

        self.ent_ky = tk.Entry(self.lblfrm_scaling)
        self.ent_ky.place(relx=0.664, rely=0.29, height=29, relwidth=0.3
                , bordermode='ignore')
        self.ent_ky.configure(background="white")
        self.ent_ky.configure(font="TkFixedFont")
        self.ent_ky.configure(selectbackground="blue")
        self.ent_ky.configure(selectforeground="white")

        self.btn_scaling = tk.Button(self.lblfrm_scaling)
        self.btn_scaling.place(relx=0.025, rely=0.582, height=40, relwidth=0.94
                , bordermode='ignore')
        self.btn_scaling.configure(activebackground="#f9f9f9")
        self.btn_scaling.configure(text="Масштабировать")
        self.btn_scaling.configure(command= lambda: update.scale(self, FISH, FISHES))


    def crtwdg_turn(self):
        """
            Создание виджетов поворота
        """
        self.lblfrm_turn = tk.LabelFrame(self.root)
        self.lblfrm_turn.place(relx=0.017, rely=0.649, relheight=0.157,
                                   relwidth=0.25)
        self.lblfrm_turn.configure(relief='groove')
        self.lblfrm_turn.configure(font=('DejaVu Sans', 12))
        self.lblfrm_turn.configure(text="Поворот")

        self.lbl_angle = tk.Label(self.lblfrm_turn)
        self.lbl_angle.place(relx=0.025, rely=0.29,
                              bordermode='ignore')
        self.lbl_angle.configure(activebackground="#f9f9f9")
        self.lbl_angle.configure(font=('DejaVu Sans', 12))
        self.lbl_angle.configure(justify=tk.CENTER)
        self.lbl_angle.configure(text="Угол (°):")

        self.ent_angle = tk.Entry(self.lblfrm_turn)
        self.ent_angle.place(relx=0.390, rely=0.29, height=29, relwidth=0.57,
                              bordermode='ignore')
        self.ent_angle.configure(background="white")
        self.ent_angle.configure(cursor="fleur")
        self.ent_angle.configure(font="TkFixedFont")
        self.ent_angle.configure(selectbackground="blue")
        self.ent_angle.configure(selectforeground="white")

        self.btn_turn = tk.Button(self.lblfrm_turn)
        self.btn_turn.place(relx=0.025, rely=0.582, height=40, relwidth=0.94,
                               bordermode='ignore')
        self.btn_turn.configure(activebackground="#f9f9f9")
        self.btn_turn.configure(text="Повернуть")
        self.btn_turn.configure(command=lambda: update.turn(self, FISH, FISHES))


    def crtwdg_edit(self):
        """
            Создание виджетов редактирования
        """
        self.btn_undo = tk.Button(self.root)
        self.btn_undo.place(relx=0.016, rely=0.819, height=37, width=140)
        self.btn_undo.configure(text="← Назад")
        self.btn_undo.configure(state=tk.DISABLED)
        self.btn_undo.configure(command=lambda: update.undo(ROOT, FISH, FISHES))

        self.btn_redo = tk.Button(self.root)
        self.btn_redo.place(relx=0.151, rely=0.819, height=37, width=140)
        self.btn_redo.configure(activebackground="#f9f9f9")
        self.btn_redo.configure(text="Вперед →")
        self.btn_redo.configure(state=tk.DISABLED)
        self.btn_redo.configure(command=lambda: update.redo(ROOT, FISH, FISHES))

        self.btn_original = tk.Button(self.root)
        self.btn_original.place(relx=0.017, rely=0.876, height=37, width=300)
        self.btn_original.configure(text="Исходное изображение")
        self.lbl_figure_centre.configure(
                font=('DejaVu Sans Mono', 12),
                text="X:{:7.2f}; Y:{:7.2f}".format(self.funcs[7].x_list[0],
                                                   self.funcs[7].y_list[0])
                )
        self.btn_original.configure(command=lambda: update.reset(ROOT,
                                                   FISH, FISHES))

        self.btn_help = tk.Button(self.root)
        self.btn_help.place(relx=0.017, rely=0.932, height=37, width=300)
        self.btn_help.configure(activebackground="#f9f9f9")
        self.btn_help.configure(text="Справка")


    def create_matplotlib(self):
        """
            Создание окна matplotlib
        """
        margins = {
                "left"   : 0.050,
                "bottom" : 0.050,
                "right"  : 0.980,
                "top"    : 0.980
        }

        self.figure = plt.Figure(figsize=(8.5, 7.5))
        self.figure.subplots_adjust(**margins)
        self.subplt = self.figure.add_subplot(111)

        for func in self.funcs:
            self.subplt.plot(func.x_list, func.y_list, color='k', linewidth=2)

        self.subplt.set_xlim((-80, 80))
        self.subplt.set_ylim((-80, 80))
        self.subplt.grid(True)

        self.pltcnv = FigureCanvasTkAgg(self.figure, self.root)
        self.pltcnv.get_tk_widget().place(relx=0.28, rely=0.02, relheight=0.96,
                                          relwidth=0.71)


    def create_widgets(self):
        """
            Создание виджетов окна
        """
        self.crt_menu()
        self.crtwdg_figure_centre()
        self.crtwdg_transfer()
        self.crtwdg_trans_centre()
        self.crtwdg_scaling()
        self.crtwdg_turn()
        self.crtwdg_edit()
        self.create_matplotlib()


    def run(self):
        """
            Запуск окна
        """
        self.create_widgets()
        self.root.mainloop()


if __name__=="__main__":
    ROOT = root_window()
    FISH = fish.Fish()
    ROOT.funcs = FISH.full 
    FISHES = update.History(0, [copy.deepcopy(FISH)])
    ROOT.run()
