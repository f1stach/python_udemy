number = 1
previousNumber = 0

while number < 50:
    print(previousNumber, "+", number, "=", number + previousNumber)
    previousNumber = number
    number = number + 1