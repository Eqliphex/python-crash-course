#  Passing an arbitrary number of arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make

    Arguments:
        size (int) : Size of the pizza
        toppings (tuple) : tuple of x number of pizzas
    """
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)