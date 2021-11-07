#! /usr/bin/env python3

from feature import feature
from bitmap import bitmap_grayscale
import statistics
import copy


class NonEmptyColumnsFeature(feature.Feature):
    """
    Klasa oblicza liczbę niepustych kolumn.
    Cecha 5.
    """

    def __init__(self):
        self.__bitmap = None

    def calculate(self) -> float:
        count = 0
        for i in range(self.__bitmap.get_width()):
            for j in range(self.__bitmap.get_height()):
                if self.__bitmap.get_cell_value(i, j) > 0:
                    count += 1
                    break

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__bitmap = copy.deepcopy(bitmap)