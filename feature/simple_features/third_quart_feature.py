#! /usr/bin/env python

"""
Moduł zawiera klasę wyliczajcą liczbę punktów o wartościach (2/4, 3/4]
"""

import copy

import numpy as np

from feature.feature import Feature
from bitmap import bitmap_grayscale


class ThirdQuartFeature(Feature):
    """
    Klasa oblicza .
    Cecha 20.
    """

    def __init__(self):
        self.__points = None

    def calculate(self) -> float:
        if self.__points is None:
            raise RuntimeError("Run prepare() before calculate()")

        count = 0
        for x in self.__points:
            if 0.5 < x <= 0.75:
                count += 1
        return count

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__points = super()._map_bitmap_to_single_dimention(bitmap)
