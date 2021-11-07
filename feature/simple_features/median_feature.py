#! /usr/bin/env python3

from feature import feature
from bitmap import bitmap_grayscale
import statistics


class MedianFeature(feature.Feature):
    """
    Klasa oblicza medianę z kolorów komórek.
    Cecha 1.
    """

    def __init__(self):
        self.__tab = []

    def calculate(self) -> float:
        return statistics.median(self.__tab)

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        for i in range(bitmap.get_width()):
            for j in range(bitmap.get_height()):
                self.__tab.append(bitmap.get_cell_value(i, j))
