#! /usr/bin/env python

"""
Modul zawiera testy klasy FirstRawMomentVerticalFeature
"""

import unittest
from statistics import StatisticsError

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.simple_features.first_raw_moment_vertical import FirstRawMomentVerticalFeature
from tests.bitmap_generator import BitmapGenerator


class TestFirstRawMomentVerticalFeature(unittest.TestCase):
    """
    Klasa testująca klase FirstRawMomentVerticalFeature
    """
    def setUp(self):
        self.feature = FirstRawMomentVerticalFeature()

    def count_feature(self, bitmap: BitmapGrayscale) -> float:
        """
        Prawidłowo wylicza wartośc feature
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
        with self.assertRaises(RuntimeError):
            self.feature.calculate()

    def test_plain_black(self):
        """
        Test wylicza pierwszy moment projekcji poziomej dla czarnego obrazu.
        Oczekujemy wartości 0.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)

        res = self.count_feature(bitmap)

        self.assertAlmostEqual(0.0, res)

    def test_plain_white(self):
        """
        Test wylicza pierwszy moment projekcji poziomej dla białego obrazu rozmiaru 5 x 5.
        Oczekujemy wartości 5.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_white(size, size)

        res = self.count_feature(bitmap)

        self.assertAlmostEqual(5.0, res)

    def test_plain_black_with_pixel_white(self):
        """
        Test wylicza pierwszy moment projekcji poziomej dla czarnego obrazu rozmiaru 5 x 5 z jednym białym pikselem.
        Oczekujemy wartości 0.2.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(1, 1, 1.0)

        res = self.count_feature(bitmap)

        self.assertAlmostEqual(0.2, res)

    def test_plain_black_with_two_pixels_white_different_columns(self):
        """
        Test wylicza pierwszy moment projekcji poziomej dla czarnego obrazu rozmiaru 5 x 5 z dwoma białymi pikselami w różnych kolumnach.
        Oczekujemy wartości 0.2.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(1, 1, 1.0)
        bitmap.set_cell_value(2, 1, 1.0)

        res = self.count_feature(bitmap)

        self.assertAlmostEqual(0.4, res)

    def test_plain_black_with_two_pixels_white_same_column(self):
        """
        Test wylicza pierwszy moment projekcji poziomej dla czarnego obrazu rozmiaru 5 x 5 z dwoma białymi pikselami w tej samej kolumnie.
        Oczekujemy wartości 0.2.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(1, 1, 1.0)
        bitmap.set_cell_value(1, 2, 1.0)

        res = self.count_feature(bitmap)

        self.assertAlmostEqual(0.4, res)



