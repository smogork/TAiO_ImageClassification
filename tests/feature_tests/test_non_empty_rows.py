#! /usr/bin/env python3

"""
Modul zawiera testy klasy NonEmptyRowsFeature
"""

import unittest

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.simple_features.non_empty_rows_feature import NonEmptyRowsFeature
from tests.bitmap_generator import BitmapGenerator


class TestNonEmptyRowsFeature(unittest.TestCase):
    """
    Klasa testująca klase NumberOfHolesFeature
    """
    def setUp(self):
        self.feature = NonEmptyRowsFeature(0.05)

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

    def test_two_non_empty(self):
        """
        Dostarczamy bitmapę wypełniona tylko czarnym kolorem, oprócz jednego dwóch białych pikseli w różnych wierszach.
        Oczekujemy Liczby 2 jako informacji o dwóch niepustych wierszach.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(1, 1, 0.5)
        bitmap.set_cell_value(2, 1, 0.5)

        res = self.count_feature(bitmap)

        self.assertAlmostEqual(2.0, res)

    def test_two_non_empty(self):
        """
        Dostarczamy bitmapę wypełniona tylko czarnym kolorem, oprócz jednego dwóch białych pikseli w tym samym wierszu.
        Oczekujemy Liczby 1 jako informacji o jednym niepustym wierszu.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(1, 1, 0.5)
        bitmap.set_cell_value(1, 2, 0.5)

        res = self.count_feature(bitmap)

        self.assertAlmostEqual(1.0, res)

