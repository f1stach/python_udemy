values = [10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]

i = 0 # wskazywac bedzie na dana aktualizowana liczbe
max = len(values)-2 # dlugosc listy - 15 elementow odjac 2, bo musimy zatrzymac sie na liczbie 49

while i < max:
    print(i, values[i], values[i+1], values[i+2])

    if values[i] < values[i+1] and values[i+1] < values[i+2]:
        print("\tFound:", values[i], values[i+1], values[i+2])

    i += 1
