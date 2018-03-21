magicians = ['patrick', 'tobias', 'merlin', 'david']


def show_magicians(magicians):
    """Prints out magicians from a list

    Arguments:
        magicians (list): list with magicians
    """
    for magician in magicians:
        print(magician.title())


show_magicians(magicians)