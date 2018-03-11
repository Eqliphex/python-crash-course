numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ordinal_numbers = []
for number in numbers:
    if number == 1:
        ordinal_numbers.append(str(number) + "st")
    elif number == 2:
        ordinal_numbers.append(str(number) + "nd")
    elif number == 3:
        ordinal_numbers.append(str(number) + "rd")
    else:
        ordinal_numbers.append(str(number) + "th")

print(ordinal_numbers)

