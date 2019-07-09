smthLikeNumber = "1000"
print(smthLikeNumber)

# error, bo dwa rozne typy:
# smthLikeNumber + 1

# rzutowanie na liczbe:
print(int(smthLikeNumber) + 1)

# rzutowanie liczby na string:
print(smthLikeNumber + str(1))

# funkcja type zwraca typ uzytej zmiennej:
print(type(smthLikeNumber))
print(type(int(smthLikeNumber)))

# zad.:
'''
https://en.wikipedia.org/wiki/Monty_Python
'''

article = "Monty Python (also collectively known as " \
          "the Pythons)[2][3] were a British surreal comedy " \
          "group who created their sketch comedy show Monty Python's " \
          "Flying Circus, which first aired on the BBC in 1969."

print(article.upper())
print(article.lower().replace("monty", "flying"))
print(article.split(" "))
print("Word python appears", article.lower().count("python"), "times")
print("To print the \ you need to put \ twice in your text like this: \\")
print('The best hits of \'80s!!!')
print("The best hits of '80s!!!")

# zad. - mini kalkulator
amountPLN = 234
amount = amountPLN
print("cur", "\texchange", "amount")
print("USD", "\t3.65\t", amountPLN/3.65)
print("EUR", "\t4.23\t", amountPLN/4.23)

ValueAsText = "123.45"
factor = 1.23
print("value is", ValueAsText, "factor is", factor, "value*factor=", float(ValueAsText)*factor)