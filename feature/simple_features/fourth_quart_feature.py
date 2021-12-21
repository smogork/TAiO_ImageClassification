#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczajcą liczbę punktów o wartościach (3/4, 1]
"""

import copy

from feature import feature
from bitmap import bitmap_grayscale


class FourthQuartFeature(feature.Feature):
    """
    Klasa oblicza .
    Cecha 21.
    """

    def __init__(self):
        self.__points = None

    def calculate(self) -> float:
        if self.__points is None:
            raise RuntimeError("Run prepare() before calculate()")

        count = 0
        for x in self.__points:
            if 0.75 < x:
                count += 1
        return count

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__points = super()._map_bitmap_to_single_dimention(bitmap)
