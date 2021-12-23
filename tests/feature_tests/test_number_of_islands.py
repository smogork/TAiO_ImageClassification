#! /usr/bin/env python

"""
Modul zawiera testy klasy NumberOfIslandsFeature
"""

import unittest

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.simple_features.number_of_islands_feature import NumberOfIslandsFeature
from tests.bitmap_generator import BitmapGenerator


class TestNumberOfIslandsFeature(unittest.TestCase):
    """
    Klasa testująca klase NumberOfIslandsFeature
    """
    def setUp(self):
        self.feature = NumberOfIslandsFeature(0.5)

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

    def test_black_plain(self):
        """
        Dostarczamy bitmapę wypełniona tylko czarnym kolorem.
        Oczekujemy Liczby 0 jako informacji o braku wysp.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)

        res = self.count_feature(bitmap)

        self.assertIs(0, res)

    def test_black_plain_with_one_hole(self):
        """
        Dostarczamy bitmapę wypełniona tylko czarnym kolorem za wyjątkiem jednego czarnego piksela.
        Oczekujemy Liczby 1 jako informacji o jednej wyspie.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(1, 1, 1.0)
        res = self.count_feature(bitmap)

        self.assertIs(1, res)

    def test_black_plain_with_two_holes(self):
        """
        Dostarczamy bitmapę wypełniona tylko czarnym kolorem za wyjątkiem dwóch niepołączonych czarnych pikseli.
        Oczekujemy Liczby 2 jako informacji o dwóch wyspach.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(1, 1, 1.0)
        bitmap.set_cell_value(3, 3, 1.0)
        res = self.count_feature(bitmap)

        self.assertIs(2, res)

    def test_black_plain_with_one_big_hole(self):
        """
        Dostarczamy bitmapę wypełniona tylko czarnym kolorem za wyjątkiem dwóch połączonych ze sobą czarnych pikseli.
        Oczekujemy Liczby 1 jako informacji o jednej dużej wyspie.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(1, 1, 1.0)
        bitmap.set_cell_value(1, 2, 1.0)
        res = self.count_feature(bitmap)

        self.assertIs(1, res)

    def test_black_plain_with_one_big_hole_calculated_twice(self):
        """
        Dostarczamy bitmapę wypełniona tylko czarnym kolorem za wyjątkiem dwóch połączonych ze sobą czarnych pikseli.
        W obrębie testu wyliczane są wartości cechy dwa razy, aby zweryfikować, czy test nie dokonuje zmian w strukturze.
        Oczekujemy Liczby 1 jako informacji o jednej wyspie.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_black(size, size)
        bitmap.set_cell_value(1, 1, 1.0)
        bitmap.set_cell_value(1, 2, 1.0)
        res1 = self.count_feature(bitmap)

        res2 = self.count_feature(bitmap)

        self.assertIs(1, res2)

    def test_black_plain_with_one_big_hole_of_four_pixels(self):
        """
        Dostarczamy bitmapę wypełniona tylko czarnym kolorem za wyjątkiem czterech połączonych ze sobą czarnych pikseli.
        Oczekujemy Liczby 1 jako informacji o jednej wyspie.
        :return:
        """
        size = 5

        bitmap = BitmapGenerator.plain_white(size, size)
        bitmap.set_cell_value(1, 1, 1.0)
        bitmap.set_cell_value(1, 2, 1.0)
        bitmap.set_cell_value(2, 1, 1.0)
        bitmap.set_cell_value(2, 2, 1.0)
        res = self.count_feature(bitmap)

        self.assertIs(1, res)
