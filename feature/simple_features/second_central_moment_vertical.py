#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczajcą drugi moment centralny projekcji pionowej
"""

import copy
import statistics

import numpy as np

from feature import feature
from bitmap import bitmap_grayscale


class SecondCentralMomentVerticalFeature(feature.Feature):
    """
    Klasa oblicza .
    Cecha 25.
    """

    def __init__(self):
        self.__columnsSum = None

    def calculate(self) -> float:
        if self.__columnsSum is None:
            raise RuntimeError("Run prepare() before calculate()")

        return self.__columnsSum.var()

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__columnsSum = np.zeros(bitmap.get_height())
        for i in range(bitmap.get_width()):
            self.__columnsSum[i] = bitmap.get_column(i).sum()
