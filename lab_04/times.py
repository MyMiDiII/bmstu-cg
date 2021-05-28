"""
    Модуль подсчета времени
"""

import matplotlib.pyplot as plt
import time

import circle
import ellipse


def getCircleTimes(scene, pen):
    """
        Подсчет времени окружностей
    """
    funcs = [
        circle.canon,
        circle.parametric,
        circle.brezenham,
        circle.midpoint,
    ]

    funcsNames = [
        "Каноническое уравнение",
        "Параметрическое уравнение",
        "Алгоритм Брезенхема",
        "Алгоритм средней точки"
    ]

    plt.rcParams['font.size'] = '16'
    plt.figure(figsize=(14.6, 7.9))
    plt.get_current_fig_manager().window.move(250, 100)
    plt.get_current_fig_manager().canvas.set_window_title("ВРЕМЯ ГЕНЕРАЦИИ ОКРУЖНОСТЕЙ")

    for i in range(4):
        timesList = []
        rList = []
        for r in range(0, 10000, 1000):
            sumtime = 0
            for _ in range(50):
                start = time.time()
                funcs[i](450, 400, r, scene, pen, False)
                sumtime += time.time() - start

            timesList.append(sumtime / 50)
            rList.append(r)
        plt.plot(rList, timesList, label=funcsNames[i])

    plt.title("ФИГУРА: ОКРУЖНОСТЬ")
    plt.xlabel("Радиус")
    plt.ylabel("Время, с")
    plt.grid()
    plt.legend()
    plt.show()


def getEllipseTimes(scene, pen):
    """
        Подсчет времени окружностей
    """
    funcs = [
        ellipse.canon,
        ellipse.parametric,
        ellipse.brezenham,
        ellipse.midpoint
    ]

    funcsNames = [
        "Каноническое уравнение",
        "Параметрическое уравнение",
        "Алгоритм Брезенхема",
        "Алгоритм средней точки"
    ]

    plt.rcParams['font.size'] = '16'
    plt.figure(figsize=(14.6, 7.9))
    plt.get_current_fig_manager().window.move(250, 100)
    plt.get_current_fig_manager().canvas.set_window_title("ВРЕМЯ ГЕНЕРАЦИИ ЭЛЛИПСОВ")

    for i in range(4):
        timesList = []
        rList = []

        coef = 1 / 2
        for Ra in range(0, 10000, 1000):
            Rb = Ra * coef
            sumtime = 0
            for _ in range(50):
                start = time.time()
                funcs[i](450, 400, Ra, Rb, scene, pen, False)
                sumtime += time.time() - start

            timesList.append(sumtime / 50)
            rList.append(Ra)

        plt.plot(rList, timesList, label=funcsNames[i])

    plt.title("ФИГУРА: ЭЛЛИПС")
    plt.xlabel("Полуось")
    plt.ylabel("Время, с")
    plt.grid()
    plt.legend()
    plt.show()
