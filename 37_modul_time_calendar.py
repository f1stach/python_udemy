import time
import calendar

# time modules:

# wartosc ponizej to liczba sekund, ktore minely od 01.08.1970
print("Current time is unix epoch", time.time())
print("\n")

# localtime - w efekcie zwraca tuple z argumentów dot. czasu unixowego
print("Current time is tuple", time.localtime(time.time()))
print("\n")

# asctime - data i godzina dla czlowieka, ale nie ma mozliwosci zmiany generowania wyswietlania
print("Current time is for human", time.asctime(time.localtime(time.time())))
print("\n")

# clock - czas pobierany w oparciu o taktowanie procesora, inny niz rzeczywisty czas
print("Current time is for human", time.localtime(time.clock()))
print("\n\n\n")


# calendar modules:
# wyswietlamy kalendarz na miesiac wrzesien 2019 - na kazdy dzien 5 znakow, a odstepy rowne 2:
print("-----------------------------------------")
print(calendar.month(2019, 9, w=5, l=2))

# to co wyzej, ale bez argumentow da kalendarz bardziej kompaktowy:
print("-----------------------------------------")
print(calendar.month(2019, 9))

# wyznacz dzien tygodnia danego dnia (liczone od zera):
print("-----------------------------------------")
print("week day is", calendar.weekday(2019, 7, 11))

# ustawienie pierwszego dnia w kalendarzu
print("-----------------------------------------")
calendar.setfirstweekday(6)

# po ustawieniu pierwszego dnia na niedziele, zmienia sie wyswietlanie kalendarza,
# ale pierwszy dzien nadal jest liczony od poniedzialku (pon = 0):
print(calendar.month(2019, 9))
print("-----------------------------------------")
print("week day  is", calendar.weekday(2019, 7, 11))

# isleap - zwraca info czy rok jest przestepny
print("-----------------------------------------")
print("is 2020 a leap year?", calendar.isleap(2020))

# leapdays - pokaz liczbe dni przestepnych - koncowy zakres argumentow funkcji isleap nie jest brany pod uwage
print("-----------------------------------------")
print("Leap days 2000-2017", calendar.leapdays(2000, 2017))
print("Leap days 2000-2020", calendar.leapdays(2000, 2020))
print("Leap days 2000-2021", calendar.leapdays(2000, 2021))

# calendar.calendar - rysuje kalendarz za caly rok:
print(calendar.calendar(2020))


# ZADANIA
print("-------------------------")
print("ZAD. 1")
print("Time unix epoche: ", time.time())

print("-------------------------")
print("ZAD. 2")
print("Time for people:", time.asctime())

print("-------------------------")
print("ZAD. 3")
calendar.setfirstweekday(0)
print(calendar.month(2019,11))

print("-------------------------")
print("ZAD. 4")
calendar.setfirstweekday(6)
print(calendar.month(2019, 11))

print("-------------------------")
print("ZAD. 5")
print(calendar.isleap(2000))

print("-------------------------")
print("ZAD. 6")
print(calendar.calendar(2019))