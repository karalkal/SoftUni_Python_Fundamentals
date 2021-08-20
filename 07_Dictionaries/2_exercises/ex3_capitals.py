countries = [x for x in input(). split(", ")]
capitals = [y for y in input(). split(", ")]
dict_country_and_capital = {country: capital for (country, capital) in zip(countries, capitals)}
# print(dict_country_and_capital)

for country, capital in dict_country_and_capital.items():
    print(country, "->", capital)