from app.models import Artist
import app.lastfm

def test_new_artist():
    """
    GIVEN an Artist model
    WHEN a new Artst is created
    THEN check the attributes
    """
    artist = Artist('2', 'Black Flag', 55, 'www.url')
    assert artist.name == 'Black Flag'
    assert artist.popularity == 55



def test_artist_list_size():
    """
    Check that getting the artist list from Last.fm returns the correct size
    :return:
    """

    artist_list = app.lastfm.get_artist_list(10)

    assert len(artist_list) == 10
