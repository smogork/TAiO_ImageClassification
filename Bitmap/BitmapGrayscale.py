#! /usr/bin/env python3

import png


class BitmapGrayscale:
    """
    Klasa opisuje bitmape o okreslonych wymiarach w skali szarości 8 bitowej
    """



    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__bitmap = [[0 for i in range(self.__width)] for j in range(self.__height)]
        self.white = 255
        self.black = 0

    def get_height(self) -> int:
        return self.__height

    def get_width(self) -> int:
        return self.__width

    def get_cell_value(self, x: int, y: int) -> int:
        return self.__bitmap[y][x]

    def set_cell_value(self, x: int, y: int, value: int) -> None:
        if value < self.black or value > self.white:
            raise ValueError(f"Value should be in range [{self.black},{self.white}]")

        self.__bitmap[y][x] = value

    def to_png(self, path: str) -> None:
        with open(path, "wb") as f:
            writer = png.Writer(self.__width, self.__height, greyscale=True)
            writer.write(f, self.__bitmap)
