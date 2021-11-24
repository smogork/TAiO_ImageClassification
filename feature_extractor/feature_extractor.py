#! /usr/bin/env python3

"""
Moduł zawiera klasę definiującą zbiór właściwości.
"""

import typing
from multiprocessing import Pool

from bitmap import bitmap_grayscale
from feature.feature import Feature


class FeatureExtractor:
    """
    Klasa zajmująca się wyznaczenie wszystkich właściwości z obrazka w skali szarości.
    """

    def __init__(self):
        self.__features = []

    def feature_count(self) -> int:
        """
        Zwraca informacje o liczbie zaincjalizowanych featurow
        """
        return len(self.__features)

    def add_feature(self, feature: Feature) -> None:
        """
        Metoda słuzy do dodawania właściwości, które mają byc wyznaczone z obrazów w skali szarości.
        :param feature: Obiekt reprezentujący pewną funkcje wyznaczania właściwości.
        """
        self.__features.append(feature)

    def calculate_features(self, bitmap: bitmap_grayscale) -> typing.List[float]:
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

    def calculate_features_mp(self,
                              bitmap: bitmap_grayscale,
                              thread_number: int)\
            -> typing.List[float]:
        """
        Metoda wyznacza wszystkie właściwości dodane wczesniej z obrazka podanego w argumencie.
        Metoda wykorzystuje pulę procesów.
        :param bitmap: Obraz w skali szarości, z którego będzie wyznaczony zbiór właściwości.
        :param thread_number: Liczba wątków uruchomionych do obliczeń
        :return: Lista wyliczonych właściwości.
        """
        def process_function(__feature: Feature) -> float:
            __feature.prepare(bitmap)
            return __feature.calculate()

        result = []
        with Pool(processes=thread_number) as pool:
            result = pool.map(process_function, self.__features)

        return result
