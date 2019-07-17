import math

# ZADANIA
print("----------------------------")
print("ZAD. 1")

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

print("Number of elements in inputdata:", len(inputdata))
print("Number of elements in factorable:", len(factortable))

if len(inputdata) == len(factortable):
    i = 0
    for n in inputdata:
        for m in factortable:
            # minvalue = n - m * n
            # maxvalue = n + m * n

            minvalue = inputdata[i] - factortable[i] * inputdata[i]
            maxvalue = inputdata[i] + factortable[i] * inputdata[i]

        print("Wartosc min.:", minvalue)
        print("Wartosc max.:", maxvalue)

        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)

        print("Biggest int less than", minvalue, ":", mininteger)
        print("Smallest int bigger than", maxvalue, ":", maxinteger)

        i += 1

else:
    print("inputdata and factortable need to have equal number of elements")


print("----------------------------")
print("ZAD. 2")

import random

i = 0
for n in inputdata:
    for m in factortable:
        # minvalue = n - m * n
        # maxvalue = n + m * n

        minvalue = inputdata[i] - random.random() * inputdata[i]
        maxvalue = inputdata[i] + random.random() * inputdata[i]

    print("Wartosc min.:", minvalue)
    print("Wartosc max.:", maxvalue)

    mininteger = math.floor(minvalue)
    maxinteger = math.ceil(maxvalue)

    print("Biggest int less than", minvalue, ":", mininteger)
    print("Smallest int bigger than", maxvalue, ":", maxinteger)

    i += 1

print("----------------------------")
print("ZAD. 3")

import datetime

print(datetime.datetime.today())

date = datetime.datetime.now().strftime("%Y-%m-%d")

print("Today is", date)
