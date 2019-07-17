"""
c.d. z 62_errors_except: tutaj dowiemy się jak zróżnicować obsługę błędów w zależności od rodzaju błędu w skrypcie
"""

import sys

try:
    tasksPerPerson = 0
    tasks = 32

    personsStr = input("How many persons are there in the team? ")
    persons = int(personsStr)

    tasksPerPerson = tasks / persons

# można okreslic konkretny moment wywołania instrukcji except w zależności od rodzaju błędu, jak nizej.
# dodatkowo warunek dla except może byc uzyty jako zmienna w dalszej części - dopisujemy as e.
except ValueError as e:
    print("Sorry - you need to enter an integer number:", e)

except ZeroDivisionError as e:
    print("Sorry - you need to enter value > 0:", e)

except:
    print("Something went wrong...", sys.exc_info()[0])

# jezeli do zadnego błędu w instrukcji try nie doszło to mozna uzyc bloku else - instrukcje tutaj zostaną wykonane
# gdy nie dojdzie do błędu w try:
else:
    print("Every person should have around", tasksPerPerson, "tasks")

# blok finally - wszystkie instrukcje  tutaj umieszczone zostaną wykonane niezależnie od tego czy doszło do błędy
# czy nie, np. zamykamy otwarte pliki, wysłac maila, zapisac raport, dac info userowi itp.
finally:
    print("Script finished with/without errors")
