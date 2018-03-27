class Restaurant():
    """Simple model of a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Constructor to the restaurant class

        Arguments:
            restaurant_name (str) : Name of the restaurant.
            cuisine_type (str) : Type of cuisine offered.
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Try the " + self.cuisine_type.title() + " cuisine at " +
              self.restaurant_name.title() + " today!")

    def open_restaurant(self):
        print("Restaurant is open!")


restaurant1 = Restaurant("peppitos", "italian")
restaurant2 = Restaurant("khawand", "italian")
restaurant3 = Restaurant("divan", "turkish")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()