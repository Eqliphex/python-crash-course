def build_profile(first_name, last_name, **user_info):
    """Build a dictionary containing everything we know about a user

    Arguments:
        first_name (str) : first name of the user.
        last_name (str) : last name of the user.
        user_info (**kwargs) : additional key/value arguments

    Return:
        user dictionary
    """
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in user_info.items():
        profile[key] = value

    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
