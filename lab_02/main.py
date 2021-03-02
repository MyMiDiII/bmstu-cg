"""
    Модуль запуска приложения
"""

import tkinter as tk


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

        self.Label2 = tk.Label(self.lblfrm_transfer)
        self.Label2.place(relx=0.007, rely=0.29, height=29, width=53,
                          bordermode='ignore')
        self.Label2.configure(font=('DejaVu Sans', 12))
        self.Label2.configure(text="dx:")

        self.Label3 = tk.Label(self.lblfrm_transfer)
        self.Label3.place(relx=0.007, rely=0.637, height=30, width=53,
                          bordermode='ignore')
        self.Label3.configure(font=('DejaVu Sans', 12))
        self.Label3.configure(text="dy:")

        self.Entry1 = tk.Entry(self.lblfrm_transfer)
        self.Entry1.place(relx=0.164, rely=0.29, height=29, relwidth=0.389,
                          bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")

        self.Entry2 = tk.Entry(self.lblfrm_transfer)
        self.Entry2.place(relx=0.171, rely=0.645, height=29, relwidth=0.389,
                          bordermode='ignore')
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(selectbackground="blue")
        self.Entry2.configure(selectforeground="white")

        self.Button1 = tk.Button(self.lblfrm_transfer)
        self.Button1.place(relx=0.57, rely=0.282, height=77, width=120,
                           bordermode='ignore')
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text="Перенести")


    def crtwdg_trans_centre(self):
        """
            Создание виджетов центра преобразований
        """
        self.Labelframe4 = tk.LabelFrame(self.root)
        self.Labelframe4.place(relx=0.017, rely=0.308,
                               relheight=0.147, relwidth=0.25)
        self.Labelframe4.configure(relief='groove')
        self.Labelframe4.configure(font=('DejaVu Sans', 12))
        self.Labelframe4.configure(text="Центр преобразований")

        self.Label4 = tk.Label(self.Labelframe4)
        self.Label4.place(relx=0.017, rely=0.259, height=38, width=53,
                          bordermode='ignore')
        self.Label4.configure(font=('DejaVu Sans', 12))
        self.Label4.configure(text="Xc:")

        self.Label4_3 = tk.Label(self.Labelframe4)
        self.Label4_3.place(relx=0.02, rely=0.612, height=37, width=53,
                            bordermode='ignore')
        self.Label4_3.configure(activebackground="#f9f9f9")
        self.Label4_3.configure(font=('DejaVu Sans', 12))
        self.Label4_3.configure(text="Yc:")

        self.Entry3 = tk.Entry(self.Labelframe4)
        self.Entry3.place(relx=0.208, rely=0.284, height=29, relwidth=0.725,
                          bordermode='ignore')
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")

        self.Entry3_1 = tk.Entry(self.Labelframe4)
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
        self.Labelframe2_1 = tk.LabelFrame(self.root)
        self.Labelframe2_1.place(relx=0.017, rely=0.472, relheight=0.157,
                                 relwidth=0.25)
        self.Labelframe2_1.configure(relief='groove')
        self.Labelframe2_1.configure(font=('DejaVu Sans', 12))
        self.Labelframe2_1.configure(text="Масштабирование")

        self.Label2_1 = tk.Label(self.Labelframe2_1)
        self.Label2_1.place(relx=0.007, rely=0.29, height=29, width=53
                , bordermode='ignore')
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(font=('DejaVu Sans', 12))
        self.Label2_1.configure(text="Kx:")

        self.Label3_1 = tk.Label(self.Labelframe2_1)
        self.Label3_1.place(relx=0.007, rely=0.637, height=30, width=53
                , bordermode='ignore')
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(font=('DejaVu Sans', 12))
        self.Label3_1.configure(text="Ky:")

        self.Entry1_1 = tk.Entry(self.Labelframe2_1)
        self.Entry1_1.place(relx=0.164, rely=0.29, height=29, relwidth=0.289
                , bordermode='ignore')
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(selectbackground="blue")
        self.Entry1_1.configure(selectforeground="white")

        self.Entry2_1 = tk.Entry(self.Labelframe2_1)
        self.Entry2_1.place(relx=0.164, rely=0.645, height=29, relwidth=0.289
                , bordermode='ignore')
        self.Entry2_1.configure(background="white")
        self.Entry2_1.configure(font="TkFixedFont")
        self.Entry2_1.configure(selectbackground="blue")
        self.Entry2_1.configure(selectforeground="white")

        self.Button1_1 = tk.Button(self.Labelframe2_1)
        self.Button1_1.place(relx=0.47, rely=0.282, height=77, width=180
                , bordermode='ignore')
        self.Button1_1.configure(activebackground="#f9f9f9")
        self.Button1_1.configure(text="Масштабировать")


    def crtwdg_turn(self):
        """
            Создание виджетов поворота
        """
        self.Labelframe2_1_1 = tk.LabelFrame(self.root)
        self.Labelframe2_1_1.place(relx=0.017, rely=0.649, relheight=0.157,
                                   relwidth=0.25)
        self.Labelframe2_1_1.configure(relief='groove')
        self.Labelframe2_1_1.configure(font=('DejaVu Sans', 12))
        self.Labelframe2_1_1.configure(text="Поворот")

        self.Label2_1_1 = tk.Label(self.Labelframe2_1_1)
        self.Label2_1_1.place(relx=0.060, rely=0.242, relheight=0.3, width=133,
                              bordermode='ignore')
        self.Label2_1_1.configure(activebackground="#f9f9f9")
        self.Label2_1_1.configure(font=('DejaVu Sans', 12))
        self.Label2_1_1.configure(justify=tk.CENTER)
        self.Label2_1_1.configure(text="Угол (°):")

        self.Entry1_1_1 = tk.Entry(self.Labelframe2_1_1)
        self.Entry1_1_1.place(relx=0.054, rely=0.637, height=29, relwidth=0.456,
                              bordermode='ignore')
        self.Entry1_1_1.configure(background="white")
        self.Entry1_1_1.configure(cursor="fleur")
        self.Entry1_1_1.configure(font="TkFixedFont")
        self.Entry1_1_1.configure(selectbackground="blue")
        self.Entry1_1_1.configure(selectforeground="white")

        self.Button1_1_1 = tk.Button(self.Labelframe2_1_1)
        self.Button1_1_1.place(relx=0.57, rely=0.282, height=77, width=120,
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


    def run(self):
        """
            Запуск окна
        """
        self.create_widgets()
        self.root.mainloop()


if __name__=="__main__":
    ROOT = root_window()
    ROOT.run()
