#! /usr/bin/env python

"""
Moduł zawiera klasę definiującą zbiór właściwości.
"""

import typing
from multiprocessing import Pool

import numpy
import numpy as np
from itertools import repeat

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.feature import Feature

import pickle


class FeatureExtractor:
    """
    Klasa zajmująca się wyznaczenie wszystkich właściwości z obrazka w skali szarości.
    """

    def __init__(self):
        self.__features = []
        self.__activeFeatures = []
        self.__ignoredFeaturesFileName = "ignored_features"

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

    def calculate_features(self, bitmap: BitmapGrayscale) -> np.ndarray:
        """
        Metoda wyznacza wszystkie właściwości dodane wczesniej z obrazka podanego w argumencie.
        :param bitmap: Obraz w skali szarości, z którego będzie wyznaczony zbiór właściwości.
        :return: Lista wyliczonych właściwości.
        """
        result = np.zeros((1, self.feature_count()))
        i = 0
        for feature in self.__features:
            feature.prepare(bitmap)
            result[:, i] = feature.calculate()
            i += 1
        return result

    def process_function(self, feature: Feature, bitmap: BitmapGrayscale) -> float:
        feature.prepare(bitmap)
        return feature.calculate()

    def calculate_features_mp(self,
                              bitmap: BitmapGrayscale,
                              thread_number: int)\
            -> typing.List[float]:
        """
        Metoda wyznacza wszystkie właściwości dodane wczesniej z obrazka podanego w argumencie.
        Metoda wykorzystuje pulę procesów.
        :param bitmap: Obraz w skali szarości, z którego będzie wyznaczony zbiór właściwości.
        :param thread_number: Liczba wątków uruchomionych do obliczeń
        :return: Lista wyliczonych właściwości.
        """
        result = []
        with Pool(processes=thread_number) as pool:
            result = pool.starmap(self.process_function,  zip(self.__features, repeat(bitmap)))

        return result

    def SetActiveFeatures(self, mask):
        i=0
        for feature in self.__features:
            if mask[i] == False:
                self.__activeFeatures.append(feature)
            i+=1

    def GetActiveFeaturesNames(self):
        names = []
        for feature in self.__activeFeatures:
            names.append(feature.GetName())
        return names

    def GetFeaturesNames(self):
        names = []
        for feature in self.__features:
            names.append(feature.GetName())
        return names
