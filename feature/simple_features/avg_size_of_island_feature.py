#! /usr/bin/env python

"""
Moduł zawiera klasę wyliczajcą średni rozmiar wysp na obrazku w skali szarości
"""

import copy

from feature import feature
from bitmap import bitmap_grayscale


class AvgSizeOfIslandFeature(feature.Feature):
    """
    Klasa oblicza średni rozmiar wysp.
    Cecha 17.
    """

    def __init__(self, threshold: float):
        self.__bitmap = None
        self.__threshold = threshold
        self.__totalSize = 0

    def calculate(self) -> float:
        count = 0.0
        self.__totalSize = 0.0
        for i in range(self.__bitmap.get_width()):
            for j in range(self.__bitmap.get_height()):
                if self.__bitmap.get_cell_value(i, j) >= self.__threshold:
                    count += 1
                    self.flood(i, j)
                    break
        if count == 0:
            return -1
        return self.__totalSize/count

    def flood(self, i: int, j: int) -> None:
        """
        Metoda implementuje algorytm zalewania od punktu o wybranych współrzędnych
        :param i: Indeks kolumny
        :param j: Indeks wiersza
        """
        if i < 0 or i >= self.__bitmap.get_width():
            return
        if j < 0 or j >= self.__bitmap.get_height():
            return
        if self.__bitmap.get_cell_value(i, j) < self.__threshold:
            return
        self.__bitmap.set_cell_value(i, j, 0.0)#Ustawiamy wartość na 0, żeby pokazać że piksel policzony
        self.flood(i - 1, j)
        self.flood(i + 1, j)
        self.flood(i, j - 1)
        self.flood(i, j + 1)
        self.__totalSize += 1

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        self.__bitmap = copy.deepcopy(bitmap)
