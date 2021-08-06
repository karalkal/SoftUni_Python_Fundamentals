# If entered year is OK it should not be printed, you search for the next one - that's the whole trick
year = int(input())
year += 1
year_in_str = str(year)
while len(year_in_str) != len(set(year_in_str)):
    year += 1
    year_in_str = str(year)
print(year)