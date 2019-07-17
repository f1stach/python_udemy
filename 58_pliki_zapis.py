"""
wczytywanie danych do pliku;
najpierw otwieramy plik, przekazujemy ścieżkę do pliku i atrybut w jak write;
tryby:
w = write - zapis do pliku z nadpisywaniem danych
a = append umożliwiający dopisywanie danych do pliku zamiast nadpisywania
w+ - odczyt i zapis - można mieszac funkcje czytające i zapisujące do pliku z nadpisywaniem
a+ - odczyt i zapis - można mieszac funkcje czytające i zapisujące do pliku bez nadpisywania
"""

filename = "/home/wojtek/results.txt"

line = "Europe"

cities = ["London", "Berlin", "Paris", "Warsaw", "Madrid", "Rome"]


file = open(filename, "a")

# zapis danych do pliku tekstowego - polecenie write:

file.write(line)

# zapis listy wartości - polecenie writelines

file.write("\n")
# file.writelines(cities) # w tej wersji w pliku miasta bez separatorów

# poprawka dla braku separatorów listy - pętla for - jedna linia to jedno miasto i znak nowej linii:

for city in cities:
    file.write(city+"\n")



# otwarty plik zamykamy

file.close()