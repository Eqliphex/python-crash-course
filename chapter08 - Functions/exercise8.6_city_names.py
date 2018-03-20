def city_country(name, country):
    """Returns a formatted string with city name and country"""
    return name.title() + ", " + country.title()


print(city_country('copenhagen', 'denmark'))
print(city_country('tokyo', 'japan'))
print(city_country('berlin', 'germany'))