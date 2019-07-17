"""
otwieranie pliku - polecenie open z parametrem przyjmującym ścieżkę do pliku, który ma zostać otwarty oraz drugim
parametrem pokazującym tryb dla pliku:
r = read, otwarcie tylko do odczytu
# file.read() - plik można wczytać w całości za jednym zamachem

"""

file = open("/home/wojtek/results.txt", "r")
content = file.read()

print(content)

# otwarty plik należy zamknąć!!

file.close()

"""
można jednak wykonać trik pozwalający zapomnieć o konieczności zamykania pliku - poleceniem with, w ramach którego
plik będzie otwarty i dostępny
with open() as file - nazwa zmiennej, do której plik przypisujemy to "file"
"""

with open("/home/wojtek/results.txt", "r") as file:
    content = file.read()
    print(content)

"""
poniżej całkiem wydajne rozwiązanie, dobre dla wiekszych tekstów.
Nie musimy pamiętac o otwieraniu i zamykaniu pliku, ale dodatkowo odczyt następuje linijka po linijce - lepiej tak dla
wielkich plików
"""

with open("/home/wojtek/results.txt", "r") as file:
    for line in file:
        print(line)

"""
mozna tez wykorzystac otwieranie i zamykanie pliku w połączeniu z wczytywaniem linijka po linijce, jak nizej:
"""

file = open("/home/wojtek/results.txt", "r")
for line in file:
    print(line)
file.close()

"""
ponizej niedobre rozwiązanie - metoda readlines wczytuje cały plik od razu powodując tym samym to samo co sposób 
pierwszy czyli zatkanie systemu przy wiekszych plikach. Bez sensu jest dalsze wczytywanie linijka po linijce
"""
file = open("/home/wojtek/results.txt", "r")
for line in file.readlines():
    print(line)
file.close()

"""
istnieje tez możliwość wczytywanie fragmentów tekstu:
"""

file = open("/home/wojtek/results.txt", "r")

# liczba 10 w argumencie pokazuje, ze chcemy przeczytać na raz 10 bajtów
fragment = file.read(10)

# budujemy pętle przechodzącą przez plik w paczkach po 10 bajtów. Przeszukujemy zmienną fragment, jezeli jest co czytac
# to wyswietlamy (paczka 10 bajtów) a potem znowu wczytujemy 10 bajtów. Jezeli nic juz nie ma do czytania to exit

# instrukcja file.tell() - pokazuje gdzie jest wskaźnik (numer linii)
while fragment:
    print(file.tell(), fragment)
    fragment = file.read(10)

file.close()

# jest tez funkcja file.readline() - odczytuje pojedynczą linię w pliku