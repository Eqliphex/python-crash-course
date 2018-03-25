def add_car(manufacturer, model, **additional_info):
    """Adds a cars information to a dictionary and returns it.

    Arguments:
        manufacturer (str) : manufacturer name.
        model (str) : model name.
        additional_info (kwarg) : dictionary of additional car information.

    Return:
        dict: A new dictionary with all the car's information.
    """
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in additional_info.items():
        car[key] = value

    return car


print(add_car('subaru', 'outback', color='blue', tow_package=True))


