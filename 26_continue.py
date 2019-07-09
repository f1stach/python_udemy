# continue sprawi, że program przeskoczy do wybranego miejsca w kodzie

persons = ["Elizabeth", "Steven@sales.mycompany.com", "Sebastian", "Margaret", "Svetlana@mycompany.eu", "Raphael"]

domain = "mycompany.com"
emails = []

# sposob nr 1:
"""
for person in persons:
    if "@" in person:
        emails.append(person)
    else:
        email = person + "@" + domain
        emails.append(email)
"""

# sposob nr 2:

for person in persons:
    if "@" in person:
        emails.append(person)
        continue    # jezeli jest malpka to wraca do poczatku petli. Inaczej jedzie do instrukcji ponizej

    email = person + "@" + domain
    emails.append(email)

for email in emails:
    print(email)


print("----------------------------------")
print("ZADANIE 1")
menu = '''
Choose what you want me to do for you:
1 - COFFEE
2 - TEA
3 - MAKE ME SMILE
---------------
To stop this script select 0
'''

smile = '''

                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                                o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$
                                """"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$"
                                      "$$$""""
'''

while True:
    print("Dostepne opcje:", menu)
    letter = int(input())

    if letter == 1:
        print("Function COFFEE not implemented. Press Enter")
        input()
        continue

    if letter == 2:
        print("Function TEA not implemented. Press Enter")
        input()
        continue

    if letter == 3:
        print(smile)
        print("Press Enter")
        input()
        continue

    if letter == 0:
        break

    input("You need to make a valid choice. Press ENTER and try again!")