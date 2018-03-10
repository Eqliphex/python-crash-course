#  One way writing odd numbers to list:
odd_numbers = [value for value in range(1, 20, 2)]
print(odd_numbers)

#  Another way of writing odd numbers to list:
odd_numbers_two = []
for value in range(1, 20, 2):
    odd_numbers_two.append(value)

print(odd_numbers_two)