#  Initiate 3 persons which are 3 dictionaries:
person1 = {
    'first_name': 'patrick',
    'last_name': 'meyer',
    'age': 26,
    'city': 'aarhus'
    }

person2 = {
    'first_name': 'morten',
    'last_name': 'struckmann',
    'age': 25,
    'city': 'esbjerg'
    }

person3 = {
    'first_name': 'david',
    'last_name': 'lam',
    'age': 23,
    'city': 'køge'
    }

#  Put the 3 people into a list:
people = [person1, person2, person3]

#  Printing all their information:
for person_info in people:
    for key, value in person_info.items():
        print(str(key).title() + ": " + str(value).title())

    print() #  For making a format linebreak
