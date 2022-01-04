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
        self._class_names = None

    def classes_str_to_array(self, class_str: str) -> np.ndarray:
        index = np.where(self._class_names == class_str)
        res = np.zeros(self.get_class_count(), dtype=np.int64)
        res[index] = 1

        if sum(res) == 0:
            raise RuntimeError('Unknown class')
        return res

    def classes_array_to_str(self, class_arr: np.ndarray) -> str:
        if len(class_arr) != len(self._class_names):
            raise RuntimeError('Unknown class')

        index = np.where(class_arr == 1)
        res = self._class_names[index]

        if len(res) == 0:
            raise RuntimeError('Unknown class')
        return res

    def _extract_features_from_path(self, path: str):
        data = arff.loadarff(path)
        df = pd.DataFrame(data[0])

        classes = np.array([s[0].decode() for s in df.iloc[:, -1:].values])
        self._class_names = np.unique(classes)
        self._class_names.sort()
        mapped_classes = np.empty((len(classes), self.get_class_count()))
        for i in range(len(classes)):
            mapped_classes[i] = self.classes_str_to_array(classes[i])

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

        return feature_list, mapped_classes

    def _extract_features_from_path_without_classes(self, path: str):
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

    def _extract_classes_from_path(self, path: str):
        data = arff.loadarff(path)
        df = pd.DataFrame(data[0])
        classes = np.array([s[0].decode() for s in df.iloc[:, -1:].values])
        self._class_names = np.unique(classes)
        self._class_names.sort()
        mapped_classes = np.array((len(classes), self.get_class_count()))
        for i in range(len(classes)):
            mapped_classes[i] = self.classes_str_to_array(classes[i])
        return mapped_classes

    def get_class_count(self):
        if self._class_names is None:
            return None
        return len(self._class_names)

    def SetActiveFeatures(self, mask):
        self.__extractor.SetActiveFeatures(mask)

    def GetActiveFeaturesNames(self):
        return self.__extractor.GetActiveFeaturesNames()
