print("ZADANIE 1")
initialCapital = 20000
percent = 0.03
maxTimeYears = 10

year = 0
capital = initialCapital

while year < maxTimeYears:
    capital = round(capital * (1+percent),2)
    # tenYearCapital = initialCapital + (capital*maxTimeYears)
    year = year + 1
    print("After", year, "year:", capital)
else:
    print("After 10 years:", capital-initialCapital)