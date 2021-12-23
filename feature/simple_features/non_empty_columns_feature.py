#! /usr/bin/env python

"""
Moduł zawiera klasę wyliczajcą najdłuższą pustą kolumnę na obrazku w skali szarości
"""

import copy

from bitmap import bitmap_grayscale
from feature import feature


class NonEmptyColumnsFeature(feature.Feature):
    """
    Klasa oblicza liczbę niepustych kolumn.
    Cecha 5.
    POdajemy threashold blisko bialego
    """

    def __init__(self, threshold: float):
        self.__bitmap = None
        self.__threshold = threshold

    def calculate(self) -> float:
        count = 0
        for i in range(self.__bitmap.get_height()):
            for j in range(self.__bitmap.get_width()):
                if self.__bitmap.get_cell_value(j, i) >= self.__threshold:
                    count += 1
                    break
        return count

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__bitmap = copy.deepcopy(bitmap)
