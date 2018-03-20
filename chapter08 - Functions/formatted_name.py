def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name

    return full_name.title()


musician = get_formatted_name('patrick', 'meyer')
print(musician)


musician = get_formatted_name(first_name='patrick', last_name='wegener',
                              middle_name='meyer')
print(musician)

