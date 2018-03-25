def order_sandwich(*toppings):
    """Prints a sandwich with its provided toppings

    Arguments:
        toppings (tuple) : list of toppings
    """
    print("\nSandwich will have the following toppings:")
    for topping in toppings:
        print(" -" + topping.title())


order_sandwich('bacon', 'eggs', 'tomatoes')
order_sandwich('salad', 'beef', 'mayo')