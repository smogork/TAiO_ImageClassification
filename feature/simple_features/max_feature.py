#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczajcą numer  komórki, która nie jest biała
"""
from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.feature import Feature


class MaxFeature(Feature):
    """
    Klasa podaje największy numer komórki, która nie jest biała.
    Cecha 4.
    """

    def __init__(self):
        self.__tab = []

    def calculate(self) -> float:
        if len(self.__tab) == 0:
            raise RuntimeError("Run prepare() before calculate()")

        maximum = -1
        i = 0
        for cell in self.__tab:
            if cell < BitmapGrayscale.White:
                maximum = i
            i += 1
        return maximum

    def prepare(self, bitmap: BitmapGrayscale) -> None:
        for i in range(bitmap.get_width()):
            for j in range(bitmap.get_height()):
                self.__tab.append(bitmap.get_cell_value(i, j))
