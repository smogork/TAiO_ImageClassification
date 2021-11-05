#! /usr/bin/env python3

"""
W module istnieje klasa reprezentująca bitmapę w skali szarości
"""

import png


class BitmapGrayscale:
    """
    Klasa opisuje bitmape o okreslonych wymiarach w skali szarości 8 bitowej
    """

    def __init__(self, width: int, height: int):
        """
        BUdowa pustej białem bitmapy
        :param width: Szerokość
        :param height: Wysokość
        """
        self.__width = width
        self.__height = height
        self.__bitmap = [[0 for i in range(self.__width)] for j in range(self.__height)]
        self.white = 255
        self.black = 0

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

    def get_cell_value(self, x: int, y: int) -> int:
        """
        Uzyskanie zawartości komórki
        :param x: kolumna
        :param y: wiersz
        :return: wartość w komórce
        """
        return self.__bitmap[y][x]

    def set_cell_value(self, x: int, y: int, value: int) -> None:
        """
        Ustawienie wartości w komórce
        :param x: kolumna
        :param y: wiersz
        :param value: wartośc komórki
        """
        if value < self.black or value > self.white:
            raise ValueError(f"Value should be in range [{self.black},{self.white}]")

        self.__bitmap[y][x] = value

    def to_png(self, path: str) -> None:
        """
        Zapis bitmapy do pliku PNG
        :param path: Ścieżka do pliku wynikowego
        """
        with open(path, "wb") as f:
            writer = png.Writer(self.__width, self.__height, greyscale=True)
            writer.write(f, self.__bitmap)