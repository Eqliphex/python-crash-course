glossary = {
    'dictionary': 'a construct to hold key/value pairs',
    'for-loop': 'construct to iterate over the same code until terminated',
    'if-statement': 'allows the programmer to execute certain code',
    'print': 'method that allows us to print output through the console',
    'python': 'an awesome programming language',
    'items()': 'returnes a list of key/value pairs',
    'set(dictionary)': 'ensures that duplicates from the dictionary is not shown.',
    'keys()': 'returns all the keys in the dictionary.',
    'sorted(obj)': 'Sorts the passed object (ex. sorted(glossary.keys()))'

    }

for keys, values in glossary.items():
    print(keys + ":\n" +
          values + "\n")