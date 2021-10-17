#! /usr/bin/env python3
import sys

from Bitmap.BitmapGrayscale import BitmapGrayscale


class BitmapGrayscaleCounter(BitmapGrayscale):
    """
    Klasa reprezentująca tablicę, gdzie kazdy element można inkrementować.
    Następnie przetwarza taka tablice do BitmapGrayscale, gdzie kolor czarny to wartosc maksymalna znaleziona w tablicy, a biały to 0.
    """

    def __init__(self, width, height):
        self.__width = width
        super(BitmapGrayscaleCounter, self).__init__(self, width, height)
        super(BitmapGrayscaleCounter, self).White = sys.maxsize * 2 + 1 #Duża liczba w stylu MaxInt

    def increment_cell(self, x, y) -> int:
        """
        Metoda inkrementuje komórkę o wspólrzędnych podanych w argumentach

        :param x: Wspólrzędna X (numer kolumny)
        :param y: Wspólrzędna Y (numer wiersza)
        :return: Zwraca wartość komórki po inkrementacji
        """
        super(BitmapGrayscaleCounter, self).setCellValue(x, y, super(BitmapGrayscaleCounter, self).getCellValue(x, y) + 1)
        return super(BitmapGrayscaleCounter, self).getCellValue(x, y)

    def convert_to_BitmapGrayscale(self) -> BitmapGrayscale:
        """
        Metoda przetwarza aktualny stan liczników na bitmapę w skali szarości.
        0 -> biały
        maksymalna wartość z liczników -> czarny
        Reszta wartości przeskalowana jest liniowo pomiędzy tymi dwoma wartościami

        :return: Zwraca obiekt typu BitmapGrayscale reprezentujący przetworzoną bitmapę.
        """
        result = BitmapGrayscale(super(BitmapGrayscaleCounter, self).getWidth(), super(BitmapGrayscaleCounter, self).getHeight())

        #Znalezienie wartosci maksymalnej
        max_value = self.__get_max_value_in_array()

        #Przeskalowanie liniowo każdego elementu od zero do max_value
        for y in range(super(BitmapGrayscaleCounter, self).getWidth()):
            for x in range(super(BitmapGrayscaleCounter, self).getHeight()):
                #Dodatkowo zmianiemy max_value na 0, ponieważ czarny reprezentujemy jako 0 w bitmapie
                result.setCellValue(x, y, (max_value - super(BitmapGrayscaleCounter, self).getCellValue(x, y) // max_value)

        return result

    def __get_max_value_in_array(self) -> int:
        """
        Metoda znajduje maksymalną wartośc aktualnego stanu liczników

        :return: Maksymalna zanleziona wartość
        """
        max_value = 0

        for y in range(super(BitmapGrayscaleCounter, self).getWidth()):
            for x in range(super(BitmapGrayscaleCounter, self).getHeight()):
                max_value = max(max_value, super(BitmapGrayscaleCounter, self).getCellValue(x, y))

        return max_value

