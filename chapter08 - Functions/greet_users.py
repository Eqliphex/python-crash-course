def greet_users(names):
    """Print a simple greeting to each user in the list.

    Args:
        names (list): List of names.
    """
    for name in names:
        message = "Hello, " + name.title() + "!"
        print(message)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)