import datetime
adesso = datetime.datetime.now()

print(f"The current date and time is: {adesso}")

year = lambda x: x.year

month = lambda x: x.month

oggi = lambda x: x.day

ora = lambda x: x.time()

print(f'The current year is: {year(adesso)}')
print(f'The current month is: {month(adesso)}')
print(f'Today is: {oggi(adesso)}')
print(f'It\'s: {ora(adesso)} o\'clock')