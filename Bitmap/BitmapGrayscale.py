#! /usr/bin/env python3

import png


class BitmapGrayscale:
    """
    Klasa opisuje bitmape o okreslonych wymiarach w skali szarości 8 bitowej
    """

    White = 255
    Black = 0

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__bitmap = [[0 for i in range(self.__width)] for j in range(self.__height)]

    def getHeight(self) -> int:
        return self.__height

    def getWidth(self) -> int:
        return self.__width

    def getCellValue(self, x, y) -> int:
        return self.__bitmap[y][x]

    def setCellValue(self, x, y, value) -> None:
        if value < self.Black or value > self.White:
            raise ValueError(f'Value should be in range [{self.Black},{self.White}]')

        self.__bitmap[y][x] = value

    def toPNG(self, path) -> None:
        with open(path, 'wb') as f:
            writer = png.Writer(self.__width, self.__height, greyscale=True)
            writer.write(f, self.__bitmap)
