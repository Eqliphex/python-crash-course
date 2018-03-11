available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'green peppers','extra cheese', 'meat']

if requested_toppings:  #  Returns True if at least one item is in the list.
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print("Adding " + requested_topping + ".")
        else:
            print("Sorry, we don't have " + requested_topping)

    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")