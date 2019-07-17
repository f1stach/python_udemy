from datetime import date


def days_new_years_eve(year=date.today().year, month=date.today().month, day=date.today().day):

    # date_today = date.today()

    date_today = date(year, month, day)
    # current_year = date_today.year

    # date_end_year = date(current_year, 12, 31)

    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today

    # print("There are", delta.days, "days left till New Year's Eve")

    return delta.days


print("There are", days_new_years_eve(), "left to new year's eve")
print("There are", days_new_years_eve(2019,1,1), "left to new year's eve")
print("There are", days_new_years_eve(2019,6,1), "left to new year's eve")


days_new_years_eve(2019,7,30)
days_new_years_eve(month=8, day=3, year=2019)
days_new_years_eve()
