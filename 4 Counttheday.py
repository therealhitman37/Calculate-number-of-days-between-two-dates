from datetime import date

f_date = date(2021, 10, 28)

l_date = date(2022, 10, 17)

delta = l_date - f_date

print(delta.days)