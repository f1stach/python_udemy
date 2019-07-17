"""
kontynuacja i modyfikacja przykładu z aptekami
korzystamy z 60_errors_try i 62_errors_except

w skrypcie poniżej mamy dwie kategorie błędów:
ValueError - związany z tym, że konwersja danych w trzeciej kolumnie się nie udaje
IndexError - związany z tym, że linijka ma za mało danych, po podziale linijki ze względu na przecinek otrzymujemy,
np. tylko listę dwuelementową, a potem próbujemy się odwołać do elementu spoza zakresu: orders[2]
"""

import sys

file_path = "/home/wojtek/PycharmProjects/udemy_python/files/orders.csv"

with open(file_path, "r") as file:
    for line in file:
        line = line.replace('\n', '')
        order = line.split(',')

        # ADD YOUR CODE HERE

        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])

            print("Order from drugstore %s, item %s, amount %d" % (pharmacy_name, item, amount))

        except ValueError as e:
            print("Sorry - error while data conversion in line", line, " - more info:", e)

        except IndexError as e:
            print("Sorry - not enough amount of fields in line", line, "- more info:", e)

        except:
            print("Wrong input in", line, "- error description:", sys.exc_info()[0])

print("Processing finished")