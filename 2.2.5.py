import datetime


date = datetime.date(*[int(x) for x in input().split()])
days = datetime.timedelta(int(input()))
new_date = date + days
print(f"{new_date.year} {new_date.month} {new_date.day}")
