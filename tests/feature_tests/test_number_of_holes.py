#! /usr/bin/env python3

"""
Modul zawiera testy klasy NumberOfHolesFeature
"""

import unittest

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.simple_features.number_of_holes_feature import NumberOfHolesFeature
from tests.bitmap_generator import BitmapGenerator


class TestNumberOfHolesFeature(unittest.TestCase):
    """
    Klasa testująca klase MinFeature
    """
    def setUp(self):
        self.feature = NumberOfHolesFeature(0.5)

    def count_feature(self, bitmap: BitmapGrayscale) -> float:
        """
        Prawidłowow wylicza wartośc feature
        :param bitmap: Bitmapa, dla której wyliczamy feature
        :return: Wyliczony feature
        """
        self.feature.prepare(bitmap)
        return self.feature.calculate()

    def test_reorder_calculate_prepare(self):
        """
        Test sprawdza, czy wywołanie w złej kolejności metody prepare i calculate zgłaszaja wyjątek.
        Oczekujemy zgłoszenia wyjątku RuntimeError.
        :return:
        """
        with self.assertRaises(AttributeError):
            self.feature.calculate()

