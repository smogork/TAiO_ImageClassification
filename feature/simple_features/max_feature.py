#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczajcą numer  komórki, która nie jest biała
"""
import numpy as np

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.feature import Feature


class MaxFeature(Feature):
    """
    Klasa podaje największy numer komórki, która nie jest biała.
    Cecha 4.
    """

    def __init__(self):
        self.__tab = None

    def calculate(self) -> float:
        if self.__tab is None or len(self.__tab) == 0:
            raise RuntimeError("Run prepare() before calculate()")

        maximum = -1
        i = 0
        for cell in self.__tab:
            if cell < BitmapGrayscale.White:
                maximum = i
            i += 1
        self.__tab = None
        return maximum

    def prepare(self, bitmap: BitmapGrayscale) -> None:
        self.__tab = np.zeros(bitmap.get_height() *  bitmap.get_width())
        for i in range(bitmap.get_width()):
            for j in range(bitmap.get_height()):
                self.__tab[i * bitmap.get_width() + j] = bitmap.get_cell_value(i, j)
