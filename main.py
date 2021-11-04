#! /usr/bin/env python3

"""
Początkowy moduł
"""

from feature_extractor.feature_extractor import FeatureExtractor

def define_features() -> FeatureExtractor:
    """
    Funkcja inicjalizuje extractor wszystkimi feature'ami jakie mamy
    :return:
    """
    extractor = FeatureExtractor()

    return extractor


def main():
    """
    Docelowa funkcja main
    :return:
    """


def test_main():
    """
    Testowa funkcja main z losowaniem obrazka
    :return:
    """
    # Wylosuj jakąkolwiek bitmpae o wymiarach 30x30

    # Zdefiniuj feature do eksperymentów
    #extractor = define_features()

    # Wyznacz wszystkie feature'y

    # Wypisz wyniki


if __name__ == "__main__":
    test_main()
