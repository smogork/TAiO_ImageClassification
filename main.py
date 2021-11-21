#! /usr/bin/env python3

"""
Początkowy moduł
"""
import numpy as np

from feature.simple_features.max_feature import MaxFeature
from feature.simple_features.mean_feature import MeanFeature
from feature.simple_features.median_feature import MedianFeature
from feature.simple_features.min_feature import MinFeature
from feature.simple_features.non_empty_columns_feature import NonEmptyColumnsFeature
from feature.simple_features.non_empty_rows_feature import NonEmptyRowsFeature
from feature_extractor.feature_extractor import FeatureExtractor
from tests.bitmap_generator import BitmapGenerator


def define_features() -> FeatureExtractor:
    """
    Funkcja inicjalizuje extractor wszystkimi feature'ami jakie mamy
    :return:
    """
    extractor = FeatureExtractor()

    extractor.add_feature(MaxFeature())
    extractor.add_feature(MinFeature())
    extractor.add_feature(MeanFeature())
    extractor.add_feature(MedianFeature())
    extractor.add_feature(NonEmptyColumnsFeature())
    extractor.add_feature(NonEmptyRowsFeature())

    return extractor


def main():
    """
    Docelowa funkcja main
    :return:
    """


def test_main():
    """
    Testowa funkcja main z losowaniem obrazka
    :return:
    """
    # Wylosuj jakąkolwiek bitmpae o wymiarach 30x30
    size = 30
    seed = 1234
    bitmap = BitmapGenerator.random(size, size, seed)
    bitmap.to_png("test_main.png")

    # Zdefiniuj feature do eksperymentów
    extractor = define_features()

    # Wyznacz wszystkie feature'y
    # np.array(extractor.calculate_features_mp(bitmap, 4))
    data = np.array(extractor.calculate_features(bitmap))

    # Wypisz wyniki
    print (data)



if __name__ == "__main__":
    test_main()
