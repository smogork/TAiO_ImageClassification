from statistics import StatisticsError
from unittest import TestCase

from bitmap.bitmap_grayscale import BitmapGrayscale
from feature.simple_features.mean_feature import MeanFeature


class TestMeanFeature(TestCase):
    """
        Klasa testująca klase MaxFeature
        """

    def setUp(self):
        self.feature = MeanFeature()

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
        with self.assertRaises(StatisticsError):
            self.feature.calculate()
