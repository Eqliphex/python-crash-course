def make_album(album_artist, album_title, album_song_num=None):
    """Creates an album.

    Args:
        album_artist (str): Name of the artist.
        album_title (str): Title of the album.
        album_song_num (:obj:`str`, optional): The second parameter.
            Defaults to None.
    Returns:
        bool: The return value. True for success, False otherwise.
    """
    if album_song_num:
        return {'artist': album_artist, 'title': album_title,
                'song_num': album_song_num}
    else:
        return {'artist': album_artist, 'title': album_title}


def create_albums():
    """Enteres a loop for generating albums.

    Returns:
        dict: returns a dictionary with albums and artists
    """
    albums = []
    while True:
        print("Please enter album information")
        print("(type 'quit' for exiting program!)")

        artist = input("Album artist: ")
        if artist == 'quit':
            break

        title = input("Album title: ")
        if title == 'quit':
            break

        track_num = input("Album track numbers: (leave blank if unknown)")
        if track_num == 'quit':
            break

        albums.append(make_album(artist, title, track_num))

    return albums

print(create_albums())
