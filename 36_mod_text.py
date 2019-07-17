import string

line = "this IS a very STRANGE text"

# konwersja - duza litera na poczatku
print(line.capitalize())

# konwersja - kazdy wyraz zaczyna sie wielka litera
print(line.title())

# konwersja - wszystko wielkimi
print(line.upper())

# konwersja - wszystko malymi
print(line.lower())

# konwersja - kazda duza na mala a kazda mala na duza
print(line.swapcase())

# konwersja - rozpoznaje dziwne znaki jezykowe i wrzuca ich rozszerzenie + wypluwa male litery
print(line.casefold())

# zamiana dla słowa żółć - polski casefold:
line2 = "ZÓŁĆ"
print(line2.replace("Ż", "Z").replace("Ó", "O").replace("Ł", "L").replace("Ć", "C").lower())


# wystepowanie literki:
print(line.count("e"))

# na ktorym miejscu literka w zdaniu
print(line.find("e"))

# na ktorym miejscu literka w zdaniu liczac od prawej strony:
print(line.rfind("e"))

# blizniacza to find:
print(line.index("e"))

print(line.rindex("e"))

# szukamy literki, ktorej nie ma w tekscie - return wartosci -1:
print(line.find("p"))

# dla index wystapi blad
# print(line.index("p"))

# badanie czy literka jest w tekscie za pomoca wyrazenia logicznego:
print("e" in line)
print("p" in line)

# czy ciag znakow rozpoczyna sie danym wyrazem - case sensitive:
print(line.startswith("this"))
print(line.startswith("THIS"))

# czy ciag znakow konczy sie danym wyrazem:
print(line.endswith("text"))

# dlugi tekst:
line3 = """this is a long text
that spans multiple lines
but bla bla bla"""
print(line3)

print(line3.count("\n"))


# operowanie na module string:
print(string.ascii_letters)
print(string.digits)

# inny sposob generowania hasla - w oparciu o funkcje z modulu string


# split - rozbijanie wyrazu na poszczegolne wyrazy po wykryciu okreslonego znaku
list = line.split(" ")
print(list)

# join - odwrotnosc funkcji split - specyficzna funkcja wywolywana dla napisu a nie dla listy, ktora powstaje po split
# nie uzywamy join dla zmiennej list tylko dla tego co bylo argumentem split - tutaj dla spacji:
print(" ".join(list))


# ZADANIA
print("---------------")
print("ZAD. 1")
poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp am legą w prochu i pyle! '''

lines = poem.split("\n")

for i in range(8):
    print(lines[i])
    print(lines[i+8])