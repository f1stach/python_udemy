import os
import time

dir = input("Enter folder path: ")

if not os.path.isdir(dir):
    print("This is not a path to folder")
else:
    file = input("Enter file's name: ")
    path = os.path.join(dir, file)

    if not os.path.isfile(path):
        print("No file.")
    else:
        print("Printing file's preferences: ")
        print("Date of modification:", time.localtime(os.path.getmtime(path)))
        print("Size in bytes:", os.path.getsize(path))
        print("Current directory info:", os.getcwd())
        print("Relative path to file:", os.path.relpath(path))
