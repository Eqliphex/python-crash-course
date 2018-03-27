class Dog():
    """A Simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes.
        the name __init__ is to avoid conflict with custom method names.
        So whenever leading and tracing underscores, then it's pythons own
        methods. Is run every time a new instance of the object is created.

        Arguments:
            self (object) : Is necessary to give access to the object instances,
                attributes and methods.
            name (str) : Name of the dog.
            age (int) : age of the dog.
        """
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll(self):
        """Simulate rolling over in repsonse to a command."""
        print(self.name.title() + " rolled over!.")

my_dog = Dog('buller', 6)
your_dog = Dog('lucy', 3)


print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()