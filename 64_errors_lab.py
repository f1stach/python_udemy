import os

line = input("What is the acceptable price of Udemy course: ")

file_path = input("Provide file path: ")

try:
    file = open(file_path, "w")
    file.write(line)
    file.close()

    value = int(line)
    print("The value saved in file is", value)

except FileNotFoundError as e:
    print("Error opening file - ", file_path, "-", e)

except ValueError as e:
    print("The value entered cannot be converted to a number -", line, "-", e)

except IsADirectoryError as e:
    print("This is a directory. Please point the file name -", e)

except:
    print("Sorry - we have an error")

else:
    print("Actions completed successfully")

"""
Provide file path: /home/wojtek/PycharmProjects/udemy_python
Traceback (most recent call last):
  File "/home/wojtek/PycharmProjects/udemy_python/64_errors_lab.py", line 7, in <module>
    file = open(file_path, "w")
IsADirectoryError: [Errno 21] Is a directory: '/home/wojtek/PycharmProjects/udemy_python'
"""