print("Enter a series of pizza toppings:")


chosen_toppings = []
topping_number = 1
is_active = True

prompt = "Enter " + str(topping_number) + ".\n"

while is_active:
    topping = input(prompt)
    if topping != 'quit':
        chosen_toppings.append(input(prompt))
    else:
        is_active = False

print(chosen_toppings)