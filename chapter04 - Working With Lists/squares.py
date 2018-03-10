#  Filling a list with squares
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

#  Simple operations on list
print("Minimum value in list: " + str(min(squares)))
print("Maximum value in list: " + str(max(squares)))
print("The sum of the whole list: " + str(sum(squares)))

#  Another way to build the list:
squares= [value**2 for value in range(1, 11)]
print("New list: " + str(squares))