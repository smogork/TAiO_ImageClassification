#! /usr/bin/env python


from bitmap_mapper.bitmap_mapper_interface import BitmapMapperInterface
from data_parsers.common_data import CommonData
from feature_extractor.feature_extractor import FeatureExtractor
import pickle
import numpy


class ClassifyData(CommonData):

    def __init__(self, classify_path: str, feature_extractor: FeatureExtractor, bitmap_mapper: BitmapMapperInterface):
        super().__init__(feature_extractor, bitmap_mapper)

        self.__classify_path = classify_path
        self.__classify_features = None
        self.__rowMaskFileName = "rowMask"

    def get_classify_data(self):
        if self.__classify_features is None:
            print ("Calculating classify data")
            self.__train_features = self._extract_features_from_path_without_classes(self.__classify_path)
        return self.__train_features

    def LoadDeletedColumns(self):
        with open('filename.pickle', 'rb') as handle:
            rows = pickle.load(handle)
            self.__classify_features = numpy.delete(self.__classify_features, rows, 1)
