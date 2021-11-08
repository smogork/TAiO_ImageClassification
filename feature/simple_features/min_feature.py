#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczajcą minimalna wartość koloru obrazka w skali szarości
"""

from feature import feature
from bitmap import bitmap_grayscale


class MinFeature(feature.Feature):
    """
    Klasa oblicza podaje najmniejszy numer komórki, która nie jest biała.
    Cecha 3.
    """

    def __init__(self):
        self.__tab = []

    def calculate(self) -> float:
        i = 0
        for cell in self.__tab:
            if cell > 0:
                return i
            i += 1
        return i

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        for i in range(bitmap.get_width()):
            for j in range(bitmap.get_height()):
                self.__tab.append(bitmap.get_cell_value(i, j))
