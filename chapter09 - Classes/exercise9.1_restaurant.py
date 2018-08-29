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
        """Prints out the information of the restaurant"""
        print("Try the " + self.cuisine_type.title() + " cuisine at " +
              self.restaurant_name.title() + " today!")

    def open_restaurant(self):
        print("Restaurant is open!")


restaurant = Restaurant("peppitos", "italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
