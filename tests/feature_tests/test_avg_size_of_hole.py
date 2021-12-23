#! /usr/bin/env python

"""
Modul zawiera testy klasy AvgSizeOfHoleFeature
"""

import unittest

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.simple_features.avg_size_of_hole_feature import AvgSizeOfHoleFeature
from tests.bitmap_generator import BitmapGenerator


class TestAvgSizeOfHoleFeature(unittest.TestCase):
    """
    Klasa testująca klase AvgSizeOfHoleFeature
    """
    def setUp(self):
        self.feature = AvgSizeOfHoleFeature(0.5)

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

    def test_white_plain(self):
        """
        Dostarczamy bitmapę wypełniona tylko białym kolorem.
        Oczekujemy Liczby -1 jako informacji o braku dziur.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_white(size, size)

        res = self.count_feature(bitmap)

        self.assertIs(-1, res)

    def test_white_plain_one_hole_of_size_1(self):
        """
        Dostarczamy bitmapę wypełniona tylko białym kolorem, poza jednym pikselem.
        Oczekujemy Liczby 1 jako informacji o jednej dziurze o rozmiarze 1.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_white(size, size)
        bitmap.set_cell_value(1, 1, 0.0)

        res = self.count_feature(bitmap)

        self.assertAlmostEqual(1.0, res)

    def test_white_plain_one_hole_of_size_2(self):
        """
        Dostarczamy bitmapę wypełniona tylko białym kolorem, poza dwoma czarnymi pikselami.
        Oczekujemy Liczby 2 jako informacji o jednej dziurze o rozmiarze 2.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_white(size, size)
        bitmap.set_cell_value(1, 1, 0.0)
        bitmap.set_cell_value(1, 2, 0.0)

        res = self.count_feature(bitmap)

        self.assertAlmostEqual(2.0, res)

    def test_white_plain_two_holes_of_size_1(self):
        """
        Dostarczamy bitmapę wypełniona tylko białym kolorem, poza jednym pikselem.
        Oczekujemy Liczby 1 jako informacji o dwórch dziurach o rozmiarze 1.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_white(size, size)
        bitmap.set_cell_value(1, 1, 0.0)
        bitmap.set_cell_value(3, 3, 0.0)

        res = self.count_feature(bitmap)

        self.assertAlmostEqual(1.0, res)

    def test_white_plain_two_holes_of_size_1_and_2(self):
        """
        Dostarczamy bitmapę wypełniona tylko białym kolorem, poza dwoma dziurami o rozmiarach 1 i 2.
        Oczekujemy Liczby 1.5.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_white(size, size)
        bitmap.set_cell_value(1, 1, 0.0)
        bitmap.set_cell_value(3, 3, 0.0)
        bitmap.set_cell_value(3, 4, 0.0)

        res = self.count_feature(bitmap)

        self.assertAlmostEqual(1.5, res)


