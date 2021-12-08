#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczajcą drugi moment centralny projekcji poziomej
"""

import copy
import statistics

import numpy as np

from feature import feature
from bitmap import bitmap_grayscale


class SecondCentralMomentHorizontalFeature(feature.Feature):
    """
    Klasa oblicza .
    Cecha 23.
    """

    def __init__(self):
        self.__rowsSum = None

    def calculate(self) -> float:
        if self.__rowsSum is None:
            raise RuntimeError("Run prepare() before calculate()")

        return self.__rowsSum.var()

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__rowsSum = np.zeros(bitmap.get_height())
        for i in range(bitmap.get_height()):
            self.__rowsSum[i] = bitmap.get_row(i)
