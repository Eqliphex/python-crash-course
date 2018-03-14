favorite_places = {
    'patrick': ['japan', 'greenland', 'iceland'],
    'morten': ['china', 'thailand', 'amsterdam'],
    'david': ['japan', 'amsterdam', 'america']
}

#  Using key/value pair to print:
for person, places in favorite_places.items():
    print("\n" + str(person.title()) + " likes to go to the following places:")
    for place in places:
        print("\t" + str(place.title()))
