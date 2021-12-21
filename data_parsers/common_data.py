import time

import numpy as np
import pandas as pd
from scipy.io import arff

from bitmap_mapper.bitmap_mapper_interface import BitmapMapperInterface
from feature_extractor.feature_extractor import FeatureExtractor


class CommonData:
    def __init__(self, feature_extractor: FeatureExtractor, bitmap_mapper: BitmapMapperInterface):
        self.__extractor = feature_extractor
        self.__mapper = bitmap_mapper

    def classes_str_to_array(self, class_str: str):
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

    def classes_array_to_str(self, class_arr):
        # Przykladowe dane
        # TODO: zrobic cos bardziej elastycnego
        if class_arr == [1, 0, 0, 0]:
            return 'raised_crosswalk'
        elif class_arr == [0, 1, 0, 0]:
            return 'raised_markers'
        elif class_arr == [0, 0, 1, 0]:
            return 'speed_bump'
        elif class_arr == [0, 0, 0, 1]:
            return 'vertical_patch'
        else:
            raise RuntimeError('Unknown class')

    def _extract_features_from_path(self, path: str,):
        data = arff.loadarff(path)
        df = pd.DataFrame(data[0])

        classes = df.iloc[:, -1:]

        feature_list = np.empty((len(classes), self.__extractor.feature_count()))
        self.__mapper.set_bitmap_size(30)
        i = 0
        for row in df.iloc[:, :-1].iterrows():
            start = time.process_time_ns()
            bitmap = self.__mapper.convert_series(row[1].values.tolist())
            feature_list[i] = self.__extractor.calculate_features(bitmap)
            end = time.process_time_ns()
            print(f"Set {i + 1} converted at {(end - start) / 1e6} ms")
            i += 1

        classes = np.array([self.classes_str_to_array(s[0].decode()) for s in classes.values])
        return feature_list, classes

    def _extract_features_from_path_without_classes(self, path: str,):
        data = arff.loadarff(path)
        df = pd.DataFrame(data[0])

        first_column = df.iloc[:, 1:]

        feature_list = np.empty((len(first_column), self.__extractor.feature_count()))
        self.__mapper.set_bitmap_size(30)
        i = 0
        for row in df.iloc[:, :-1].iterrows():
            start = time.process_time_ns()
            bitmap = self.__mapper.convert_series(row[1].values.tolist())
            feature_list[i] = self.__extractor.calculate_features(bitmap)
            end = time.process_time_ns()
            print(f"Set {i + 1} converted at {(end - start) / 1e6} ms")
            i += 1

        return feature_list