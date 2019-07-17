from datetime import date
from datetime import timedelta


def give_working_day(year=date.today().year, month=date.today().month, day=date.today().day):
    # najblizszy dzien roboczy

    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    # print("Working day for", day, "is", workingday)

    return workingday


# najlepiej jakby funkcja zwracala wynik aby wykorzystac go gdzie indziej - return
# zwrócona wartość zostaje przypisana do zmiennej:

nextworkingday = give_working_day(2019,7,30)
print("Next working day after", 2019,7,30, "is", nextworkingday)

nextworkingday = give_working_day()
print("Next working day after today is", nextworkingday)

# mozna tez (w przypadku tak prostego returna) wyprintowac całą funkcję:
print("Next working day after today is", give_working_day())


# ponizej pozostalosc poprzedniej wersji - tylko printujemy wynik wiec nie mozemy skorzystac z wynikow obliczen funkcji
# give_working_day()
# give_working_day(2019,8)
# give_working_day(2019)
# give_working_day(2019,7,27)
# give_working_day(year=2019, month=8, day=3)
# give_working_day(day=3, month=8, year=2019)
