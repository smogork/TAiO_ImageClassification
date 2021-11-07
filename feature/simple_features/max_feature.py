#! /usr/bin/env python3

from feature import feature
from bitmap import bitmap_grayscale
import statistics


class MaxFeature(feature.Feature):
    """
    Klasa oblicza podaje największy numer komórki, która nie jest biała
    """

    def __init__(self):
        self.__tab = []

    def calculate(self) -> float:
        maximum = 0
        i = 0
        for cell in self.__tab:
            if cell > 0:
                maximum = i
            i += 1
        return i

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        for i in range(bitmap.get_height()):
            for j in range(bitmap.get_width()):
                self.__tab.append(bitmap.get_cell_value(i, j))
