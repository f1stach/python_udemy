# tuple = krotka - lista statyczna - nie mozna jej zmieniac z definicji

Tax = (4, 7, 8, 23)
print(Tax[-1])
print(Tax.index(7)) # na której pozycji wartosc 7
print(Tax.count(8)) # ile razy 8 wystepuje w statycznej liscie
print(max(Tax)) # jaka max. wartosc wystepujaca w Tax

# zmiana krotek funkcjami jak w listach, typu sort itp. nie jest mozliwa
# Tax.sort()

print(Tax)

# konwersja na liste:
TaskList = list(Tax)

# tablice poszerzamy i zamieniamy na krotke:
TaskList.append(30)
NewTax = tuple(TaskList)

print(TaskList) # wyswietlona zawartosc jest w nawiasach kwadratowych
print(NewTax)

# ale wartosc z krotki mozna przypisac innym zmiennym:
(tax1, tax2, tax3, tax4) = Tax
print(tax1, tax2, tax3, tax4)

# zamiana wartosci zmiennych
a = 1
b = 10
print("a =", a, "\tb =", b)

# a = b
# b = a
print("a =", a, "\tb =", b)

# temp = a
# a = b
# b = temp
print("a =", a, "\tb =", b) # dziala spoko

# inne podejscie:
(a,b) = (b,a)
print("a =", a, "\tb =", b)


# zadania:
marketing = ["loyality program", "client promotion", "market research"]
marketing.append("public relations")
print(marketing[3])

marketing.insert(2, "investor relations")

emailMarketing = marketing.copy()
emailMarketing.sort()

internalEmails = ["internal communication"]
emailMarketing.extend(internalEmails)

email = tuple(emailMarketing)

print(marketing)
print(emailMarketing)
print(email)