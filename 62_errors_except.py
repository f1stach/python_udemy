"""
c.d. z 60_errors_try: tutaj dowiemy się jak zróżnicować obsługę błędów w zależności od rodzaju błędu w skrypcie
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

print("Every person should have around", tasksPerPerson, "tasks")

