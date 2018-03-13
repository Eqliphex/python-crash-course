favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

#  Looping through the keys of the dictionary
for name in favorite_languages.keys():
    print(name.title())

#  Is the same as:
for name in favorite_languages:
    print(name.title())

# Accessing a keys value in for-loop:
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("   Hi " + name.title() +
              ", I see your favorite language is " +
              name.title())

#  Finding if key exists:
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

#  Sorting keys:
for name in sorted(favorite_languages.keys()): # Sorts the keys before execution
    print(name.title() + ", thank you for taking the poll.")

#  Looping without keys (With duplicates):
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language)

#  Looping without keys (Without duplicates):
for language in set(favorite_languages.values()):
    print(language)