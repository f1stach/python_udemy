'''
Zapisz swój numer buta i pomnóż przez 5. Do tego dodaj 50.
Całość pomnóż przez 20, a następnie dodaj 1019.
Odejmij od tego swój rok urodzenia. Wyszła 4cyfrowa liczba.
Pierwsze dwie cyfry to Twój numer buta a dwie ostatnie to Twój wiek.<<<
'''

shoe = 42
nr = ((shoe*5+50)*20+1019)-1992
print("shoe size is", nr //100)
print("birth date is", nr %100)

'''
Pomyśl liczbę nieujemną całkowitą. 
Pomnóż ją przez 2, dodaj 10, podziel przez 2, odejmnij początkową liczbę. 
Powinno wyjść 5 - zawsze
'''

print((15*2+10)/2-15)

'''
Ile to jest - najpierw policz sam, a potem sprawdź rozwiązanie pythona
2+2*2 = ?
7+7/7+7*7-7 = ?
'''
print(2+2*2)
print(7+7/7+7*7-7)

'''
Wykładowca mówi studentom. Zaliczysz semestr jeżeli masz obecność 
co najmniej 80% i średnią >= 3.0 lub zaliczyłeś pracę semestralną. 
Zbuduj wyrażenie w Python które stwierdzi czy student, 
który ma obecność 0.85, średnią 3.5 i nie zaliczył pracy 
semestralnej zda czy nie.
'''

sr = 2.5 # 3.5
ob = 0.4 # 0.85
sem = True # False

zal = ob >= 0.8 and sr >= 3.0 or sem == True
print("Zaliczyl?", zal) # true

zal = ob >= 0.8 and sr >= 3.0 and sem == True
print("Zaliczyl?", zal) # false