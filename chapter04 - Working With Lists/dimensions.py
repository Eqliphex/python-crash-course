#  representation of a tuple. They are immutable
#  They are good if you have data that does not change through the life of the program
dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])

print("\nOriginal dimensions:")
#  looping through a tuple
for dimension in dimensions:
    print(dimension)

#  Assigning a new tuple to variable
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)