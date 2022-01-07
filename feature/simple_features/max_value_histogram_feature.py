#! /usr/bin/env python

"""
Moduł zawiera klasę wyliczajcą minimalna wartość koloru obrazka w skali szarości
"""
import numpy as np
from bitmap.bitmap_grayscale import BitmapGrayscale
from feature import feature
from bitmap import bitmap_grayscale


class MaxValueHistogramFeature(feature.Feature):
    """
    Klasa oblicza podaje najmniejszy numer komórki, która nie jest biała.
    Cecha 3.
    """

    def __init__(self):
        self.__tab = None

    def calculate(self) -> float:
        if self.__tab is None or len(self.__tab) == 0:
            raise RuntimeError("Run prepare() before calculate()")

        return self.__tab.max()

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__tab = np.zeros(256)
        for i in range(bitmap.get_width()):
            for j in range(bitmap.get_height()):
                self.__tab[int(bitmap.get_cell_value(i, j)*255)] += 1
