#! /usr/bin/env python3

from Bitmap.BitmapGrayscale import BitmapGrayscale

class BitmapMapperInterface:
    """
    Interfejs reprezentujący wszystkei sposoby przetworzenia ciągu liczb na obrazek w skali szarości.
    Obrazek będzie kwadratowy o ustalonej szerokości.
    """

    def convert_series(self, series) -> BitmapGrayscale:
        """
        Metoda powinna przetworzyć pewien ciąg liczbowy na obrazek w skali szarości.

        :param series: Ciąg danych liczbowych
        :return: Zwraca BitmapGrayscale przechowującą obrazek wygenerowany w pewien sposób z ciągu wejściowego.
        """
        pass

    def set_bitmap_size(self, bitmap_size) -> None:
        """
        Metoda powinna byc uzyta do konfiguracji rozmiaru bitmapy wynikowej.
        Wynikowa bitmapa powinna byc rozmiaru podanego w tej metodzie.
        Gdy nie zostanie ona wykonana przed ConvertSeries, powinien zostac wyrzucony wyjatek RuntimeError.

        :param bitmap_size: Szerokośc i wysokość bitmapy (jedna liczba)
        """
        pass