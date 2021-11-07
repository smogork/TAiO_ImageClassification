#! /usr/bin/env python3

from feature import feature
from bitmap import bitmap_grayscale
import statistics


class MeanFeature(feature.Feature):
    """
    Klasa oblicza średni kolor komórki.
    Cecha 2.
    """

    def __init__(self):
        self.__tab = []

    def calculate(self) -> float:
        return statistics.mean(self.__tab)

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        for i in range(bitmap.get_width()):
            for j in range(bitmap.get_height()):
                self.__tab.append(bitmap.get_cell_value(i, j))