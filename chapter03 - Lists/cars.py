#  Sorting a list:

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#  Reverse sorting list:
cars.sort(reverse=True)
print(cars)

#  Sorting temporary:
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the sorted reversed list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)

#  Printing in reverse (no sorting)
cars.reverse()
print("\n" + str(cars))

# Finding the length of the list:
print("Length is: " + str(len(cars)))