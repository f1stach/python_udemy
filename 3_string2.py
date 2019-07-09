# lekcja - konkatenacja stringów
drive = "c:\\"
folder = "scripts\\python\\"
file = "myscript.py"
path = drive + folder + file
print(path)

justText = "text with \nnewline"
print(justText)

# wyswietl raw text (bez formatowania)
justText = r"text with \nnewline"
print(justText)

# dla ponizszego pojedynczy apostrof generuje blad
justText = "Mc Donald's"
print(justText)

justText = 'Mc Donald\'s'
print(justText)

line = 'He said "I like python!"'
print(line)

# zad. 1:
firstName = "Kasia"
familyName = "Sowa"
lastName = "Mrugala"

newName = firstName + " " + familyName + " " + lastName
print(newName)

# zad. 2:
# music = '"Universal Fanfare" Jerry Goldsmith', '"Happy Together" Garry Bonner', '"I\'m a Man"	Steve Winwood'
music = '"Universal Fanfare" Jerry Goldsmith \n"Happy Together" Garry Bonner \n"I\'m a Man" Steve Winwood'
print(music)

# zad. 3:
print("(\(\\")
print("( -.-)")
print("0_(\")(\")")