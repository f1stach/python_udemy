"""
python widząc błedy wywali wielkie info, ze cos tam nie działa. Trzeba wziąć skrypt, znaleźc błedy i naprawić.

Mozna tez dodac tzw. obsługę wyjątków.

jezeli do ponizszego skryptu damy liczbe w formie stringa to python powie, że:
ValueError: invalid literal for int() with base 10: 'one'

Jest to wyjątek, który można obsłuzyć instrukcją try. W miejscu, w którym spodziewamy się błędy wpisać try: - wtedy
podejrzane instrukcje będa w jednym bloku i w przypadku wystąpienia błędu zostanie uruchomione instrukcja zapisana
w except: a nie inne instrukcje

Istnieje możliwość rozpoznania rodzaju błędu - w instrukcji w bloku except dodac sys.exc_info()[0]
"""

# instrukcja ponizej wyrzuci błąd syntaxu
# print "this is a message"

import sys


try:
    tasksPerPerson = 0
    tasks = 32

    personsStr = input("How many persons are there in the team? ")
    persons = int(personsStr)

    tasksPerPerson = tasks / persons

except:
    print("Something went wrong...", sys.exc_info()[0])

print("Every person should have around", tasksPerPerson, "tasks")

