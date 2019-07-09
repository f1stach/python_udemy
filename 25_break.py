# break - przerywa pętle
for candidate in range(2,31):
    # isPrime = True
    for divider in range(2, candidate):
        if candidate % divider == 0:
            # isPrime = False
            print("%2d is not a prime number - divider is %2d" % (candidate, divider))
            break # nie ma juz sensu szukac kolejnych dzielnikow badanej liczby wiec zrywamy wewnetrzna petle
#    if isPrime:
    else:
        print("%2d is prime!" %(candidate))

# w przypadku zerwania ifa instrukcją break, else nie wykona się
# w przypadku gdy for nie została zerwana (zakonczyła się), else wykona się


print("----------------------------------")
print("ZADANIE 1")
text = 'Mechanical advantage is a measure of the force amplification ' \
       'achieved by using a tool, mechanical device or machine system. ' \
       'The device preserves the input power and simply trades off forces ' \
       'against movement to obtain a desired amplification in the output ' \
       'force. The model for this is the law of the lever. Machine' \
       'components designed to manage forces and movement in this way are ' \
       'called mechanisms.[1] An ideal mechanism transmits power without ' \
       'adding to or subtracting from it. This means the ideal mechanism ' \
       'does not include a power source, is frictionless, and is constructed ' \
       'from rigid bodies that do not deflect or wear. The performance ' \
       'of a real system relative to this ideal.'

words = text.split(" ")
short_text = ""
counter = 0

for every_word in words:
    short_text = short_text + every_word + " "
    counter = counter + 1
    # print(short_text)
    if counter >= 20:
        print(short_text)
        break

print("----------------------------------")
print("ZADANIE 2")
definitions = [
    'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.',
    'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt, ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
    'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando un mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para contrarrestar una carga de resistencia.',
    'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale dans les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une force importante transmise au système de freinage pour une course de faible distance.'
    ]

for definition in definitions:
    words = definition.split(" ")
    short_text = ""
    counter = 0

    for every_word in words:
        short_text = short_text + every_word + " "
        counter = counter + 1
        # print(short_text)
        if counter >= 20:
            print(short_text)
            break
