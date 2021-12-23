#! /usr/bin/env python

"""
W module istnieje klasa reprezentująca bitmapę w skali szarości
"""
import numpy as np
import png
from numpy import ndarray


class BitmapGrayscale:
    """
    Klasa opisuje bitmape o okreslonych wymiarach w skali szarości 8 bitowej
    """

    White = 1.0
    Black = 0.0

    def __init__(self, width: int, height: int):
        """
        BUdowa pustej białem bitmapy
        :param width: Szerokość
        :param height: Wysokość
        """
        self.__width = width
        self.__height = height
        self.__bitmap = np.zeros((height, width))

    def get_height(self) -> int:
        """
        Pobranie wysokości
        :return: Wysokość
        """
        return self.__height

    def get_width(self) -> int:
        """
        Pobranie szerokości
        :return: Szerokość
        """
        return self.__width

    def get_row(self, rowNum: int) -> ndarray :
        return self.__bitmap[rowNum, :]

    def get_column(self, colNum: int) -> ndarray :
        return self.__bitmap[:, colNum]

    def get_cell_value(self, x: int, y: int) -> float:
        """
        Uzyskanie zawartości komórki
        :param x: kolumna
        :param y: wiersz
        :return: wartość w komórce
        """
        return self.__bitmap[y][x]

    def set_cell_value(self, x: int, y: int, value: float) -> None:
        """
        Ustawienie wartości w komórce
        :param x: kolumna
        :param y: wiersz
        :param value: wartośc komórki
        """
        self.__bitmap[y][x] = value

    def to_png(self, path: str) -> None:
        """
        Zapis bitmapy do pliku PNG
        :param path: Ścieżka do pliku wynikowego
        """
        mapped_bitmap = [[0 for i in range(self.__width)] for j in range(self.__height)]
        for y in range(self.__height):
            for x in range(self.__width):
                mapped_bitmap[y][x] = int(round(self.__bitmap[y][x] * 255))

        with open(path, "wb") as f:
            writer = png.Writer(self.__width, self.__height, greyscale=True)
            writer.write(f, mapped_bitmap)

    def get_array(self):
        return np.array(self.__bitmap)
