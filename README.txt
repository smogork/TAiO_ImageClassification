TAiO_ImageClassification

 Klasyfikacja szeregów czasowych przy pomocy przekształcania szeregów na obrazki czarno-białe.
 Uruchomienie projektu

 Projekt był testowany na interpreterze pythona 3.9. Prawdopodobnie starsze wersje interpretera w wersji 3 przy
 poprawce wersji zależności w pliku requirements.txt także powinny prawidłowo uruchomić kod.

 Załóżmy, że posiadamy pobrany kod źródłowy projektu. Następnie:

   0. (MINI) Uruchamiamy Anaconda Prompt będąc na Windowsie albo terminal będąc na linuxie.
   1. Utworzyć wirtualne środowisko pythona w folderze projektu oraz je
      aktywować (python -m venv venv && .\venv\Scripts\activate.bat).
   2. Wczytać zależności projektu, bez korzystania z folderu cache, zapisane w pliku requirements.txt
     (pip install -r requiremets/path --no-cache-dir).

 Czasami może się zdarzyć, że folder domowy sie przepełni. Wtedy należy
 przekopiować folder z kodem do /tmp i tam wykonać powyższe kroki.

 Od tego momentu punktem wejściowym do programu jest main.py.
 Parametry

 python main.py -h - dokładny opis parametrów

 Program działa w dwóch trybach: training oraz classify.
Training

W trybie training program potrzebuje danych testowych oraz walidacyjnych aby nauczyć sieć. Dane powinny być
 dostarczone w postaci pliku ARFF. Wyjściem tego trybu jest struktura nauczonego modelu (domyslnie plik wyjściowy
 ma nazwę model.keras). Przykład wywołania:

 python main.py training data/AsphaltObstacles_TRAIN.arff data/AsphaltObstacles_TEST.arff

 Classify

W trybie classify korzystamy z wcześniej wyznaczonego modelu oraz wyznaczmy klasy podanych danych na wejściu
 (także w formacie ARFF). Wyjściem programu jest wiele wierszy postaci: [c1 c2 ... cn], gdzie ci jest wartością z zakresu
 [0,1] oceniającą jak bardzo dane pasują do klasy i. Każdy wiersz odpowiada klasyfikacji jednego zestawu wejściowego.
 Domyślnie program wypisuje je do pliku output.txt oraz na standardowe wyjście. Przykład wywołania:

 python main.py classify model.keras data/AsphaltObstacles_TRAIN.arff

 Format danych wyjściowych

W procesie uczenia podawana jest ścieżka output_path, do której program wypisuje pliki:

   1. output_path - model nauczony na podanych danych. Potrzebne do procesu klasyfikacji.
   2. output_path.feature - serializowane cechy uznane za zbędne. Potrzebne aby przy klasyfikacji już nauczonego
      modelu brac pod uwagę tylko konieczne cechy.
   3. output_path.weight - plik tekstowy z listą cech wykorzystanych przy uczeniu modelu oraz ich znaczenie w
      klasyfikacji.
   4. output_path.pdf - plik pdf z wykresem przedstawiającym historię uczenia modelu. Wykres przedstawia poziom
      dokładności w zalezności od epoki uczenia.
   5. output_path.corrarr - plik csv reprezentujący macierz korelacji pomiędzy cechami wyznaczone w czasie
      uczenia.
