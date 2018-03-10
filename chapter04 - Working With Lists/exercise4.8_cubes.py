#  One way of adding multiples to a list:
list_of_cubes = []
for value in range(1, 11):
    list_of_cubes.append(value ** 3)
print(list_of_cubes)

#  Another way of adding with list comprehension:
list_of_cubes_two = [value ** 3 for value in range(1, 11)]
print(list_of_cubes_two)

