"""
    Модуль с 3D функциями
"""
from math import sin, cos, sqrt

funcs = [
    lambda x, z: cos(x * sin(z)),
    lambda x, z: cos(sqrt(x * x + z * z)),
    lambda x, z: sin(x) ** 2 + cos(z) ** 2
]