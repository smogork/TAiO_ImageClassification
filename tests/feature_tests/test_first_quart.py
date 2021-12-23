#! /usr/bin/env python

"""
Modul zawiera testy klasy FirstQuartFeature
"""

import unittest

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.simple_features.first_quart_feature import FirstQuartFeature
from tests.bitmap_generator import BitmapGenerator


class TestFirstQuartFeature(unittest.TestCase):
    """
    Klasa testująca klase FirstQuartFeature
    """
    def setUp(self):
        self.feature = FirstQuartFeature()

    def count_feature(self, bitmap: BitmapGrayscale) -> float:
        """
        Prawidłowow wylicza wartośc feature
        :param bitmap: Bitmapa, dla której wyliczamy feature
        :return: Wyliczony feature
        """
        self.feature.prepare(bitmap)
        return self.feature.calculate()

    def test_black_plain(self):
        """
        Test sprawddza ilość pikseli w pierwszej ćwiartce w obrazie czarnym rozmiaru 5 x 5.
        Oczekujemy 25, czyli rozmiaru obrazu.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)

        res = self.count_feature(bitmap)

        self.assertIs(25, res)

    def test_white_plain_with_one_pixel_black(self):
        """
        Test sprawddza ilość pikseli w pierwszej ćwiartce w obrazie białym rozmiaru 5 x 5 z jednym czarnym pikselem.
        Oczekujemy 1, czyli ilości czarnych pikseli.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_white(size, size)
        bitmap.set_cell_value(0, 1, 0.0)

        res = self.count_feature(bitmap)

        self.assertIs(1, res)


