#! /usr/bin/env python

"""
Modul zawiera testy klasy FourthQuartFeature
"""

import unittest

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.simple_features.fourth_quart_feature import FourthQuartFeature
from tests.bitmap_generator import BitmapGenerator


class TestFourthQuartFeature(unittest.TestCase):
    """
    Klasa testująca klase FourthQuartFeature
    """
    def setUp(self):
        self.feature = FourthQuartFeature()

    def count_feature(self, bitmap: BitmapGrayscale) -> float:
        """
        Prawidłowow wylicza wartośc feature
        :param bitmap: Bitmapa, dla której wyliczamy feature
        :return: Wyliczony feature
        """
        self.feature.prepare(bitmap)
        return self.feature.calculate()

    def test_color_plain(self):
        """
        Test sprawddza ilość pikseli w czwartej ćwiartce w obrazie  białym rozmiaru 5 x 5.
        Oczekujemy 25, czyli rozmiaru obrazu.
        :return:
        """
        size = 5
        color = 0.8

        bitmap = BitmapGenerator.plain_color(size, size, color)

        res = self.count_feature(bitmap)

        self.assertIs(25, res)

    def test_color_plain_with_one_pixel_black(self):
        """
        Test sprawddza ilość pikseli w czwartej ćwiartce w obrazie czarnym rozmiaru 5 x 5 z jednym prawie białym pikselem.
        Oczekujemy 1, czyli ilości czarnych pikseli.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(0, 1, 0.81)

        res = self.count_feature(bitmap)

        self.assertIs(1, res)


