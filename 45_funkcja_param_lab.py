def print_animal(animal=""):
    txt_cat = r'''
        |\---/|
        | o_o |
         \_^_/'''

        # print(txt)

    txt_bear = r'''
        /  \.-"""-./  \
        \    -   -    /
         |   o   o   |
         \  .-'"'-.  /
          '-\__Y__/-'
             `---`'''

        # print(txt)

    txt_bat = r'''
           /\                 /\
          / \'._   (\_/)   _.'/ \
         /_.''._'--('.')--'_.''._\
         | \_ / `;=/ " \=;` \ _/ |
          \/ `\__|`\___/`|__/`  \/
                  \(/|\)/  
             '''

        # print(txt)

    if animal == "cat":
        print(txt_cat)
    elif animal == "bear":
        print(txt_bear)
    elif animal == "bat":
        print(txt_bat)
    else:
        # print("Cannot print %s. Correct values for the parameter are: cat, bear, bat" % animal)
        print("Correct values for the parameter are: cat, bear, bat")
        return False

    return True

# print_animal()
# print_animal("cat")
# print_animal(animal="bat")
# print_animal(animal="dog")


if print_animal("cat"):
    print("Good")
else:
    print("Wrong params, fuck you")

if print_animal("bear"):
    print("Good")
else:
    print("Wrong params, fuck you")

if print_animal("bat"):
    print("Good")
else:
    print("Wrong params, fuck you")

if print_animal("dog"):
    print("Good")
else:
    print("Wrong params, fuck you")