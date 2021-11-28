#! /usr/bin/env python3

"""
Moduł zawiera klasę wyliczajcą liczbę dziur na obrazku w skali szarości
"""
import copy

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature import feature
from bitmap import bitmap_grayscale


class NumberOfIslandsFeature(feature.Feature):
    """
    Klasa oblicza liczbę wysp.
    Cecha 8.
    """

    def __init__(self, threshold: float):
        """
        Threshold tyczy sie
        """
        self.__bitmap = None
        self.__threshold = threshold

    def calculate(self) -> float:
        count = 0
        for i in range(self.__bitmap.get_width()):
            for j in range(self.__bitmap.get_height()):
                if self.__bitmap.get_cell_value(i, j) >= self.__threshold:
                    count += 1
                    self.flood(i, j)
                    break
        return count

    def flood(self, i: int, j: int):
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
        self.__bitmap.set_cell_value(i, j, BitmapGrayscale.White)
        self.flood(i - 1, j)
        self.flood(i + 1, j)
        self.flood(i, j - 1)
        self.flood(i, j + 1)

    def prepare(self, bitmap: bitmap_grayscale) -> None:
        # KS: To jets ważne! Nie zapominajmy o tym przypadkiem.
        self.__bitmap = copy.deepcopy(bitmap)
