#! /usr/bin/env python3

"""
Modul zawiera testy klasy ThirdQuartFeature
"""

import unittest

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.simple_features.third_quart_feature import ThirdQuartFeature
from tests.bitmap_generator import BitmapGenerator


class TestThirdQuartFeature(unittest.TestCase):
    """
    Klasa testująca klase ThirdQuartFeature
    """
    def setUp(self):
        self.feature = ThirdQuartFeature()

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
        Test sprawddza ilość pikseli w pierwszej ćwiartce w obrazie prawie białym rozmiaru 5 x 5.
        Oczekujemy 25, czyli rozmiaru obrazu.
        :return:
        """
        size = 5
        color = 0.51

        bitmap = BitmapGenerator.plain_color(size, size, color)

        res = self.count_feature(bitmap)

        self.assertIs(25, res)

    def test_white_plain_with_one_pixel_black(self):
        """
        Test sprawddza ilość pikseli w pierwszej ćwiartce w obrazie białym rozmiaru 5 x 5 z jednym prawie białym pikselem.
        Oczekujemy 1, czyli ilości czarnych pikseli.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_white(size, size)
        bitmap.set_cell_value(0, 1, 0.51)

        res = self.count_feature(bitmap)

        self.assertIs(1, res)


