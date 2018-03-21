magicians = ['patrick', 'tobias', 'merlin', 'david']


def show_magicians(magicians):
    """Prints out magicians from a list

    Arguments:
        magicians (list): list with magicians
    """
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    """Appends 'the great' to the list items

    Arguements:
        magician (list): list with magicians

    Return:
        :returns a new list with updated names.
    """
    upgraded_magicians = []
    for magician in magicians:
        magician += ' the Great'
        upgraded_magicians.append(magician)

    return upgraded_magicians


show_magicians(magicians)
magicians = make_great(magicians)
show_magicians(magicians)