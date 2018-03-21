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
    for magician in magicians:
        magician += ' the Great'


show_magicians(magicians)
make_great(magicians[:])
show_magicians(magicians)