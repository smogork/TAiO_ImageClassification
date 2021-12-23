#! /usr/bin/env python

"""
Modul zawiera testy klasy MedianFeature
"""

import unittest
from statistics import StatisticsError

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.simple_features.median_feature import MedianFeature
from tests.bitmap_generator import BitmapGenerator


class TestMedianFeature(unittest.TestCase):
    """
    Klasa testująca klase MedianFeature
    """
    def setUp(self):
        self.feature = MedianFeature()

    def count_feature(self, bitmap: BitmapGrayscale) -> float:
        """
        Prawidłowo wylicza wartość feature
        :param bitmap: Bitmapa, dla której wyliczamy feature
        :return: Wyliczony feature
        """
        self.feature.prepare(bitmap)
        return self.feature.calculate()

    def test_reorder_calculate_prepare(self):
        """
        Test sprawdza, czy wywołanie w złej kolejności metody prepare i calculate zgłaszaja wyjątek.
        Oczekujemy zgłoszenia wyjątku StatisticsError.
        :return:
        """
        with self.assertRaises(StatisticsError):
            self.feature.calculate()