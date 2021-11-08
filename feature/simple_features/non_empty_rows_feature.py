#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczajcą najdłuższy nie pusty wiersz na obrazku w skali szarości
"""

import copy

from feature import feature
from bitmap import bitmap_grayscale



class NonEmptyRowsFeature(feature.Feature):
    """
    Klasa oblicza liczbę niepustych wierszy
    Cecha 6.
    """

    def __init__(self):
        self.__bitmap = None

    def calculate(self) -> float:
        count = 0
        for j in range(self.__bitmap.get_width()):
            for i in range(self.__bitmap.get_height()):
                if self.__bitmap.get_cell_value(i, j) > 0:
                    count += 1
                    break

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__bitmap = copy.deepcopy(bitmap)
