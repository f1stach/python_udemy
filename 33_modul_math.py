import math

f_smaller = 3.141592653589793
f_bigger = 3.87756392764

# math.ceil - zwraca dla argumentu najmniejsza liczbe całkowitą, która jest większa od argumentu
print(math.ceil(f_smaller), math.ceil(f_bigger))
print("\n")

# math.floor - zwraca najwieksza liczbe, która jest mniejsza od podanego argumentu
print(math.floor(f_smaller), math.floor(f_bigger))
print("\n")

print(math.ceil(-f_smaller), math.ceil(-f_bigger))
print("\n")

print(math.floor(-f_smaller), math.floor(-f_bigger))
print("\n")

print(pow(2, 8), pow(9, 0.5))
print("\n")

print(math.sqrt(16))
print("\n")

print(math.pi, math.e)
print("\n")

print(math.sin(math.pi/2), math.cos(math.pi/4))
print("\n")


# ZADANIA
print("-----------------------")
print("ZAD. 1")

degree = 360
degree2 = 45
conv_deg = (degree * math.pi) / 180
print(conv_deg)
conv_deg2 = (degree2 * math.pi) / 180
print(conv_deg2)


print("-----------------------")
print("ZAD. 2")

print(math.radians(degree))
print(math.radians(degree2))


print("-----------------------")
print("ZAD. 3")
small_pizza_r = 22
big_pizza_r = 27
family_pizza_r = 38
small_pizza_price = 11.5
big_pizza_price = 15.6
family_pizza_price = 22

small_pizza_area_cm = math.pi*pow(small_pizza_r, 2)
big_pizza_area_cm = math.pi*pow(big_pizza_r, 2)
family_pizza_area_cm = math.pi*pow(family_pizza_r, 2)

print("Small pizza area:", small_pizza_area_cm)
print("Big pizza area:", big_pizza_area_cm)
print("Family pizza area:", family_pizza_area_cm)


print("-----------------------")
print("ZAD. 4")

small_area_m = small_pizza_area_cm/10000
big_area_m = big_pizza_area_cm/10000
family_area_m = family_pizza_area_cm/10000

print(small_area_m)
print(big_area_m)
print(family_area_m)


print("-----------------------")
print("ZAD. 5")

small_price_m = (small_pizza_price * 10000) / small_pizza_area_cm
big_price_m = (big_pizza_price * 10000) / big_pizza_area_cm
family_price_m = (family_pizza_price * 10000) / family_pizza_area_cm

print(small_price_m)
print(big_price_m)
print(family_price_m)


print("-----------------------")
print("ZAD. 6")
math_ls = dir(math)
print(math_ls)


print("-----------------------")
print("ZAD. 7")

small_area = math.pi * small_pizza_r ** 2
big_area = math.pi * big_pizza_r ** 2
family_area = math.pi * family_pizza_r ** 2

print('small', small_pizza_r, small_pizza_price, small_area)
print('big', big_pizza_r, big_pizza_price, big_area)
print('family', family_pizza_r, family_pizza_price, family_area)
print('')
print('small', small_pizza_price / small_area)
print('big', big_pizza_price / big_area)
print('family', family_pizza_price / family_area)
print('')