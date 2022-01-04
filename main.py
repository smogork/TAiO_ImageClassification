#! /usr/bin/env python

"""
Początkowy moduł
"""
import argparse

from bitmap_mapper.min_max_difference_coordinates_bitmap_mapper import MinMaxDifferenceCoordinatesBitmapMapper
from data_parsers.classify_data import ClassifyData
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
from feature.simple_features.max_projection_horizontal_feature import MaxProjectionHorizontalFeature
from feature.simple_features.max_projection_horizontal_value_feature import MaxProjectionHorizontalValueFeature
from feature.simple_features.max_projection_vertical_feature import MaxProjectionVerticalFeature
from feature.simple_features.max_projection_vertical_value_feature import MaxProjectionVerticalValueFeature
from feature.simple_features.mean_feature import MeanFeature
from feature.simple_features.median_feature import MedianFeature
from feature.simple_features.min_feature import MinFeature
from feature.simple_features.min_projection_horizontal_feature import MinProjectionHorizontalFeature
from feature.simple_features.min_projection_horizontal_value_feature import MinProjectionHorizontalValueFeature
from feature.simple_features.min_projection_vertical_feature import MinProjectionVerticalFeature
from feature.simple_features.min_projection_vertical_value_feature import MinProjectionVerticalValueFeature
from feature.simple_features.non_empty_columns_feature import NonEmptyColumnsFeature
from feature.simple_features.non_empty_rows_feature import NonEmptyRowsFeature
from feature.simple_features.number_of_holes_feature import NumberOfHolesFeature
from feature.simple_features.number_of_islands_feature import NumberOfIslandsFeature
from feature.simple_features.second_central_moment_horizontal import SecondCentralMomentHorizontalFeature
from feature.simple_features.second_central_moment_vertical import SecondCentralMomentVerticalFeature
from feature.simple_features.second_quart_feature import SecondQuartFeature
from feature.simple_features.third_quart_feature import ThirdQuartFeature
from feature_extractor.feature_extractor import FeatureExtractor
from learning import Learning, LearningClassify


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
    extractor.add_feature(MaxProjectionHorizontalFeature())
    extractor.add_feature(MaxProjectionHorizontalValueFeature())
    extractor.add_feature(MaxProjectionVerticalFeature())
    extractor.add_feature(MaxProjectionVerticalValueFeature())
    extractor.add_feature(MinProjectionHorizontalFeature())
    extractor.add_feature(MinProjectionHorizontalValueFeature())
    extractor.add_feature(MinProjectionVerticalFeature())
    extractor.add_feature(MinProjectionVerticalValueFeature())

    return extractor

def classify_main(model_path: str, classify_data_path: str, output: str):
    extractor = define_features()
    data = ClassifyData(classify_data_path, extractor, MinMaxDifferenceCoordinatesBitmapMapper())

    model = LearningClassify(model_path)
    classes = model.classify(data)

    with open(output, "w") as f:
        for c in classes:
            f.write(f"{str(c)}\n")

def train_main(training_path: str, test_path: str, output_path: str):
    extractor = define_features()
    data = LearningData(training_path, test_path, extractor, MinMaxDifferenceCoordinatesBitmapMapper())

    model = Learning(extractor.feature_count(), 4) # nie ma latwego sposobu na wylicznie ilosci klas. W moich danych testowych sa 4 klasy.
    model.plot_history(model.learn(data, 1024, 8))
    model.save_model(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='TAIO obrazki w skali szarosci')
    subparser = parser.add_subparsers(dest='mode')
    parser_training = subparser.add_parser('training', help="Training mode")
    parser_training.add_argument("train_path", help="path to training dataset")
    parser_training.add_argument("test_path", help="path to testing dataset")
    parser_training.add_argument("-o", "--output", help="Output path for model from learning process",
                                 default="model.keras")
    parser_classify = subparser.add_parser('classify', help="Classification mode")
    parser_classify.add_argument("model_path", help="path to model file")
    parser_classify.add_argument("classification_path", help="path to objects to classify")
    parser_classify.add_argument("-o", "--output", help="Output path for classification result",
                                 default="output.txt")
    args = parser.parse_args()

    if args.mode == "classify":
        classify_main(args.model_path, args.classification_path, args.output)
    elif args.mode == "training":
        train_main(args.train_path, args.test_path, args.output)