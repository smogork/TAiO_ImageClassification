#! /usr/bin/env python3

from feature import feature
from bitmap import bitmap_grayscale
import statistics
import copy


class LongestNonEmptyDiagonalFeature(feature.Feature):
    """
    Klasa oblicza .
    Cecha 11.
    """

    def __init__(self, threshold: float):
        self.__bitmap = None
        self.__startingPoints = []
        self.__threshold = threshold

    def calculate(self) -> float:
        count = 0
        for x in self.__startingPoints:
            length = 0
            i = x[0]
            j = x[1]
            while self.in_bounds(i, j):
                if self.__bitmap.get_cell_value(i, j) >= self.__threshold:
                    length += 1
                    i += 1
                    j += 1
                    continue
                if length > count:
                    count = length
                length = 0
                i += 1
                j += 1
            if length > count:
                count = length
        return count

    def in_bounds(self, i: int, j: int):
        if i < 0 or i >= self.__bitmap.get_width():
            return False
        if j < 0 or j >= self.__bitmap.get_height():
            return False
        return True

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__bitmap = copy.deepcopy(bitmap)
        for i in range(self.__bitmap.getWidth()):
            self.__startingPoints.append((0, i))
        for i in range(self.__bitmap.getHeight()):
            self.__startingPoints.append((i, 0))
