#! /usr/bin/env python

"""
Modul zawiera testy klasy LongestNonEmptyAntidiagonalFeature
"""

import unittest

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.simple_features.longest_non_empty_antidiagonal_feature import LongestNonEmptyAntidiagonalFeature
from tests.bitmap_generator import BitmapGenerator


class TestLongestNonEmptyAntidiagonalFeature(unittest.TestCase):
    """
    Klasa testująca klase LongestNonEmptyAntidiagonalFeature
    """
    def setUp(self):
        self.feature = LongestNonEmptyAntidiagonalFeature(0.05)

    def count_feature(self, bitmap: BitmapGrayscale) -> float:
        """
        Prawidłowo wylicza wartośc feature
        :param bitmap: Bitmapa, dla której wyliczamy feature
        :return: Wyliczony feature
        """
        self.feature.prepare(bitmap)
        return self.feature.calculate()

    def test_empty(self):
        """
        Dostarczamy bitmapę wypełniona tylko czarnym kolorem.
        Oczekujemy Liczby 0 jako informacji o braku wartości.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)

        res = self.count_feature(bitmap)

        self.assertAlmostEqual(0.0, res)

    def test_one_non_empty(self):
        """
        Dostarczamy bitmapę wypełniona tylko czarnym kolorem, oprócz jednego białego piksela.
        Oczekujemy Liczby 1 jako informacji o jednej niepustej antydiagonali.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(1, 1, 0.5)

        res = self.count_feature(bitmap)

        self.assertAlmostEqual(1.0, res)

    def test_two_non_empty_diagonals(self):
        """
        Dostarczamy bitmapę wypełniona tylko czarnym kolorem, oprócz jednego dwóch białych pikseli w różnych antydiagonalach.
        Oczekujemy Liczby 1 jako informacji o najdłuższej niepustej antydiagonali.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(1, 1, 0.5)
        bitmap.set_cell_value(2, 1, 0.5)

        res = self.count_feature(bitmap)

        self.assertEqual(1, res)

    def test_two_values_in_one_diagonal(self):
        """
        Dostarczamy bitmapę wypełniona tylko czarnym kolorem, oprócz dwóch białych pikseli w jednej antydiagonali obok siebie.
        Oczekujemy Liczby 2 jako informacji o najdłuższej niepustej antydiagonali.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(0, 1, 1.0)
        bitmap.set_cell_value(1, 0, 1.0)

        res = self.count_feature(bitmap)

        self.assertEqual(2, res)

    def test_two_values_in_one_diagonal_but_with_space(self):
        """
        Dostarczamy bitmapę wypełniona tylko czarnym kolorem, oprócz dwóch białych pikseli w jednej antydiagonali nie obok siebie.
        Oczekujemy Liczby 1 jako informacji o najdłuższej niepustej antydiagonali.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(0, 2, 1.0)
        bitmap.set_cell_value(2, 0, 1.0)

        res = self.count_feature(bitmap)

        self.assertEqual(1, res)

