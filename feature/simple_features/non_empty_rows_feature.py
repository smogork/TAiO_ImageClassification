#! /usr/bin/env python

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
    Threashold blisko czarnego
    """

    def __init__(self, threshold: float):
        self.__bitmap = None
        self.__threshold = threshold

    def calculate(self) -> float:
        count = 0.0
        for i in range(self.__bitmap.get_height()):
            for j in range(self.__bitmap.get_width()):
                if self.__bitmap.get_cell_value(i, j) >= self.__threshold:
                    count += 1.0
                    break
        return count

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__bitmap = copy.deepcopy(bitmap)
