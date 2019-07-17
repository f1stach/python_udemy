import math
import geom

# tworzymy moduł do obliczen na ciągach geometrycznych -przyjmuje 3 parametry a1 - o domyślnej wartości  2,
# która oznacza pierwszy element ciągu, factor - o domyślnej wartości 2, która oznacza współczynnik ciągu
# geometrycznego, index o domyślnej wartości 2, która oznacza  który element ciągu ma być wyliczony


print("-------------------------")
print("ZAD. 1")

print("a^64=", geom.give_geom_seq_element(1,2,64))


print("-------------------------")
print("ZAD. 2")

a1 = 3
factor = 2
maxindex = 10

for i in range(1,maxindex):
    g = geom.give_geom_seq_element(a1=a1, factor=factor, index=i)
    print("Element nr a", i, "ma wartosc", g)



print("-------------------------")
print("ZAD. 3")

print("Factor's value is", geom.give_factor_for_geom_seq(12,24))


print("-------------------------")
print("ZAD. 4")

print("Sum of elements is", geom.give_sum_of_n_elements_geom_seq(2, 3, 4))