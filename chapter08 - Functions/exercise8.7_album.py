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


print(make_album('snoop dogg', 'doggtown'))
print(make_album('eminem', 'encore'))
print(make_album('king crimson', 'in the court of the crimson king'))

print(make_album('tesseract', 'polaris', 12))
