#  Printing a number from 1 to 5 inclusive
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


#  Another method:

current_number = 1
formatted_numbers = ''

while current_number <= 5:
    formatted_numbers += str(current_number) + " "
    current_number += 1

print(formatted_numbers)

#  Using continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue #  returns to the start of the loop

    print(current_number)
