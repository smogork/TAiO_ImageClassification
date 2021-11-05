#! /usr/bin/env python3

from feature import feature
from bitmap import bitmap_grayscale
import statistics


class MinFeature(feature.Feature):

    def __init__(self):
        self.__tab = []

    def calculate(self) -> float:
        i = 0
        for cell in self.__tab:
            if cell > 0:
                return i
            i += 1
        return i

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        for i in range(bitmap.get_height()):
            for j in range(bitmap.get_width()):
                self.__tab.append(bitmap.get_cell_value(i, j))
