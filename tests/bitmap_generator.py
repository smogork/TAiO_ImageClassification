#! /usr/bin/env python3

"""
Moduł zawiera klasy generujące bitmapy na potrzeby testów jednostkowych
"""

from typing import *

from bitmap.bitmap_grayscale import BitmapGrayscale


class BitmapGenerator:

    @staticmethod
    def iterate_through_bitmap(
            bitmap: BitmapGrayscale,
            func: Callable[[BitmapGrayscale, int, int]]
    ):
        for y in bitmap.get_height():
            for x in bitmap.get_width():
                func(bitmap, x, y)

    @staticmethod
    def plain_color(width: int, height: int, color: int) -> BitmapGrayscale:
        ret = BitmapGrayscale(width, height)

        BitmapGenerator.iterate_through_bitmap(
            ret,
            lambda bitmap, x, y:
                bitmap.set_cell_value(x, y, color)
        )

        return ret

