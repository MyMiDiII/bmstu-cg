"""
    Модуль для создания интерфейса приложения
"""

import tkinter as tk
import tkinter.ttk as ttk

import messages as msg
import points as pnts
import problem as prob


MAIN_BG = '#a6f0ff'

COLUMNS = ('#1', '#2')


def create_menu(window):
    """
        Создание меню
    """

    menu = tk.Menu()

    menu.add_command(label='Об авторе', command=msg.author)
    menu.add_command(label='Выход', command=window.destroy)

    window.config(menu=menu)


def create_lables(window):
    """
        Создание подсказок
    """

    lbl_points= tk.Label(window)
    lbl_points.place(relx=0.023, rely=0.0, relwidth=0.244, relheight=0.057)
    lbl_points.configure(background=MAIN_BG)
    lbl_points.configure(font='-family {Fira Code} -size 10')
    lbl_points.configure(text='Список точек')

    lbl_x = tk.Label(window)
    lbl_x.place(relx=0.023, rely=0.411, relwidth=0.028, relheight=0.047)
    lbl_x.configure(background=MAIN_BG)
    lbl_x.configure(text='X:')

    lbl_y = tk.Label(window)
    lbl_y.place(relx=0.023, rely=0.464, relwidth=0.028, relheight=0.047)
    lbl_y.configure(background=MAIN_BG)
    lbl_y.configure(text='Y:')


def create_table(window):
    """
        Создание таблицы точек
    """

    tr_points = ttk.Treeview(window, columns=COLUMNS)

    tr_points.heading('#0', text='№')
    tr_points.heading('#1', text='X')
    tr_points.heading('#2', text='Y')

    tr_points.column('#0', minwidth=30, width=108, stretch=True)
    tr_points.column('#1', minwidth=30, width=108, stretch=True)
    tr_points.column('#2', minwidth=30, width=108, stretch=True)

    tr_points.place(relx=0.023, rely=0.057, relheight=0.337, relwidth=0.247)

    return tr_points


def create_buttons(window, points, entries, canvas):
    """
        Создание кнопок
    """
    btn_add = tk.Button(window)
    btn_add.place(relx=0.023, rely=0.529, relwidth=0.242, relheight=0.05)
    btn_add.configure(activebackground="#f9f9f9")
    btn_add.configure(text='Добавить точку')
    btn_add.configure(command=lambda: pnts.add_point(points, entries))

    btn_delete = tk.Button(window)
    btn_delete.place(relx=0.023, rely=0.589, relwidth=0.242, relheight=0.05)
    btn_delete.configure(activebackground="#f9f9f9")
    btn_delete.configure(text='Удалить точку')
    btn_delete.configure(command=lambda: pnts.delete_point(points))

    btn_solve = tk.Button(window)
    btn_solve.place(relx=0.023, rely=0.805, relwidth=0.242, relheight=0.05)
    btn_solve.configure(activebackground="#f9f9f9")
    btn_solve.configure(background="#4cd876")
    btn_solve.configure(text='Решить')
    btn_solve.configure(command=lambda: prob.call_solve_problem(points, canvas))

    btn_clean = tk.Button(window)
    btn_clean.place(relx=0.023, rely=0.865, relwidth=0.242, relheight=0.05)
    btn_clean.configure(activebackground="#cecced")
    btn_clean.configure(background="#d84e4e")
    btn_clean.configure(text='Очистить вcё')
    btn_clean.configure(command=lambda: pnts.clean_all(points, entries, canvas))

    btn_problem = tk.Button(window)
    btn_problem.place(relx=0.023, rely=0.925, relwidth=0.242, relheight=0.05)
    btn_problem.configure(activebackground="#f9f9f9")
    btn_problem.configure(background="#3fb9d8")
    btn_problem.configure(text='Условие задачи')
    btn_problem.configure(command=msg.problem)

    btn_edit = tk.Button(window)
    btn_apply = tk.Button(window)

    btns = [btn_add, btn_delete, btn_edit, btn_clean, btn_solve]

    btn_edit.place(relx=0.023, rely=0.649, relwidth=0.242, relheight=0.05)
    btn_edit.configure(activebackground="#f9f9f9")
    btn_edit.configure(text='Редактировать точку')
    btn_edit.configure(command=lambda: pnts.edit_point(points, entries, 
                                                       btns, btn_apply))

    btn_apply.place(relx=0.023, rely=0.709, relwidth=0.242, relheight=0.05)
    btn_apply.configure(activebackground="#f9f9f9")
    btn_apply.configure(text='Применить редактирование')
    btn_apply.configure(state=tk.DISABLED)
    btn_apply.configure(command=lambda: pnts.apply(points, entries,
                                                   btns, btn_apply))


def create_entry(window):
    """
        Создание полей ввода
    """
    ent_x = tk.Entry(window)
    ent_x.place(relx=0.061, rely=0.419, relwidth=0.201, relheight=0.036)
    ent_x.configure(background="white")
    ent_x.configure(font="TkFixedFont")
    ent_x.configure(selectbackground="blue")
    ent_x.configure(selectforeground="white")

    ent_y = tk.Entry(window)
    ent_y.place(relx=0.061, rely=0.470, relwidth=0.201, relheight=0.036)
    ent_y.configure(background="white")
    ent_y.configure(font="TkFixedFont")
    ent_y.configure(selectbackground="blue")
    ent_y.configure(selectforeground="white")

    return [ent_x, ent_y]


def on_resize(event, sizes, canvas):
    """
        Масштабирование содержимого canvas
    """
    wscale = float(event.width)/sizes[0]
    hscale = float(event.height)/sizes[1]

    sizes[0] = event.width
    sizes[1] = event.height

    canvas.configure(width=sizes[0], height=sizes[1])
    canvas.scale("all", 0, 0, wscale, hscale)


def create_canvas(window):
    """
        Создание окна графического решения
    """
    cnv_solution = tk.Canvas(window)
    cnv_solution.place(relx=0.289, y=0, relheight=1.0, relwidth=0.713)
    cnv_solution.configure(background="#ffffff")
    cnv_solution.configure(borderwidth="2")
    cnv_solution.configure(highlightbackground="#ffffff")
    cnv_solution.configure(insertbackground="#ffffff")
    cnv_solution.configure(relief="raised")
    cnv_solution.configure(selectbackground="#2908ff")
    cnv_solution.configure(selectforeground="#ffffff")
    cnv_solution.addtag_all("all")

    cnv_sizes = [cnv_solution.winfo_reqwidth(), cnv_solution.winfo_reqheight()]
    cnv_solution.bind("<Configure>", lambda event: on_resize(event, cnv_sizes, cnv_solution))

    return cnv_solution


def create_window():
    """
        Создание окна приложения
    """

    window = tk.Tk()
    window.title('ЛР1')
    window.geometry('1320x800+300+100')
    window.minsize(939, 676)
    window.configure(bg=MAIN_BG)

    create_menu(window)
    create_lables(window)
    points = create_table(window)
    entries = create_entry(window)
    canvas = create_canvas(window)
    create_buttons(window, points, entries, canvas)

    window.mainloop()


if __name__ == '__main__':
    create_window()
