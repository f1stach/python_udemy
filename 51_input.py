# aplikacja pyta o sciezke do pliku. Mogę podać ją wpisując "C:\plik" a python automatycznie zmieni pojedynczy backslash
# na podwójny. To się dzieje w oparciu o funkcję input od v3. W v2 pythona należało uzywać raw_input

# filename = input("Enter filename: ")
# print("The file name is %s" % filename)


# wszystko co przeczyta input to string! w ponizszym przykladzie trzeba rzutowac albo zmienic odczyt z %d na %s

# filesize = input("Enter the max file size (MB): ")
# # print("The max size is %d" % filesize)
# print("The max size is %s" % (filesize))
# print("Size in KB is %s" % (filesize*1024))


# aby uniknąć powyzszego, należy przejsc proces konwersji + dorzucamy info o złych danych

while True:
    filesizeStr = input("Enter the max file size (MB): ")

    if filesizeStr.isdecimal():
        filesizeInt = int(filesizeStr)
        break

print("The max size is %d" % (filesizeInt))

print("Size in KB is %d" % (filesizeInt*1024))
