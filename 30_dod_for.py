print("ZADANIE 1")
fibonacciIterations = 20

a1 = 0
a2 = 1
a3 = 0

for number in range(fibonacciIterations):
    a1 = a2
    a2 = a3
    a3 = a1 + a2
    print(a1, "+", a2, "=", a3)


print("------------------------")
print("ZADANIE 2")
text = "Industrial Light & Magic: In this case, you find Python" \
       "used in the production process for scripting complex," \
       "computer graphic-intensive films. Originally, Industrial" \
       "Light & Magic relied on Unix shell scripting, but it was" \
       "found that this solution just couldn’t do the job. Python" \
       "was compared to other languages, such as Tcl and Perl, and" \
       "chosen because it’s an easier-to-learn language that the" \
       "organization can implement incrementally. In addition, Python" \
       "can be embedded within a larger software system as a scripting" \
       "language, even if the system is written in a language such as" \
       "C/C++. It turns out that Python can successfully interact with" \
       "these other languages in situations in which some languages can’t."

divide = text.split(" ")

for letter in divide:
    if letter.lower().find("p") >= 0:
        print(letter)

print("------------------------")
print("ZADANIE 3")

dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'}
key = dictionary.keys()

for words in key:
    print(words, "-", dictionary[words])

print("------------------------")
print("ZADANIE 4")
wordDictionary = {} # kluczem będzie słowo z tekstu a wartością ilość wystąpień słowa w tekście

listOfWords = text.split(" ")

for everyWord in listOfWords:
    if everyWord in wordDictionary.keys():
        wordDictionary[everyWord] += 1
    else:
        wordDictionary[everyWord] = 1
        # wordDictionary.setdefault(everyWord, 1)
print(wordDictionary)
