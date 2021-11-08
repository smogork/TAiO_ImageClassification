#! /usr/bin/env python3

"""
Moduł zawiera klasy generujące bitmapy na potrzeby testów jednostkowych
"""

from typing import Callable

from bitmap.bitmap_grayscale import BitmapGrayscale


class BitmapGenerator:
    """
    Statyczna klasa do generowania bitmap w ramach testów
    """

    @staticmethod
    def iterate_through_bitmap(
            bitmap: BitmapGrayscale,
            func: Callable[[BitmapGrayscale, int, int], None]
    ) -> None:
        """
        Metoda wywołuje funkcje na każdej komórce bitmpay
        :param bitmap: Bitmapa do przejścia
        :param func: Funkcja do wykonania na każdej komórce
        """
        for y in range(bitmap.get_height()):
            for x in range(bitmap.get_width()):
                func(bitmap, x, y)

    @staticmethod
    def plain_color(width: int, height: int, color: int) -> BitmapGrayscale:
        """
        Metoda generuje bitmapę w jednym kolorze o wybranym rozmiarze.
        :param width: Szerokość
        :param height: Wysokość
        :param color: Ustalony kolor
        :return: Bitmapa o kolorze color
        """
        ret = BitmapGrayscale(width, height)

        BitmapGenerator.iterate_through_bitmap(
            ret,
            lambda bitmap, x, y:
                bitmap.set_cell_value(x, y, color)
        )

        return ret

    @staticmethod
    def plain_white(width: int, height: int) -> BitmapGrayscale:
        """
        Metoda generuje bitmapę w białym kolorze o wybranym rozmiarze.
        :param width: Szerokość
        :param height: Wysokość
        :return: Bitmapa o kolorze białym
        """
        return BitmapGenerator.plain_color(width, height, BitmapGrayscale.White)

    @staticmethod
    def plain_black(width: int, height: int) -> BitmapGrayscale:
        """
        Metoda generuje bitmapę w czarnym kolorze o wybranym rozmiarze.
        :param width: Szerokość
        :param height: Wysokość
        :return: Bitmapa o kolorze czarnym
        """
        return BitmapGenerator.plain_color(width, height, BitmapGrayscale.Black)
