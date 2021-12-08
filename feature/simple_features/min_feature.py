#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczajcą minimalna wartość koloru obrazka w skali szarości
"""
import numpy as np
from bitmap.bitmap_grayscale import BitmapGrayscale
from feature import feature
from bitmap import bitmap_grayscale


class MinFeature(feature.Feature):
    """
    Klasa oblicza podaje najmniejszy numer komórki, która nie jest biała.
    Cecha 3.
    """

    def __init__(self):
        self.__tab = None

    def calculate(self) -> float:
        if self.__tab is None or len(self.__tab) == 0:
            raise RuntimeError("Run prepare() before calculate()")

        i = 0
        for cell in self.__tab:
            if cell < BitmapGrayscale.White:
                self.__tab = None
                return i
            i += 1
        self.__tab = None
        return -1

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__tab = np.zeros(bitmap.get_height() * bitmap.get_width())
        for i in range(bitmap.get_width()):
            for j in range(bitmap.get_height()):
                self.__tab[i * bitmap.get_width() + j] = bitmap.get_cell_value(i, j)
