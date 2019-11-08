from app.models import Artist

def test_new_artist():
    """
    GIVEN an Artist model
    WHEN a new Artst is created
    THEN check the attributes
    """
    artist = Artist('2', 'Black Flag', 55, 'www.url')
    assert artist.name == 'Black Flag'
    assert artist.popularity == 55
