import os

# file_is_ok = False

# while not file_is_ok:
while True:
    filename = input("Enter path to results file: ")

    if os.path.isfile(filename):
        # file_is_ok = True
        break
    else:
        print("Filename is not correct, try again!")

    print("The results file is %s" % (filename))