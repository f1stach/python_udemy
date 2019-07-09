persons = ["Elizabeth", "Steven", "Sebastian", "Margaret", "Svetlana", "Raphael"]

domain = "mycompany.com"

for person in persons:
    email = person + "@" + domain
    print("Email for\t", person, "\tis\t", email)
else:
    print("--end of the list--")

print("--------------------------")
print("ZADANIE 1")

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for letters in data:
    print(letters.upper())


print("------------------------")
print("ZADANIE 2")

for letters in data:
    elements = letters.split(":")
    print(elements[0].upper())
    print(elements[1])


print("------------------------")
print("ZADANIE 3")

for letters in data:
    elements = letters.split(":")
    if elements[0] == "Error":
        print(elements[1].upper())
    else:
        print(elements[1])