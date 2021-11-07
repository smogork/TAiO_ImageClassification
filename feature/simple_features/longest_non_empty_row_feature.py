#! /usr/bin/env python3

from feature import feature
from bitmap import bitmap_grayscale
import statistics
import copy


class LongestNonEmptyRowFeature(feature.Feature):
    """
    Klasa oblicza .
    Cecha 9.
    """

    def __init__(self, threshold: float):
        self.__bitmap = None
        self.__threshold = threshold

    def calculate(self) -> float:
        count = 0
        for j in range(self.__bitmap.get_height()):
            length = 0
            for i in range(self.__bitmap.get_width()):
                if self.__bitmap.get_cell_value(i, j) >= self.__threshold:
                    length += 1
                    continue
                if length > count:
                    count = length
                length = 0
            if length > count:
                count = length
        return count

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__bitmap = copy.deepcopy(bitmap)
