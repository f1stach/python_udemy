import os
import time

# os.getcwd() - info o bieżącym katalogu (w którym jest projekt):
print("Current directory is:", os.getcwd())

currentDir = os.getcwd()
filename = "results.txt"

# os.path.join - łączymy katalog z plikiem o danej nazwie
fullpath = os.path.join(currentDir, filename)
print("\nThe constructed file path is", fullpath)

# sciezka do pliku względna - okresla położenie pliku względem bieżącego katalogu
# czyli jezeli podam plik jak nizej to python sklei podany katalog z bieżącą nazwą
# sciezka bezwzgledna - litera dysku z katalogami i nazwą pliku
relativePath = "output.txt"
print("\nThe absolute path is", os.path.abspath(relativePath))

# analiza scieżki za pomocą modułu os. Wyodrębniamy część dot. pliku i katalogu:
# basename - zwraca nazwę samego pliku
# dirname - sciezka dostępu do katalogu z plikiem
filepath = r"/home/wojtek/results.txt"
print("\nThe file name part is:", os.path.basename(filepath))
print("The directory part is:", os.path.dirname(filepath))

# spr. czy plik lub folder istnieje:
print("\nIs file existing?", os.path.exists(filepath))

if os.path.exists(filepath):
    # getmtime - data modyfikacji pliku
    # getctime - data utworzenia pliku
    # getatime - data ostatniego dostepu do pliku
    # zwraca epoc time (unixowy od 1970 roku w sekundach) dlatego robimy konwersje czasu przez time"
    print("\nLast modify date is:", os.path.getmtime(filepath))
    print("Last modify date is:", time.localtime(os.path.getmtime(filepath)))

    # getsize - rozmiar pliku zwracany w bajtach
    print("\nFile size is:", os.path.getsize(filepath))

    # isfile - czy ścieżka okresla plik
    # isdir - czy ścieżka określa katalog
    print("\nIs it a file?", os.path.isfile(filepath))
    print("Is it a dir?", os.path.isdir(filepath))

    # path.split - zadaniem jest oderwać ostatni fragment sciezki dostepu do pliku lub katalogu
    print("\nPath split:", os.path.split(filepath))
    print("Only file name part:", os.path.split(filepath)[1])

    # splitdrive - zadaniem oderwanie samej nazwy dysku. Zwraca tuple.
    print("\nPath split into drive:", os.path.splitdrive(filepath))
    print("Only drive:", os.path.splitdrive(filepath)[0])
