#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczajcą drugi moment centralny projekcji poziomej
"""

import copy
import statistics

from feature import feature
from bitmap import bitmap_grayscale


class SecondCentralMomentHorizontalFeature(feature.Feature):
    """
    Klasa oblicza .
    Cecha 23.
    """

    def __init__(self):
        self.__rowsSum = []

    def calculate(self) -> float:
        return statistics.variance(self.__rowsSum)

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        for i in range(bitmap.get_height()):
            rowI = []
            for j in range(bitmap.get_width()):
                rowI.append(bitmap.get_cell_value(i, j))
            self.__rowsSum.append(sum(rowI))
