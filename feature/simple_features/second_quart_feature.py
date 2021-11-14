#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczajcą liczbę punktów o wartościach (1/4, 2/4]
"""

import copy

from feature import feature
from bitmap import bitmap_grayscale


class SecondQuartFeature(feature.Feature):
    """
    Klasa oblicza .
    Cecha 19.
    """

    def __init__(self, threshold: float):
        self.__points = []

    def calculate(self) -> float:
        count = 0
        for x in self.__points:
            if 0.25 < x <= 0.5:
                count += 1
        return count

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        for i in range(bitmap.get_width()):
            for j in range(bitmap.get_height()):
                self.__points.append(bitmap.get_cell_value(i, j))
