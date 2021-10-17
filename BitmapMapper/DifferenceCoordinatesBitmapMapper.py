#! /usr/bin/env python3

import typing
import numpy as np

from BitmapMapper.BitmapMapperInterface import BitmapMapperInterface
from Bitmap.BitmapGrayscale import BitmapGrayscale
from Bitmap.BitmapGrayscaleCounter import BitmapGrayscaleCounter


class DifferenceCoordinatesBitmapMapper(BitmapMapperInterface):
    """
    Klasa przetwarza ciag na bitmape za pomocą współrzednych wyznaczonych z pierwszej różnicy i danych wejściowych.
    Niech ciąg ma n elementów. Wtedy otrzymamy n-1 par (x_i, dx_i), które traktujemy jak wspólrzędne w bitmapie.
    Zliczamy takie punkty w każdym pixelu i ten największą liczba będzie czarny.
    """

    def __init__(self):
        self.__size = None

    def convert_series(self, series: typing.List[float]) -> BitmapGrayscale:
        """
        Metoda powinna przetworzyć pewien ciąg liczbowy na obrazek w skali szarości.

        :raise RuntimeError: W przypadku, gdy nie zostala wykonana wczesniej metoda set_bitmap_size
        :param series: Ciąg danych liczbowych
        :return: Zwraca BitmapGrayscale przechowującą obrazek wygenerowany w pewien sposób z ciągu wejściowego.
        """

        if self.__size is None:
            raise RuntimeError("Call set_bitmap_size to set bitmap size before this method.")

        counters = BitmapGrayscaleCounter(self.__size, self.__size)

        #Wyliczenie rożnic i wspólrzędnych
        x = np.array(series)
        dx = x[1:] - x[:-1]
        coordinates = np.array((x[1:], dx)).T

        #Policzenie wystapień
        for (x, y) in coordinates:
            counters.increment_cell(round(x), round(y))

        return counters.convert_to_BitmapGrayscale()


    def set_bitmap_size(self, bitmap_size: int) -> None:
        """
        Metoda powinna byc uzyta do konfiguracji rozmiaru bitmapy wynikowej.
        Wynikowa bitmapa powinna byc rozmiaru podanego w tej metodzie.
        Gdy nie zostanie ona wykonana przed ConvertSeries, powinien zostac wyrzucony wyjatek RuntimeError.

        :param bitmap_size: Szerokośc i wysokość bitmapy (jedna liczba)
        """
        self.__size = bitmap_size