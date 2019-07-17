from datetime import date


def print_animal(*animals):
    txt_cat = r'''
        |\---/|
        | o_o |
         \_^_/'''

    txt_bear = r'''
        /  \.-"""-./  \
        \    -   -    /
         |   o   o   |
         \  .-'"'-.  /
          '-\__Y__/-'
             `---`'''

    txt_bat = r'''
           /\                 /\
          / \'._   (\_/)   _.'/ \
         /_.''._'--('.')--'_.''._\
         | \_ / `;=/ " \=;` \ _/ |
          \/ `\__|`\___/`|__/`  \/
                  \(/|\)/  
             '''

    for animal in animals:
        if animal == "cat":
            print(txt_cat)
        elif animal == "bear":
            print(txt_bear)
        elif animal == "bat":
            print(txt_bat)
        else:
            print("Correct values for the parameter are: cat, bear, bat")
            # return False

    # return True
    return

# if print_animal("cat"):
#     print("Good")
# else:
#     print("Wrong params, fuck you")
#
# if print_animal("bear"):
#     print("Good")
# else:
#     print("Wrong params, fuck you")
#
# if print_animal("bat"):
#     print("Good")
# else:
#     print("Wrong params, fuck you")
#
# if print_animal("dog"):
#     print("Good")
# else:
#     print("Wrong params, fuck you")


print_animal("cat", "dog", "bat")
print_animal("cat", "bat")

print("-----------------------------------------")


def days_new_years_eve(*dates): # year=date.today().year, month=date.today().month, day=date.today().day):

    for date_today in dates:
        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print("Date", date_today, "days to end of year", delta.days)


days_new_years_eve(date(2019,7,30))
days_new_years_eve(date(2019,5,25), date(2019,1,2))
days_new_years_eve(date(1999,1,15),date(2009,1,15),date(2019,1,15),date.today())