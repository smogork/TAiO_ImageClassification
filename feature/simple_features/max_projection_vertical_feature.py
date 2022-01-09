#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczającą numer kolumny, którego projekcja ma największą wartość.
"""
import copy
import statistics

import numpy as np

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature import feature
from bitmap import bitmap_grayscale


class MaxProjectionVerticalFeature(feature.Feature):
    """
    Klasa oblicza numer kolumny, którego projekcja ma największą wartość.
    Cecha 23.
    """

    def __init__(self):
        self.__columnsSum = None

    def calculate(self) -> float:
        if self.__columnsSum is None:
            raise RuntimeError("Run prepare() before calculate()")
        return self.__columnsSum.argmax()

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__columnsSum = np.zeros(bitmap.get_width())
        for i in range(bitmap.get_width()):
            self.__columnsSum[i] = bitmap.get_column(i).sum()
