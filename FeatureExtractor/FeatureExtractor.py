#! /usr/bin/env python3

import typing

from Bitmap import BitmapGrayscale
from Feature.Feature import Feature


class FeatureExtractor:
    """
    Klasa zajmująca się wyznaczenie wszystkich właściwości z obrazka w skali szarości.
    """
    def __init__(self):
        self.__features = typing.List[Feature]

    def add_feature(self, feature: Feature) -> None:
        """
        Metoda słuzy do dodawania właściwości, które mają byc wyznaczone z obrazów w skali szarości.
        :param feature: Obiekt reprezentujący pewną funkcje wyznaczania właściwości.
        """
        self.__features.append(feature)

    def calculate_features(self, bitmap: BitmapGrayscale) -> typing.List[float]:
        """
        Metoda wyznacza wszystkie właściwości dodane wczesniej z obrazka podanego w argumencie.
        :param bitmap: Obraz w skali szarości, z którego będzie wyznaczony zbiór właściwości.
        :return: Lista wyliczonych właściwości.
        """
        result = []
        for feature in self.__features:
            feature.prepare(bitmap)
            result.append(feature.calculate())
        return result
        