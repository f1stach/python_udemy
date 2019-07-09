CountryLeaders = {"PL":"Duda", "US":"Trump"}

print(CountryLeaders["US"])

CountryLeaders["DE"] = "Merkel"

print(CountryLeaders.keys())
print(CountryLeaders.items())
print(CountryLeaders.values())
print("----------")

# popitem - destruktywna iteracja po słowniku
print(CountryLeaders.popitem()) # pobierze 1 z elementow dict, zwróci go i usunie z listy

# setdefault - jezeli nie ma wartosci to zostanie dodana
print(CountryLeaders.setdefault("FR", "Macron"))

# get - ponizej jest tylko key bez value więc nowa wartosc nie zostanie dodana
print(CountryLeaders.get("RU"))

NewLeaders = {"RU":"Putin", "DE":"Schulz"}
print(NewLeaders)
CountryLeaders.update(NewLeaders) # update dodaje nowe wartości i aktualizuje te, które są juz w dictionary (vide DE)

print(CountryLeaders)


# zadania
print("-------------------------")
print("ZADANIA")

chanels = {"Google":1480, "Email":300, "Natural Traffic":440, "TV Spot":700}
print(chanels["Email"])

chanelsUpdate = {"Natural Traffic":520, "News":600}
chanels.update(chanelsUpdate)

print(chanels)

print(chanels.pop("Email"))
print(chanels)