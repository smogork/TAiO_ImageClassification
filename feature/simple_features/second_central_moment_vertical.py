#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczajcą drugi moment centralny projekcji pionowej
"""

import copy
import statistics

from feature import feature
from bitmap import bitmap_grayscale


class SecondCentralMomentVerticalFeature(feature.Feature):
    """
    Klasa oblicza .
    Cecha 25.
    """

    def __init__(self):
        self.__columnsSum = []

    def calculate(self) -> float:
        return statistics.variance(self.__columnsSum)

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        for i in range(bitmap.get_height()):
            rowI = []
            for j in range(bitmap.get_width()):
                rowI.append(bitmap.get_cell_value(i, j))
            self.__columnsSum.append(sum(rowI))
