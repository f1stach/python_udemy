# importowanie modulu - wtedy odnosimy sie do niego przez np. math.pi
# import math tworzy nowy katalog zawierajacy funkcje w tym module. Aby z nich skorzystac nalezy podac sciezke
# import math

# ponizej importujemy wszystko co sie da z modulu math wiec nie trzeba poprzedzac funkcji nazwą math
# wszystkie funkcje umieszczamy w katalogu głównym z innymi funkcjami:
from math import *

# istnieje ryzyko, że uzywajac drugiej metody wymagane metody przykryją się jeżeli importujemy te same nazwy
from statistics import median, median_high, median_low

print(pi)
print(floor(pi))

# IMPORT MATH - BETTER TO USE IN SCRI[T
# FROM MATH IMPORT * - BETTER TO USE IN INTERACTION


# ZADANIA
print("-----------------------")
print("ZAD. 1")

percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,

           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,

           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,

           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,

           8.740978348,6.174819567]

sorted_list = sorted(percent)
print(sorted_list)


print("-----------------------")
print("ZAD. 2")

# mediana z całej listy:
print(median(sorted_list))

# wartosc elementu 13-go
print(median_low(sorted_list))

# wartosc elementu 14-go:
print(median_high(sorted_list))

