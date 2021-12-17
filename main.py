#! /usr/bin/env python3

"""
Początkowy moduł
"""
import argparse
import time
from itertools import repeat
from multiprocessing import Pool

import numpy as np
from scipy.io import arff
import pandas as pd
from tensorflow import keras

from bitmap_mapper.min_max_difference_coordinates_bitmap_mapper import MinMaxDifferenceCoordinatesBitmapMapper
from data_parsers.image_learning_data import ImageLearningData
from data_parsers.learning_data import LearningData
from feature.simple_features.avg_size_of_hole_feature import AvgSizeOfHoleFeature
from feature.simple_features.avg_size_of_island_feature import AvgSizeOfIslandFeature
from feature.simple_features.first_quart_feature import FirstQuartFeature
from feature.simple_features.first_raw_moment_horizontal import FirstRawMomentHorizontalFeature
from feature.simple_features.first_raw_moment_vertical import FirstRawMomentVerticalFeature
from feature.simple_features.fourth_quart_feature import FourthQuartFeature
from feature.simple_features.longest_non_empty_antidiagonal_feature import LongestNonEmptyAntidiagonalFeature
from feature.simple_features.longest_non_empty_column_feature import LongestNonEmptyColumnFeature
from feature.simple_features.longest_non_empty_diagonal_feature import LongestNonEmptyDiagonalFeature
from feature.simple_features.longest_non_empty_row_feature import LongestNonEmptyRowFeature
from feature.simple_features.max_feature import MaxFeature
from feature.simple_features.mean_feature import MeanFeature
from feature.simple_features.median_feature import MedianFeature
from feature.simple_features.min_feature import MinFeature
from feature.simple_features.non_empty_columns_feature import NonEmptyColumnsFeature
from feature.simple_features.non_empty_rows_feature import NonEmptyRowsFeature
from feature.simple_features.number_of_holes_feature import NumberOfHolesFeature
from feature.simple_features.number_of_islands_feature import NumberOfIslandsFeature
from feature.simple_features.second_central_moment_horizontal import SecondCentralMomentHorizontalFeature
from feature.simple_features.second_central_moment_vertical import SecondCentralMomentVerticalFeature
from feature.simple_features.second_quart_feature import SecondQuartFeature
from feature.simple_features.third_quart_feature import ThirdQuartFeature
from feature_extractor.feature_extractor import FeatureExtractor
from learning import Learning, ImageLearning
from tests.bitmap_generator import BitmapGenerator


def define_features() -> FeatureExtractor:
    """
    Funkcja inicjalizuje extractor wszystkimi feature'ami jakie mamy
    :return:
    """
    extractor = FeatureExtractor()

    extractor.add_feature(MaxFeature())#1
    extractor.add_feature(MinFeature())
    extractor.add_feature(MeanFeature())
    extractor.add_feature(MedianFeature())
    extractor.add_feature(NonEmptyColumnsFeature(0.05))#5
    extractor.add_feature(NonEmptyRowsFeature(0.95))
    extractor.add_feature(ThirdQuartFeature())
    extractor.add_feature(SecondQuartFeature())
    extractor.add_feature(SecondCentralMomentVerticalFeature())
    extractor.add_feature(SecondCentralMomentHorizontalFeature())#10
    extractor.add_feature(NumberOfIslandsFeature(0.05))# blisko czarnego - NIE DZIALA
    extractor.add_feature(NumberOfHolesFeature(0.95))# blisko bialego - NIE DZIALA
    extractor.add_feature(FirstRawMomentVerticalFeature())
    extractor.add_feature(FirstRawMomentHorizontalFeature())
    extractor.add_feature(AvgSizeOfIslandFeature(0.05))# blisko czarnego # 15
    extractor.add_feature(AvgSizeOfHoleFeature(0.95))# blisko bialego
    extractor.add_feature(FourthQuartFeature())
    extractor.add_feature(LongestNonEmptyRowFeature(0.05))# blisko czarnego
    extractor.add_feature(LongestNonEmptyDiagonalFeature(0.05))# blisko czarnego
    extractor.add_feature(LongestNonEmptyColumnFeature(0.05))# blisko czarnego # 20
    extractor.add_feature(LongestNonEmptyAntidiagonalFeature(0.05))# blisko czarnego
    extractor.add_feature(FirstQuartFeature())# 22

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
    print(data)



def test_classify(training_path: str, test_path: str):
    extractor = define_features()
    data = LearningData(training_path, test_path, extractor, MinMaxDifferenceCoordinatesBitmapMapper())

    model = Learning(extractor.feature_count(), 4) # nie ma latwego sposobu na wylicznie ilosci klas. W moich danych testowych sa 4 klasy.
    model.learn(data, 64, 16)
    model.evaluate(data)

def test_classify_images(training_path: str, test_path: str):
    data = ImageLearningData(training_path, test_path, MinMaxDifferenceCoordinatesBitmapMapper())

    model = ImageLearning(30, 4)  # nie ma latwego sposobu na wylicznie ilosci klas. W moich danych testowych sa 4 klasy.
    model.learn(data, 32, 16)
    model.evaluate(data)

if __name__ == "__main__":
    # Chcemy aby program dzialal w dwoch trybach: nauki i klasyfikacji
    # W trybie nauki potrzebujemy sciezki do danych treningowych oraz informacji ile ostatnich ciagow ma byc traktowanych jako walidacja
    # W trybie klasyfikacji chcemy podac sciezke do danych, ktore bedziemy klasyfikowac i dla kazdego ciagu dostac klase

    parser = argparse.ArgumentParser(description='TAIO obrazki w skali szarosci')
    parser.add_argument("train_path", help="path to training dataset")
    parser.add_argument("test_path", help="path to testing dataset")
    args = parser.parse_args()
    test_classify(args.train_path, args.test_path)
    #test_classify_images(args.train_path, args.test_path)
