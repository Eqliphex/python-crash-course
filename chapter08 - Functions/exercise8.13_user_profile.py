def build_profile(first_name, last_name, **user_info):
    """Build a dictionary containing everything we know about a user

    Arguments:
        first_name (str) : first name of the user.
        last_name (str) : last name of the user.
        user_info (**kwargs) : additional key/value arguments in a dictionary.

    Return:
        user dictionary
    """
    profile = {'first_name': first_name, 'last_name': last_name}
    for key, value in user_info.items():
        profile[key] = value

    return profile


user_profile = build_profile('patrick', 'meyer',
                             location='aarhus',
                             field='computer science',
                             age=26)
print(user_profile)
