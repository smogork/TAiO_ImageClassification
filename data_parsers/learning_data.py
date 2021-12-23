#! /usr/bin/env python

import time
import pandas
import numpy as np
import pandas as pd
from scipy.io import arff

from bitmap_mapper.bitmap_mapper_interface import BitmapMapperInterface
from data_parsers.common_data import CommonData
from feature_extractor.feature_extractor import FeatureExtractor


class LearningData(CommonData):

    def __init__ (self, train_path: str, test_path: str, feature_extractor: FeatureExtractor, bitmap_mapper: BitmapMapperInterface):
        super().__init__(feature_extractor, bitmap_mapper)

        self.__test_path = train_path
        self.__train_features = None
        self.__train_classes = None
        self.__train_path = test_path
        self.__test_features = None
        self.__test_classes = None

    def get_training_data(self):
        if self.__train_features is None or self.__train_classes is None:
            print ("Calculating training data")
            self.__train_features, self.__train_classes = self._extract_features_from_path(self.__train_path)
        return self.__train_features, self.__train_classes

    def get_testing_data(self):
        if self.__test_features is None or self.__test_classes is None:
            print("Calculating testing data")
            self.__test_features, self.__test_classes = self._extract_features_from_path(self.__test_path)
        return self.__test_features, self.__test_classes