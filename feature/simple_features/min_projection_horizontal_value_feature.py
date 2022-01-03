#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczającą numer kolumny, którego projekcja ma najmniejszą wartość.
"""
import copy
import statistics

import numpy as np

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature import feature
from bitmap import bitmap_grayscale


class MinProjectionHorizontalValueFeature(feature.Feature):
    """
    Klasa oblicza numer kolumny, którego projekcja ma najmniejszą wartość.
    Cecha .
    """

    def __init__(self):
        self.__rowsSum = None

    def calculate(self) -> float:
        if self.__rowsSum is None:
            raise RuntimeError("Run prepare() before calculate()")
        return self.__rowsSum.min()

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__rowsSum = np.zeros(bitmap.get_height())
        for i in range(bitmap.get_height()):
            self.__rowsSum[i] = bitmap.get_row(i).sum()
