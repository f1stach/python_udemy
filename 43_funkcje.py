from datetime import date
from datetime import timedelta


# PRZED:
# def give_working_day(year, month=1, day=1):

# PO:
def give_working_day(year=date.today().year, month=date.today().month, day=date.today().day):
    # najblizszy dzien roboczy

    # day = date.today()
    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print("Working day for", day, "is", workingday)

    return


# w najnowszej wersji funkcja przyjmuje parametry dot. daty dzisiejszej więc mozna nawet wywołać funkcje bez param.:
give_working_day()

# jezeli w wywolaniu mamy pominąć jeden parametr, ale znamy domyslną wartość, którą można przyjąć w zamian
# to wpisujemy tę wartość domyślną do argumentu zdefiniowanego przy utworzonej funkcji (czyli tutaj u góry dopisałem
# day=1) a funkcje mozemy wywołać bez tego argumentu (poniżej). Ale wrzucając konkretny argument będzie ok, 1 nadpisana
give_working_day(2019,8)
give_working_day(2019)

# wywolanie funkcji przez PRZEKAZANIE POZYCJI PARAMETRÓW DO FUNKCJI:
give_working_day(2019,7,27)

# wywolanie funkcji przez PRZEKAZANIE NAZW PARAMETRÓW DO FUNKCJI
# nie trzeba pamietac kolejnosci parametrow, wystarczy kojarzyc nazwy i mozna mieszac miejsca argumentow:
give_working_day(year=2019, month=8, day=3)
give_working_day(day=3, month=8, year=2019)
