import datetime

# datetime zaklada, ze kalendarz byl taki sam na przestrzeni lat
# datetime nie jest swiadomy sekund przestepnych, ale to nie szkodzi

# potezniejszy modul, ponizej np. zobaczymy min i max wartosc roku - nie ma tu unix epoch
print("Min and max", datetime.MINYEAR, datetime.MAXYEAR)

# timedelta - wylicza roznice czasu. Wektor czasu, o jaki nalezy przesunac sie do przodu lub do tylu
d1 = datetime.timedelta(days=1, hours=2, minutes=-30)
print(d1)

d2 = datetime.timedelta(days=-1, hours=-2, minutes=-3)
print(d2)

print("timedelta sum:", d1+d2)
print("------------------------------\n\n")


# typ date - zajmuje sie datą

print("Today is", datetime.date.today())
print("\n")

today = datetime.date.today()
days_to_pay = datetime.timedelta(days=7)
print("Today is", today)
print("Bills should be paid within", days_to_pay.days, "days")
print("The bill should be paid till", today+days_to_pay)
print("\n")


endOfTheWorld = datetime.date.max
print("The final end of world will hapen - by Python:", endOfTheWorld)
print("Weekday:", endOfTheWorld.weekday())
print("\n")

# ponizej czesc godzinowa i minutowa jest zerowa, bo typ date zwraca tylko to co dotyczy dni
bornDate = datetime.date(2000, 8, 15)
today = datetime.date.today()
print(today - bornDate)
print("\n")
print("--------------------------")


# modul datetime:
# pierwsze datetime to nazwa modulu, drugie datetime to nazwa typu - datetime
# mozna tez zaimportowac from datetime import datetime

# now - zwraca date i godzine
print("now()\t", datetime.datetime.now())

# today - zwraca to co now
print("today()\t", datetime.datetime.today())

# utcnow - zwraca czas greenwich
print("utcnow()\t", datetime.datetime.utcnow())

# weekday - zwraca numer dnia tygodnia, liczony od 0 dla poniedziałku
print("weekday()\t", datetime.datetime.today().weekday())
print("\n")

# strftime - konwersja czasu do napisu
# %a - skrocona nazwa dnia tygodnia
print("%a", datetime.datetime.now().strftime("%a"))

# %A - pelna nazwa dnia
print("%A", datetime.datetime.now().strftime("%A"))

# %w - numer dnia tygodnia, numerowany od 1
print("%w", datetime.datetime.now().strftime("%w"))

# spinanie argumentow razem:
print("%a %A %w", datetime.datetime.now().strftime("%a %A %w"))

# %f - milisekundy
print("%Y-%m-%d_%H_%M_%S_%f", datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f"))
