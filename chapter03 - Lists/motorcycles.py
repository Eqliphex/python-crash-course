#  Initializing a list:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#  Appending to a list:
motorcycles.append('ducati')
print(motorcycles)

#  Inserting an element into a list: (non-overwriting)
motorcycles.insert(0, 'harley')
print(motorcycles)

#  Removing an element from a list:
del motorcycles[1]
print(motorcycles)

#  popping an element from the list (last entry):
popped_element = motorcycles.pop()
print(motorcycles)
print(popped_element)

#  Popping from any position in the list:
popped_element = motorcycles.pop(0)
print("The first motorcycle I owned was a " + popped_element.title() + ".")

#  Removing an element by value:
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

