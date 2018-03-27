class User():
    """Simple model of a user"""
    def __init__(self, first_name, last_name, age, mail):
        """Initializes the user

        Arguments:
            first_name (str) : users first name.
            last_name (str) : users last name.
            age (int): age of user.
            mail (str) : mail of the user.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.mail = mail

    def describe_user(self):
        """Prints a formatted summary of the user."""
        print("First name: " + self.first_name.title())
        print("Last name: " + self.last_name.title())
        print("Age: " + str(self.age))
        print("Mail: " + self.mail)

    def greet_user(self):
        print("Hello, " + self.first_name.title() +
              " " + self.last_name.title())


new_user = User("patrick", "meyer", 26, "tbt_paddik@hotmail.com")
new_user.greet_user()
new_user.describe_user()