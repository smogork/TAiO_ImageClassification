#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczajcą najbielszą komórkę na obrazku w skali szarości
"""

from feature import feature
from bitmap import bitmap_grayscale


class MaxFeature(feature.Feature):
    """
    Klasa oblicza podaje największy numer komórki, która nie jest biała.
    Cecha 4.
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
        return maximum

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        for i in range(bitmap.get_width()):
            for j in range(bitmap.get_height()):
                self.__tab.append(bitmap.get_cell_value(i, j))
