favorite_numbers = {
    'ken': [55, 44],
    'patrick': [69, 88],
    'linda': [14, 55],
    'jacob': [66, 6]
    }

for person, numbers in favorite_numbers.items():
    print("\n" + str(person.title()) + " Likes the numbers:")
    for number in numbers:
        print("\t" + str(number))
