# w pythonie nie ma funkcjonalności switch znanej z innych jezyków. Substytut to dictionary:

def weekday_french(day_number):
    names = {
        0: "lundi",
        1: "mardi",
        2: "mercredi",
        3: "jeudi",
        4: "vendredi",
        5: "samedi",
        6: "dimanche"
    }

    # metoda get ma wybrac day_number z names a jak nic nie znajdzie to wyswietli error
    return names.get(day_number, "error")


print(weekday_french(5))
print(weekday_french(7))
