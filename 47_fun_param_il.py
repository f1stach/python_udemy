def do_action(action, parameter):
    print("action:", action)
    print("parameter:", parameter)
    return


do_action("buy", "shoes")


# gwiazdka oznacza kolekcję elementów a nie pojedynczy element więc funkcje może przyjąć więcej argumentów, które nie
# zostały wczesniej określone:

def do_action2(action, *parameter):
    print("action:", action)
    print("parameter:", parameter)
    for element in parameter:
        print("Element is", element)
    return


do_action2("buy", "shoes", "socks")
do_action2("buy", "shoes", "socks", "Tshirt")


# dwie gwiazdki - zmienna stała się słownikiem:

def do_action3(action, what, **parameter):
    print("action:", action)
    print("what:", what)
    print("parameter:", parameter)
    for element in parameter:
        print(element, "=", parameter[element])
    return


do_action3("buy", "shoes", size=45, color="brown", type="sport")