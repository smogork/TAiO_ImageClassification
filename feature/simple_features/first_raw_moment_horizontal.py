#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczajcą pierwszy moment projekcji poziomej
"""

import copy
import statistics

import numpy as np

from feature.feature import Feature
from bitmap.bitmap_grayscale import BitmapGrayscale


class FirstRawMomentHorizontalFeature(Feature):
    """
    Klasa oblicza .
    Cecha 22.
    """

    def __init__(self):
        self.__rowsSum = None

    def calculate(self) -> float:
        if self.__rowsSum is None:
            raise RuntimeError("Run prepare() before calculate()")

        return self.__rowsSum.mean()

    def prepare(self, bitmap: BitmapGrayscale) -> None:
        self.__rowsSum = np.zeros(bitmap.get_height())
        for i in range(bitmap.get_height()):
            self.__rowsSum[i] = bitmap.get_row(i).sum()
