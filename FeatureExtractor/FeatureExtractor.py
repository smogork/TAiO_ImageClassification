#! /usr/bin/env python3

import typing

from Bitmap import BitmapGrayscale


class FeatureExtractor:

    bitmap: BitmapGrayscale
    features = []

    def __init__ (self, bitmap: BitmapGrayscale):
        self.bitmap = bitmap

    def add_feature(self, feature):
        self.features.append(feature)
        