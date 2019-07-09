for x in range(1,6):
    line = str(x)
    for y in range(1,6):
        line += ("\t%3d" % (x*y))
    print(line)


print("-------------------------")
print("ZADANIE 1")

i = 10
result = 1

for x in range(1, i+1):
    result = result * x
print(i, "! = ", result)


print("-------------------------")
print("ZADANIE 2")

x = 10
for i in range(1,x+1):
    res = 1
    for j in range(1, i+1):
        res = res*j
    print(i, "! =", res)


print("-------------------------")
print("ZADANIE 3")

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for x in list_adj:
    for y in list_noun:
        print(x, y)