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

#  This is a infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(first_name=f_name, last_name=l_name)
    print("\nHello, " + formatted_name + "!")