TAiO_ImageClassification

Nazwa projektu:
    Klasyfikacja szeregów czasowych przy pomocy przekształcania szeregów na obrazki czarno-białe.


Instrukcja uruchamiania:

    Uwaga!
    Projekt był testowany na interpreterze pythona 3.9. Starsze wersje interpretera w wersji co najmniej 3 też prawdopodobnie
    prawidłowo uruchomią kod projektu, jednakże wymaga to poprawienia wersji zależności programu w pliku requirements.txt.

    Tworzenie środowiska:
        1. Pobrać kod źródłowy projektu i go rozpakować.
        2. (MINI) Uruchomić Anaconda Prompt będąc na Windowsie albo terminal będąc na linuxie.
        3. Zmienić aktualny katalog roboczy na miejsce rozpakowania kodu. Po zmianie katalog roboczy powinien zawierać m. in. plik main.py.
        4. Utworzyć wirtualne środowisko pythona w folderze projektu oraz je
           aktywować:
              python -m venv venv && .\venv\Scripts\activate.bat
        5. Wczytać zależności projektu, zapisane w pliku requirements.txt, bez korzystania z folderu cache:
              pip install -r requiremets/path --no-cache-dir

        Uwaga!
        Czasami może się zdarzyć, że folder domowy sie przepełni. Wtedy należy
        przekopiować folder z kodem do /tmp i tam wykonać powyższe kroki.

    Po stworzeniu środowiska punktem wejściowym do programu jest main.py.

    Parametry wywołania programu:
    python main.py -h - dokładny opis parametrów

    Program działa w dwóch trybach: training oraz classify.


    Tryb training:

        W trybie training program wykorzystuje dane testowe oraz walidacyjne żeby nauczyć sieć. Dane powinny być
        dostarczone w postaci pliku ARFF. Wyjściem programu uruchomionego w tym trybie jest struktura nauczonego modelu
        (domyslnie plik wyjściowy ma nazwę model.keras).

        Przykład wywołania:
            python main.py training data/AsphaltObstacles_TRAIN.arff data/AsphaltObstacles_TEST.arff

    Tryb classify

        W trybie classify korzystamy z wcześniej wyuczonego modelu do wyznaczania klas danych podanych na wejściu
        (także przekazanych w formacie ARFF).
        Wyjściem programu jest ciąg wierszy postaci:
            [c1 c2 ... cn] - ci jest liczbą z zakresu [0,1] określającą jak bardzo dane z odpowiadającego szeregu wejścia pasują do i-tej klasy.
            Każdy wiersz odpowiada klasyfikacji jednego szeregu wejściowego (j-ty wiersz - j-ty szereg wejścia).

        Domyślnie program wypisuje dane wyjściowe do pliku output.txt oraz na standardowe wyjście.
        Przykład wywołania:
            python main.py classify model.keras data/AsphaltObstacles_TRAIN.arff

    Format danych wyjściowych

    W procesie uczenia podawana jest ścieżka output_path, do której program zapisuje pliki:
    1. output_path - model nauczony na podanych danych. Potrzebnu do procesu klasyfikacji.
    2. output_path.feature - zserializowane cechy uznane za zbędne. Potrzebne aby przy klasyfikacji za pomocą już nauczonego
       modelu, brać pod uwagę tylko istotne cechy.
    3. output_path.weight - plik tekstowy z listą cech wykorzystanych przy uczeniu modelu oraz ich znaczenie w
       klasyfikacji.
    4. output_path.pdf - plik pdf z wykresem przedstawiającym historię uczenia modelu. Wykres przedstawia poziom
       dokładności w zależności od epoki uczenia.
    5. output_path.corrarr - plik csv reprezentujący macierz korelacji pomiędzy cechami, wyznaczoną w czasie
       uczenia.
