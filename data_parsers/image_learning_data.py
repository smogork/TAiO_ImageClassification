#! /usr/bin/env python

import time
import pandas
import numpy as np
import pandas as pd
from scipy.io import arff

from bitmap_mapper.bitmap_mapper_interface import BitmapMapperInterface
from feature_extractor.feature_extractor import FeatureExtractor


class ImageLearningData:

    def __init__ (self, train_path: str, test_path: str, bitmap_mapper: BitmapMapperInterface):
        self.__test_path = train_path
        self.__train_features = None
        self.__train_classes = None
        self.__train_path = test_path
        self.__test_features = None
        self.__test_classes = None

        self.__mapper = bitmap_mapper

    def __map_classes(self, class_str: str):
        # Przykladowe dane
        #TODO: zrobic cos bardziej elastycnego
        if class_str == 'raised_crosswalk':
            return [1, 0, 0, 0]
        elif class_str == 'raised_markers':
            return [0, 1, 0, 0]
        elif class_str == 'speed_bump':
            return [0, 0, 1, 0]
        elif class_str == 'vertical_patch':
            return [0, 0, 0, 1]
        else:
            raise RuntimeError('Unknown class')

    def __extract_features_from_path(self, path: str):
        data = arff.loadarff(path)
        df = pd.DataFrame(data[0])

        # data_size = 16# TODO: do wyrzucenia pozniej!
        classes = df.iloc[:, -1:]

        feature_list = np.empty((len(classes), 30, 30))
        self.__mapper.set_bitmap_size(30)
        i = 0
        for row in df.iloc[:, :-1].iterrows():
            start = time.process_time_ns()
            feature_list[i] = self.__mapper.convert_series(row[1].values.tolist()).get_array()
            end = time.process_time_ns()
            print(f"Set {i + 1} converted at {(end - start) / 1e6} ms")
            i += 1

        classes = np.array([self.__map_classes(s[0].decode()) for s in classes.values])
        return feature_list, classes

    def get_training_data(self):
        if self.__train_features is None or self.__train_classes is None:
            print ("Calculating training image data")
            self.__train_features, self.__train_classes = self.__extract_features_from_path(self.__train_path)
        return self.__train_features, self.__train_classes

    def get_testing_data(self):
        if self.__test_features is None or self.__test_classes is None:
            print("Calculating testing image data")
            self.__test_features, self.__test_classes = self.__extract_features_from_path(self.__test_path)
        return self.__test_features, self.__test_classes