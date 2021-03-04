"""
    Модуль запуска приложения
"""

import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import fish


matplotlib.use('TkAgg')


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
        self.menu = tk.Menu(self.root,font="TkMenuFont")
        self.root.configure(menu = self.menu)


    def crtwdg_figure_centre(self):
        """
            Создание виджетов центра фигуры
        """
        self.lblfrm_figure_centre = tk.LabelFrame(self.root)
        self.lblfrm_figure_centre.place(relx=0.017, rely=0.013,
                                        relheight=0.109, relwidth=0.25)
        self.lblfrm_figure_centre.configure(relief='sunken')
        self.lblfrm_figure_centre.configure(font=('DejaVu Sans', 12))
        self.lblfrm_figure_centre.configure(relief='sunken')
        self.lblfrm_figure_centre.configure(text="Центр фигуры")

        self.lbl_figure_centre = tk.Label(self.lblfrm_figure_centre)
        self.lbl_figure_centre.place(relx=0.007, rely=0.370,
                                     height=42, width=288,
                                     bordermode='ignore')
        self.lbl_figure_centre.configure(font=('DejaVu Sans', 14))
        self.lbl_figure_centre.configure(text="X:    0.00  Y:    0.00")


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


    def crtwdg_trans_centre(self):
        """
            Создание виджетов центра преобразований
        """
        self.lbl_frame4 = tk.LabelFrame(self.root)
        self.lbl_frame4.place(relx=0.017, rely=0.308,
                               relheight=0.147, relwidth=0.25)
        self.lbl_frame4.configure(relief='groove')
        self.lbl_frame4.configure(font=('DejaVu Sans', 12))
        self.lbl_frame4.configure(text="Центр преобразований")

        self.lbl_4 = tk.Label(self.lbl_frame4)
        self.lbl_4.place(relx=0.017, rely=0.259, height=38, width=53,
                          bordermode='ignore')
        self.lbl_4.configure(font=('DejaVu Sans', 12))
        self.lbl_4.configure(text="Xc:")

        self.lbl_4_3 = tk.Label(self.lbl_frame4)
        self.lbl_4_3.place(relx=0.02, rely=0.612, height=37, width=53,
                            bordermode='ignore')
        self.lbl_4_3.configure(activebackground="#f9f9f9")
        self.lbl_4_3.configure(font=('DejaVu Sans', 12))
        self.lbl_4_3.configure(text="Yc:")

        self.Entry3 = tk.Entry(self.lbl_frame4)
        self.Entry3.place(relx=0.208, rely=0.284, height=29, relwidth=0.725,
                          bordermode='ignore')
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")

        self.Entry3_1 = tk.Entry(self.lbl_frame4)
        self.Entry3_1.place(relx=0.208, rely=0.638, height=29, relwidth=0.725,
                            bordermode='ignore')
        self.Entry3_1.configure(background="white")
        self.Entry3_1.configure(font="TkFixedFont")
        self.Entry3_1.configure(selectbackground="blue")
        self.Entry3_1.configure(selectforeground="white")


    def crtwdg_scaling(self):
        """
            Создание виджетов масштабирования
        """
        self.lbl_frame2_1 = tk.LabelFrame(self.root)
        self.lbl_frame2_1.place(relx=0.017, rely=0.472, relheight=0.157,
                                 relwidth=0.25)
        self.lbl_frame2_1.configure(relief='groove')
        self.lbl_frame2_1.configure(font=('DejaVu Sans', 12))
        self.lbl_frame2_1.configure(text="Масштабирование")

        self.lbl_2_1 = tk.Label(self.lbl_frame2_1)
        self.lbl_2_1.place(relx=0.007, rely=0.29, height=29, width=53
                , bordermode='ignore')
        self.lbl_2_1.configure(activebackground="#f9f9f9")
        self.lbl_2_1.configure(font=('DejaVu Sans', 12))
        self.lbl_2_1.configure(text="Kx:")

        self.lbl_3_1 = tk.Label(self.lbl_frame2_1)
        self.lbl_3_1.place(relx=0.507, rely=0.29, height=30, width=53
                , bordermode='ignore')
        self.lbl_3_1.configure(activebackground="#f9f9f9")
        self.lbl_3_1.configure(font=('DejaVu Sans', 12))
        self.lbl_3_1.configure(text="Ky:")

        self.Entry1_1 = tk.Entry(self.lbl_frame2_1)
        self.Entry1_1.place(relx=0.164, rely=0.29, height=29, relwidth=0.3
                , bordermode='ignore')
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(selectbackground="blue")
        self.Entry1_1.configure(selectforeground="white")

        self.Entry2_1 = tk.Entry(self.lbl_frame2_1)
        self.Entry2_1.place(relx=0.664, rely=0.29, height=29, relwidth=0.3
                , bordermode='ignore')
        self.Entry2_1.configure(background="white")
        self.Entry2_1.configure(font="TkFixedFont")
        self.Entry2_1.configure(selectbackground="blue")
        self.Entry2_1.configure(selectforeground="white")

        self.Button1_1 = tk.Button(self.lbl_frame2_1)
        self.Button1_1.place(relx=0.025, rely=0.582, height=40, relwidth=0.94
                , bordermode='ignore')
        self.Button1_1.configure(activebackground="#f9f9f9")
        self.Button1_1.configure(text="Масштабировать")


    def crtwdg_turn(self):
        """
            Создание виджетов поворота
        """
        self.lbl_frame2_1_1 = tk.LabelFrame(self.root)
        self.lbl_frame2_1_1.place(relx=0.017, rely=0.649, relheight=0.157,
                                   relwidth=0.25)
        self.lbl_frame2_1_1.configure(relief='groove')
        self.lbl_frame2_1_1.configure(font=('DejaVu Sans', 12))
        self.lbl_frame2_1_1.configure(text="Поворот")

        self.lbl_2_1_1 = tk.Label(self.lbl_frame2_1_1)
        self.lbl_2_1_1.place(relx=0.025, rely=0.29,
                              bordermode='ignore')
        self.lbl_2_1_1.configure(activebackground="#f9f9f9")
        self.lbl_2_1_1.configure(font=('DejaVu Sans', 12))
        self.lbl_2_1_1.configure(justify=tk.CENTER)
        self.lbl_2_1_1.configure(text="Угол (°):")

        self.Entry1_1_1 = tk.Entry(self.lbl_frame2_1_1)
        self.Entry1_1_1.place(relx=0.390, rely=0.29, height=29, relwidth=0.57,
                              bordermode='ignore')
        self.Entry1_1_1.configure(background="white")
        self.Entry1_1_1.configure(cursor="fleur")
        self.Entry1_1_1.configure(font="TkFixedFont")
        self.Entry1_1_1.configure(selectbackground="blue")
        self.Entry1_1_1.configure(selectforeground="white")

        self.Button1_1_1 = tk.Button(self.lbl_frame2_1_1)
        self.Button1_1_1.place(relx=0.025, rely=0.582, height=40, relwidth=0.94,
                               bordermode='ignore')
        self.Button1_1_1.configure(activebackground="#f9f9f9")
        self.Button1_1_1.configure(text="Повернуть")


    def crtwdg_edit(self):
        """
            Создание виджетов редактирования
        """
        self.Button2 = tk.Button(self.root)
        self.Button2.place(relx=0.016, rely=0.819, height=37, width=140)
        self.Button2.configure(text="← Назад")

        self.Button2_1 = tk.Button(self.root)
        self.Button2_1.place(relx=0.151, rely=0.819, height=37, width=140)
        self.Button2_1.configure(activebackground="#f9f9f9")
        self.Button2_1.configure(text="Вперед →")

        self.Button3 = tk.Button(self.root)
        self.Button3.place(relx=0.017, rely=0.876, height=37, width=300)
        self.Button3.configure(text="Исходное изображение")

        self.Button3_1 = tk.Button(self.root)
        self.Button3_1.place(relx=0.017, rely=0.932, height=37, width=300)
        self.Button3_1.configure(activebackground="#f9f9f9")
        self.Button3_1.configure(text="Справка")


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

        self.subplt.set_xlim((-60, 60))
        self.subplt.set_ylim((-60, 60))
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
    FISHES = [FISH.full]
    ROOT.run()
