year = int(input())
year += 1  #cannot be current year
thousands = year // 1000
hundreds = year // 100 % 10
tens = year // 10 % 10
units = year % 10
while thousands == hundreds or thousands == tens or thousands == units or \
        hundreds == tens or hundreds == units or tens == units:
    year += 1
    thousands = year // 1000 % 10
    hundreds = year // 100 % 10
    tens = year // 10 % 10
    units = year % 10
if thousands == 0:
    print(f"0{year}")
else:
    print(year)