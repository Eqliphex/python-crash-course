#  Initiate a dictionary of dictionaries:
cities = {
    'tokyo':  {
        'county': 'japan',
        'population': '13.000.000',
        'fact': 'is comprised of wards'
    },
    'copenhagen': {
        'county': 'denmark',
        'population': '750.000',
        'fact': 'has the little mermaid'
    },
    'amsterdam': {
        'county': 'holland',
        'population': '851.000',
        'fact': 'coffeeshops are a front'
    }
}

#  Print the content of the dictionary:
for city, city_facts in cities.items():
    print("\n" + str(city.title()))
    for key, value in city_facts.items():
        print("\t" + str(key).title() + ": " + str(value).title())
