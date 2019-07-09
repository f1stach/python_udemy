# Zad 1
print("ZADANIE 1")
firstRow = 1
lastRow = 31
currentRow = firstRow

while currentRow <= lastRow:
    print("Row number", currentRow)
    currentRow = currentRow + 1


print("---------------")
print("ZADANIE 2")
firstNum = 1
lastNum = 13
currNum = firstNum

while currNum <= lastNum:
    print("Kwadrat", currNum, "to", currNum**2)
    print("Szescian", currNum, "to", currNum**3)
    currNum = currNum + 1


print("------------------")
print("ZADANIE 3")
x = 0
y = 16

while x <= y:
    print("2 do potegi", x, "to", 2**x)
    x+=1


print("------------------")
print("ZADANIE 4")
x = 1
y = 10

while x <= y:
    print(x*"x")
    x+=1