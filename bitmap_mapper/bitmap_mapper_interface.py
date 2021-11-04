#! /usr/bin/env python3

"""
W module istnieje klasa reprezentująca abstrakcyjna metode przeksztalcajaca
ciag do bitmapy w skali szarosci
"""

import abc
import typing

from bitmap.bitmap_grayscale import BitmapGrayscale


class BitmapMapperInterface(metaclass=abc.ABCMeta):
    """
    Interfejs reprezentujący wszystkei sposoby przetworzenia ciągu liczb
    na obrazek w skali szarości.
    Obrazek będzie kwadratowy o ustalonej szerokości.
    """

    @abc.abstractmethod
    def convert_series(self, series: typing.List[float]) -> BitmapGrayscale:
        """
        Metoda powinna przetworzyć pewien ciąg liczbowy na obrazek w skali szarości.

        :raise RuntimeError: W przypadku, gdy nie zostala wykonana wczesniej
         metoda set_bitmap_size
        :param series: Ciąg danych liczbowych
        :return: Zwraca BitmapGrayscale przechowującą obrazek wygenerowany
        w pewien sposób z ciągu wejściowego.
        """

    @abc.abstractmethod
    def set_bitmap_size(self, bitmap_size: int) -> None:
        """
        Metoda powinna byc uzyta do konfiguracji rozmiaru bitmapy wynikowej.
        Wynikowa bitmapa powinna byc rozmiaru podanego w tej metodzie.
        Gdy nie zostanie ona wykonana przed convert_series,
        powinien zostac wyrzucony wyjatek RuntimeError.

        :param bitmap_size: Szerokośc i wysokość bitmapy (jedna liczba)
        """
