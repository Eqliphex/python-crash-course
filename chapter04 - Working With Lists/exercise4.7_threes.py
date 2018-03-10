#  One way of adding multiples to a list:
list_of_threes = []
for value in range(1, 31, 3):
    list_of_threes.append(value**2)
print(list_of_threes)

#  Another way of adding:
list_of_threes_two = [value**2 for value in range(1, 31, 3)]
print(list_of_threes_two)

