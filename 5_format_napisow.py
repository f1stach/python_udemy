# wskazac literal podczas przetwarzania pliku. s jak string
message1 = "Processing file %s"
print(message1 % ('file_1.txt'))

message2 = "File %s has size %d KB"
print(message2 % ('file1.txt', 100))

# wskazanie ile znakow ma byc przeznaczone na napis i wart liczbowa
message3 = "File %20s has size %10d KB"
print(message3 % ('file1.txt', 100)) # miejsce zarezerwowane - 20 dla s i 10 dla d

# nowy sposob:
message4 = "Processing file {0:s}" # 0 oznacza, ze spodziewamy sie jednego parametru - napisu
print(message4.format('file1.txt'))

message5 = "File {0:s} has size {1:d} KB" # 0 - miejsce zerowe, 1 - miejsce pierwsze
print(message5.format('file1.txt',100))

message5 = "File {1:s} has size {0:d} KB" # 0 - miejsce zerowe, 1 - miejsce pierwsze
print(message5.format(100, 'file1.txt')) # format nie musi trzymac sie kolejnosci

message6 = "File {0:20s} has size {1:10d}"
print(message6.format('file1.txt', 100))

# zadania:
helloMessage = "Hello %s!"
print(helloMessage % ('Kate'))
print(helloMessage % ('Chris'))

helloMessage = "Hello {0:s}!"
print(helloMessage.format('Kate'))
print(helloMessage.format('Chris'))

helloMessage = "%s has %d %s"
print(helloMessage % ('Kate', 1, 'animal'))
print(helloMessage % ('Chris', 100000, '$'))

helloMessage = "{0:s} has {1:d} {2:s}"
print(helloMessage.format('Kate', 1, 'animal'))
print(helloMessage.format('Chris', 100000, '$'))

line = "%20s costs %6d €"
print(line % ('ICE CREAM', 3))
print(line % ('Trip to Venice', 119))
print(line % ('Pizza Hawaii', 6))

line = "{0:20s} costs {1:6d} €"
print(line.format("ICE CREAM", 3))
print(line.format("Trip to Venice", 119))
print(line.format('Pizza Hawaii', 6))

