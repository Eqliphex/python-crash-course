print("Enter a series of pizza toppings:")


chosen_toppings = []
topping_number = 1
is_active = True

while is_active:
    topping = input("Enter " + str(topping_number) + ". topping\n")
    if topping != 'quit':
        chosen_toppings.append(topping)
        topping_number += 1
    else:
        is_active = False

print(chosen_toppings)