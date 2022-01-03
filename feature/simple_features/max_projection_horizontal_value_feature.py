#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczającą kolumnę, którego projekcja ma najmniejszą wartość.
"""
import copy
import statistics

import numpy as np

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature import feature
from bitmap import bitmap_grayscale


class MaxProjectionHorizontalValueFeature(feature.Feature):
    """
    Klasa oblicza kolumnę, którego projekcja ma najmniejszą wartość.
    Cecha .
    """

    def __init__(self):
        self.__columnsSum = None

    def calculate(self) -> float:
        if self.__columnsSum is None:
            raise RuntimeError("Run prepare() before calculate()")
        return self.__columnsSum.max()

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__columnsSum = np.zeros(bitmap.get_height())
        for i in range(bitmap.get_height()):
            self.__columnsSum[i] = bitmap.get_row(i).sum()
