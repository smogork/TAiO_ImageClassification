#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczającą numer kolumny, którego projekcja ma największa wartość.
"""
import copy
import statistics

import numpy as np

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature import feature
from bitmap import bitmap_grayscale


class MaxProjectionVerticalValueFeature(feature.Feature):
    """
    Klasa oblicza sumę kolumny, którego projekcja ma największą wartość.
    Cecha 24.
    """

    def __init__(self):
        self.__columnsSum = None

    def calculate(self) -> float:
        if self.__columnsSum is None:
            raise RuntimeError("Run prepare() before calculate()")
        return self.__columnsSum.max()

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__columnsSum = np.zeros(bitmap.get_width())
        for i in range(bitmap.get_width()):
            self.__columnsSum[i] = bitmap.get_column(i).sum()
