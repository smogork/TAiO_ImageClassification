#! /usr/bin/env python3

import abc
import typing
from Bitmap import BitmapGrayscale


class Feature:

    @abc.abstractmethod
    def calculate(self):
        pass

    @abc.abstractmethod
    def prepare(self, bitmap: BitmapGrayscale):
        pass
