country_names = input().split(", ")
capitals = input().split(", ")
my_dict = {}

for country, capital in zip(country_names, capitals):
    my_dict[country] = capital

# my_dict = {country: capital for country, capital in zip(country_names, capitals)}
for country, capital in my_dict.items():
    print(f"{country} -> {capital}")


# countries = input().split(", ")
# capitals = input().split(", ")
# # countries_and_capitals = dict(zip(countries, capitals))
# # # countries_and_capitals = {countries[index]:capitals[index] for index in range(len(countries))}
# countries_and_capitals = {country: capital for country, capital in zip(countries, capitals)}
# for country, capital in countries_and_capitals.items():
#     print(f"{country} -> {capital}")