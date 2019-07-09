numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

x = 0
max = len(numbers)-1
max2 = len(numbers)-2

while x < max2:
    print(x, numbers[x], numbers[x+1], numbers[x+2])
    if numbers[x]*numbers[x] == numbers[x+1] and numbers[x+1]*numbers[x+1] == numbers[x+2]:
        print("\tFound!", numbers[x], numbers[x+1], numbers[x+2])

    x = x+1


while x < max:
    print(x, numbers[x], numbers[x+1])

    if numbers[x+1] == numbers[x]*numbers[x]:
        print("\tFound!",numbers[x], numbers[x+1])

    x = x+1

