"""
adanie zautomatyzowania pobierania danych dotyczących zamówień kierowanych z aptek do dystrybutora leków. Zamówienia
są przesyłane w postaci plików CSV  i umieszczane w katalogu c:\temp\data_input. Pliki są tam umieszczane przez różne
inne procesy w ciągu całego dnia. Codziennie o godzinie 19:00 będzie uruchamiany skrypt, który przeniesie te pliki do i
nnego folderu, np c:\temp\yyyy-mm-dd (gdzie yyyy to rok, mm to miesiąc, a dd to dzień z daty dzisiejszej). Potem na
tych plikach są wykonywane dalsze operacje, jak np. import danych.
"""

# spr. warunki uruchomienia przetwarzania

import os
import time, datetime

file_path = "/home/wojtek/PycharmProjects/udemy_python/files/orders.csv"

data_input_catalog = "/home/wojtek/PycharmProjects/udemy_python/files/data_input"
data_output_catalog = "/home/wojtek/PycharmProjects/udemy_python/files/data_output"

today = datetime.date.today()

expr = today.strftime("%Y-%m-%d")
today_output_catalog = os.path.join(data_output_catalog, expr)

is_input_catalog_ok = os.path.isdir(data_input_catalog)
is_output_catalog_ok = os.path.isdir(data_output_catalog)

is_today_output_catalog_ok = not(os.path.isdir(today_output_catalog)) and not(os.path.isfile(today_output_catalog))

if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
    print("Conditions met! We can continue!")
else:
    print("Error with catalogs.")
    if not is_input_catalog_ok:
        print("No input catalog %s" % data_input_catalog)
    elif not is_output_catalog_ok:
        print("No output catalog %s" % data_output_catalog)
    elif not is_today_output_catalog_ok:
        print("Today's output catalog cannot exist %s" % today_output_catalog)

with open(file_path) as file:
    for line in file:
        line = line.replace("\n", " ")
        order = line.split(",")

        if len(order) == 3:
            print("Order from drugstore %s , item %s, amount %s" %(order[0], order[1], order[2]))
        else:
            print("Line %s malformed!!!" % line)
        # print(order)

print("Processing completed.")
