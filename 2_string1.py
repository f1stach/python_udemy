atext = "This is a text"
atext.endswith('ext')
print(atext.endswith('ext'))
print(atext.islower())
print(atext.upper())
print(atext.upper().isupper())
print(atext.find("is"))
print(atext.replace("a","4"))
print(atext.replace("a", "4").replace("i", "l").replace("e", "3"))
print(atext.split(" "))

smthLikeNumber = "1000"
# smthLikeNumber = smthLikeNumber+1
print(smthLikeNumber)
print(smthLikeNumber.isdigit())
print(smthLikeNumber.isdecimal())
print(smthLikeNumber.isalpha())
print(smthLikeNumber.isalnum())

# zadania:
# Utwórz zmienną quote i przypisz jej następującą wartość:   'A good programmer is someone who always looks both ways before crossing a one-way street'
quote = "A good programmer is someone who always looks both ways before crossing a one-way street"

# Wyświetl tekst napisany tylko wielkimi literami
print(quote.upper())

# Wyświetl tekst zapisany tylko małymi literami
print(quote.lower())

# Sprawdź czy tekst kończy się słowem 'street'
print(quote.endswith("street"))

# Sprawdź czy tekst jest zapisany wielkimi literami
print(quote.isupper())

# Sprawdź, czy tekst skonwertowany do wielkich liter jest zapisany wielkimi literami (Zastosuj złożenie funkcji)
print(quote.upper().isupper())

# Poszukaj na której pozycji (licząc od zera) znajduje się w tekście słowo 'one'
print(quote.find("one"))

# Zamień w tekście słowo 'one' na '1'
print(quote.replace("one", "1"))

# Zamień w tekście słowo 'one' na '1' a słowo 'both' na 2
print(quote.replace("one", "1").replace("both", "2"))

# Rozdziel napis na mniejsze napisy ze względu na znak rozdzielający jakim jest spacja
print(quote.split(" "))

# Sprawdź czy napis jest liczbą, liczbą dziesiętną, napisem bez cyfr, napisem z literami i cyframi
print(quote.isdigit())
print(quote.isdecimal())
print(quote.isalpha())
print(quote.isalnum())