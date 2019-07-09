text = "United Space Alliance: This company provides major " \
       "support to NASA for various projects, such as the " \
       "space shuttle. One of its projects is to create Workflow Automation System (WAS), an application designed to" \
       "manage NASA and other third-party projects. The setup " \
       "uses a central Oracle database as a repository for " \
       "information. Python was chosen over languages such " \
       "as Java and C++ because it provides dynamic typing " \
       "and pseudo-code–like syntax and it has an interpreter." \
       "The result is that the application is developed faster, and unit testing each piece is easier."

wordLength = 6
shortWords = 0
longWords = 0

listOfWords = text.split(" ")
i = 0

while i < len(listOfWords):
    if wordLength < len(listOfWords[i]):
        longWords = longWords + 1
    elif len(listOfWords[i]) > 0:
        shortWords = shortWords + 1
    i = i+1
print("Krótszych niz", wordLength, "jest", shortWords)
print("Dluzszych niz", wordLength, "jest", longWords)