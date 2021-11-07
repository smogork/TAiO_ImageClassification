#! /usr/bin/env python3

from feature import feature
from bitmap import bitmap_grayscale
import statistics
import copy


class NumberOfIslandsFeature(feature.Feature):
    """
    Klasa oblicza liczbę dziur.
    Cecha 7.
    """

    def __init__(self, treshold: float):
        self.__bitmap = None
        self.__treshold = treshold

    def calculate(self) -> float:
        count = 0
        for i in range(self.__bitmap.get_width()):
            for j in range(self.__bitmap.get_height()):
                if self.__bitmap.get_cell_value(i, j) < self.__treshold:
                    count += 1
                    self.flood(i, j)
                    break
        return count

    def flood(self, i: int, j: int):
        if i < 0 or i > self.__bitmap.get_width():
            return
        if j < 0 or j > self.__bitmap.get_height():
            return
        if self.__bitmap.get_cell_value(i, j) >= self.__treshold:
            return
        self.__bitmap.set_cell_value = -1
        self.flood(i - 1, j)
        self.flood(i + 1, j)
        self.flood(i, j - 1)
        self.flood(i, j + 1)

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__bitmap = copy.deepcopy(bitmap)
