number = 20730906
temp = number
sumDigit = 0

while temp > 0:
    before = temp
    mod = temp % 10
    sumDigit = sumDigit + mod
    temp = temp // 10  # // - to dzielenie bez reszty
    print("Modulo z", before, "to", mod)
else:
    print("Suma cyfr liczby", number, "wynosi", sumDigit)
