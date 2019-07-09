import sys

print(8*3)
five = 5
three = 3
print(five*three)
print(type(five))
print(type(five*three))
print(type(five/three))

print(sys.maxsize)
veryBigValue = 99999999999999999999999999999999999999999999999
print(veryBigValue)
print(veryBigValue+1)
print(type(veryBigValue))
print((veryBigValue+1)/2)
print(type((veryBigValue+1)/2))
print(five//three) # dzielenie całkowite. Wynik to ilosc trojek mieszczacych sie w 5
print(five % three) # reszta z dzielenia
print(float('inf')) # to jest zapis oznaczajacy nieskonczonosc - inf
print(float('inf') > 999999999999999999999999999999999999999999999)
print(-float('inf')) # minus nieskonczonosc


# zadania:
name = "Wojtek"
age = 38
daysInYear = 365
message = "%s is %d years old, so is about %d days old"
print(message % ("Jan", 26, 9490))
print(message % (name, age, daysInYear))

message = "{0:s} is {1:d} years old, so is about {2:d} days old"
print(message.format('Chris', 17, 6205))

num1 = 1234567890
num2 = 12345
div = 1234567890/12345
mod = div % 12345
print(num1, "divided by", num2, "is", div, "and the rest is", mod)