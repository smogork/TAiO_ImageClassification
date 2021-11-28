#! /usr/bin/env python3

"""
Modul zawiera testy klasy LongestNonEmptyRowFeature
"""

import unittest

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.simple_features.longest_non_empty_row_feature import LongestNonEmptyRowFeature
from tests.bitmap_generator import BitmapGenerator


class TestLongestNonEmptyRowFeature(unittest.TestCase):
    """
    Klasa testująca klase LongestNonEmptyColumnFeature
    """
    def setUp(self):
        self.feature = LongestNonEmptyRowFeature(0.05)

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
        Oczekujemy zgłoszenia wyjątku AttributeError.
        :return:
        """
        with self.assertRaises(AttributeError):
            self.feature.calculate()

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
        Oczekujemy Liczby 1 jako informacji o jednym niepustym wierszu.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(1, 1, 0.5)

        res = self.count_feature(bitmap)

        self.assertAlmostEqual(1.0, res)

    def test_two_non_empty_rows(self):
        """
        Dostarczamy bitmapę wypełniona tylko czarnym kolorem, oprócz jednego dwóch białych pikseli w różnych wierszach.
        Oczekujemy Liczby 1 jako informacji o najdłuższym niepustym wierszu.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(1, 1, 0.5)
        bitmap.set_cell_value(1, 2, 0.5)

        res = self.count_feature(bitmap)

        self.assertEqual(1, res)

    def test_two_values_in_one_row(self):
        """
        Dostarczamy bitmapę wypełniona tylko czarnym kolorem, oprócz dwóch białych pikseli w jednym wierszu obok siebie.
        Oczekujemy Liczby 2 jako informacji o najdłuższym niepustym wierszu.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(1, 1, 1.0)
        bitmap.set_cell_value(2, 1, 1.0)

        res = self.count_feature(bitmap)

        self.assertEqual(2, res)

    def test_two_values_in_one_row_but_with_space(self):
        """
        Dostarczamy bitmapę wypełniona tylko czarnym kolorem, oprócz dwóch białych pikseli w jednym wierszu nie obok siebie.
        Oczekujemy Liczby 1 jako informacji o najdłuższym niepustym wierszu.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(1, 1, 1.0)
        bitmap.set_cell_value(3, 1, 1.0)

        res = self.count_feature(bitmap)

        self.assertEqual(1, res)

