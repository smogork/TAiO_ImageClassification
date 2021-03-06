#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczającą sumę kolumny, którego projekcja ma najmniejszą wartość.
"""
import copy
import statistics

import numpy as np

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature import feature
from bitmap import bitmap_grayscale


class MinProjectionVerticalValueFeature(feature.Feature):
    """
    Klasa oblicza sumę kolumny, którego projekcja ma najmniejszą wartość.
    Cecha .
    """

    def __init__(self):
        self.__columnsSum = None

    def calculate(self) -> float:
        if self.__columnsSum is None:
            raise RuntimeError("Run prepare() before calculate()")
        return self.__columnsSum.min()

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__columnsSum = np.zeros(bitmap.get_width())
        for i in range(bitmap.get_width()):
            self.__columnsSum[i] = bitmap.get_column(i).sum()
