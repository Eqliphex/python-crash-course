class Restaurant:
    """Simple model of a restaurant. Is a slight update of exercise 9.1"""
    def __init__(self, restaurant_name, cuisine_type):
        """Constructor to the restaurant class

        Arguments:
            restaurant_name (str) : Name of the restaurant.
            cuisine_type (str) : Type of cuisine offered.
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbers_served = 0

    def describe_restaurant(self):
        """Prints out the information of the restaurant"""
        print("Try the " + self.cuisine_type.title() + " cuisine at " +
              self.restaurant_name.title() + " today!")

    def open_restaurant(self):
        """Prints the restaurant is open"""
        print("Restaurant is open!")

    def number_of_customers_served(self):
        """Prints the total number of customers served"""
        print("Total numbers of customers served: " + str(self.numbers_served))

    def set_numbers_served(self, amount):
        """
        Sets the amount of customers the restaurant har served.

        Arguments:
             amount (int) : amount of customers the restaurant has served.
        """
        self.numbers_served = amount


restaurant = Restaurant("Peppitos", "italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()

restaurant.set_numbers_served(30)
restaurant.number_of_customers_served()
