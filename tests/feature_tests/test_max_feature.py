#! /usr/bin/env python3

"""
Modul zawiera testy klasy MaxFeature
"""

import unittest

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.simple_features.max_feature import MaxFeature
from tests.bitmap_generator import BitmapGenerator


class TestMaxFeature(unittest.TestCase):
    """
    Klasa testująca klase MaxFeature
    """
    def setUp(self):
        self.feature = MaxFeature()

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

    def test_non_white_plain(self):
        """
        Dostarczamy bitmapę wypełniona jednym nie białym kolorem.
        Oczekujemy wyniku ilości komórek -1.
        :return:
        """
        color = 0.5
        size = 3

        bitmap = BitmapGenerator.plain_color(size, size, color)

        res = self.count_feature(bitmap)

        self.assertIs(size * size - 1, res)

    def test_white_plain(self):
        """
        Dostarczamy bitmapę wypełniona tylko białym kolorem.
        Oczekujemy Liczby -1 jako informacji o całej białej bitmapie.
        :return:
        """
        size = 3

        bitmap = BitmapGenerator.plain_white(size, size)

        res = self.count_feature(bitmap)

        self.assertIs(-1, res)

    def test_black_dot(self):
        """
        Dostarczamy bitmape całkowicie białą, z wyjątkiem jednego czrnego pixela.
        oczekujemy Numeru tego pixela.
        :return:
        """
        size = 5
        x = 4
        y = 1
        bitmap = BitmapGenerator.plain_white(size, size)
        bitmap.set_cell_value(x, y, BitmapGrayscale.Black)# czarna kropka

        res = self.count_feature(bitmap)

        self.assertIs(res, size * x + y)

    def test_black_dot_multiple_times(self):
        """
        Dostarczamy bitmape całkowicie białą, z wyjątkiem jednego czrnego pixela.
        oczekujemy Numeru tego pixela.
        TEst uruchamiamy 3 razy
        :return:
        """
        size = 5
        x = 4
        y = 1
        bitmap = BitmapGenerator.plain_white(size, size)
        bitmap.set_cell_value(x, y, BitmapGrayscale.Black)# czarna kropka

        res1 = self.count_feature(bitmap)
        res2 = self.count_feature(bitmap)
        res3 = self.count_feature(bitmap)

        self.assertIs(res1, size * x + y)
        self.assertIs(res2, size * x + y)
        self.assertIs(res3, size * x + y)
