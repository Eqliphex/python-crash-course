#  Parameters:
#       Is the abstract thing called 'username' in the function signature
#  Arguments:
#       The concrete string 'patrick' is an argument

#  So in this case, when we call the function greet_user,
#  the argument 'patrick' was passed to the function and saved in
#  the parameter 'username'


def greet_user(username):
    """Display a simple greeting""" #  Docstring
    print("Hello, " + username.title() + "!")


greet_user('patrick')
