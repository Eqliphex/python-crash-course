rivers = {'nile': 'egypt', 'amazon': 'america', 'yellow river': 'china'}

for key, value in rivers.items():
    print("The " + key.title() + " runs through " + value.title())

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())