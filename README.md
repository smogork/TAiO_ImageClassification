# TAiO_ImageClassification

Klasyfikacja szeregów czasowych przy pomocy przekształcania szeregów na obrazki czarno-białe.

# Uruchomienie projektu

Projekt wymaga posiadania interpretera pythona w wersji 3.9

Załóżmy, że posiadamy pobrany kod źródłowy projektu. Następnie:
1. (Opcjonalnie - silnie zalecane) Utworzyć wirtualne środowisko pythona w folderze projektu oraz je aktywować.
2. Wczytać zależności projektu zapisane w pliku `requirements.txt` (`pip install -r requiremets/path`).

Od tego momentu punktem wejściowym do programu jest `main.py`.

# Parametry

`./main.py -h` - dokładny opis parametrów

Program działa w dwóch trybach: *training* oraz *classify*.

## Training
W trybie *training* program potrzebuje danych testowych oraz walidacyjnych aby nauczyć sieć.
Dane powinny być dostarczone w postaci pliku ARFF.
Wyjściem tego trybu jest struktura nauczonego modelu (domyslnie plik wyjściowy ma nazwę `model.keras`).
Przykład wywołania: 
```
./main.py training data/AsphaltObstacles_TRAIN.arff data/AsphaltObstacles_TEST.arff
```
## Classify
W trybie *classify* korzystamy z wcześniej wyznaczonego modelu oraz wyznaczmy klasy podanych danych na wejściu (także w formacie ARFF).
Wyjściem programu jest wiele wierszy postaci: [c1 c2 ... cn], gdzie ci jest wartością z zakresu [0,1] oceniającą jak bardzo dane pasują do klasy i.
Każdy wiersz odpowiada klasyfikacji jednego zestawu wejściowego.
Domyślnie program wypisuje je do pliku `output.txt` oraz na standardowe wyjście.
Przykład wywołania: 
```
./main.py classify model.keras data/AsphaltObstacles_TRAIN.arff
```