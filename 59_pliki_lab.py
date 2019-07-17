"""
program  zapyta użytkownika o adresy www i zapisze je w pliku.
"""

import os
webaddresses = []

line = input("Enter website address: ")

# pętla która będzie się wykonywać tak długo  póki line nie jest puste
while line != "":
    webaddresses.append(line)
    line = input("Enter website address: ")

print(webaddresses)
dirname = os.getcwd()

filename = input("Enter file's name: ")

filepath = os.path.join(dirname, filename)

file = open(filepath, "a")
for string in webaddresses:
    file.write(string + "\n")

file.close()
