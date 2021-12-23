#! /usr/bin/env python

"""
Moduł zaiwera abstrakcyjną klasę reprezentująca funkcje wylczjącą właściwość
przekazanego obrazu
"""

import abc
import numpy as np
from numpy import ndarray

from bitmap.bitmap_grayscale import BitmapGrayscale


class Feature(metaclass=abc.ABCMeta):
    """
    Klasa abstrakcyjna opisująca dowolne wyciagniecie właściwości obrazu
    Z Założenia jest to pewna funkcja z obrazów w skali szarości do liczb rzeczywistych.
    """

    @abc.abstractmethod
    def calculate(self) -> float:
        """
        Metoda wyznaczająca wartość właściwości.

        :raise RuntimeError: W przypadku, gdy nie zostala wykonana wczesniej metoda prepare
        :return:
        Wartość reprezentująca wynikową właściwość
        """

    @abc.abstractmethod
    def prepare(self, bitmap: BitmapGrayscale) -> None:
        """
        Metoda przygotowuje wejściową bitmpae w skali szarości do wyznaczenia implementowanej
        właściwości.
        Uwaga: Należy wykonac ta metodę przed calculate. Wpw metoda calculate
        powinna rzucać wyjątek RuntimeError.

        :param bitmap: Bitmapa, z której nastapi wyznaczenie właściwości w metodzie calculate
        """

    def _map_bitmap_to_single_dimention(self, bitmap: BitmapGrayscale) -> ndarray:
        tab = np.zeros(bitmap.get_height() * bitmap.get_width())
        for i in range(bitmap.get_width()):
            for j in range(bitmap.get_height()):
                tab[i * bitmap.get_width() + j] = bitmap.get_cell_value(i, j)
        return tab
