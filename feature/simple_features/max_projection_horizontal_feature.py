#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczającą numer wiersza, którego projekcja ma największą wartość.
"""
import copy
import statistics

import numpy as np

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature import feature


class MaxProjectionHorizontalFeature(feature.Feature):
    """
    Klasa oblicza numer wiersza, którego projekcja ma największą wartość.
    Cecha 25.
    """

    def __init__(self):
        self.__rowsSum = None

    def calculate(self) -> float:
        if self.__rowsSum is None:
            raise RuntimeError("Run prepare() before calculate()")
        return self.__rowsSum.argmax()

    def prepare(self, bitmap: BitmapGrayscale) -> None:
        self.__rowsSum = np.zeros(bitmap.get_height())
        for i in range(bitmap.get_height()):
            self.__rowsSum[i] = bitmap.get_row(i).sum()
