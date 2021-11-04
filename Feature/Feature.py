#! /usr/bin/env python3

import abc
import typing
from Bitmap import BitmapGrayscale


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
        pass

    @abc.abstractmethod
    def prepare(self, bitmap: BitmapGrayscale) -> None:
        """
        Metoda przygotowuje wejściową bitmpae w skali szarości do wyznaczenia implementowanej właściwości.
        Uwaga: Należy wykonac ta metodę przed calculate. Wpw metoda calculate powinna rzucać wyjątek RuntimeError.

        :param bitmap: Bitmapa, z której nastapi wyznaczenie właściwości w metodzie calculate
        """
        pass
