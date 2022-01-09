#! /usr/bin/env python

"""
Modul zawiera testy klasy MaxHistogramFeature
"""

import unittest

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.simple_features.max_value_histogram_feature import MaxValueHistogramFeature
from tests.bitmap_generator import BitmapGenerator


class TestMaxValueHistogramFeature(unittest.TestCase):
    """
    Klasa testująca klase MaxHistogramFeature
    """
    def setUp(self):
        self.feature = MaxValueHistogramFeature()

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
        with self.assertRaises(RuntimeError):
            self.feature.calculate()

    def test_same_color(self):
        """
        Dostarczamy bitmapę wypełniona tym samym kolorem
        :return:
        """
        color = 0.5
        size = 3

        bitmap = BitmapGenerator.plain_color(size, size, color)

        res = self.count_feature(bitmap)

        self.assertAlmostEqual(9, res)

    def test_one_pixel_different_color(self):
        """
        Dostarczamy bitmapę wypełniona tym samym kolorem, poza jednym kolorem
        :return:
        """
        color = 0.5
        size = 3

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(1, 1, color)

        res = self.count_feature(bitmap)

        self.assertAlmostEqual(8, res)

