#! /usr/bin/env python

"""
Moduł zawiera klasę wyliczajcą numer  komórki, która nie jest biała
"""
import numpy as np

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.feature import Feature


class MaxFeature(Feature):
    """
    Klasa podaje największy numer komórki, która nie jest biała.
    Cecha 4.
    """

    def __init__(self):
        self.__tab = None

    def calculate(self) -> float:
        if self.__tab is None:
            raise RuntimeError("Run prepare() before calculate()")

        maximum = -1
        i = 0
        for cell in self.__tab:
            if cell < BitmapGrayscale.White:
                maximum = i
            i += 1
        return maximum

    def prepare(self, bitmap: BitmapGrayscale) -> None:
        self.__tab = super()._map_bitmap_to_single_dimention(bitmap)
