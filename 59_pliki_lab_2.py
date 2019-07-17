"""
tutaj wczytasz i przeanalizujesz plik utworzony w poprzednim zadaniu
"""

import os

filename = input("Enter file path with web addresses: ")

while not os.path.isfile(filename):
    print("File does not exist")
    filename = input("Enter file path once again: ")

webaddresses = []

with open(filename, "r") as file:
    for line in file:
        webaddresses.append(line.replace("\n", ""))

dirname = os.path.dirname(filename)
web_pl_path = os.path.join(dirname, "webs_pl.txt")
web_other_path = os.path.join(dirname, "webs_other.txt")

open_pl = open(web_pl_path, "w")
open_other = open(web_other_path, "w")

for line in webaddresses:
    if line.endswith(".pl"):
        print("Adres " + line + " jest adresem z Polski")

        open_pl.write(line + "\n")

    else:
        print("Adres " + line + " nie jest adresem z Polski")

        open_other.write(line + "\n")

open_pl.close()
open_other.close()