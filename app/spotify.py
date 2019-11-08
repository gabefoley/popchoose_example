from app import db
from spotify_config import sp
from app.models import Artist

def add_artists(artist_list):

    for name in artist_list:
        results = sp.search(q='artist:' + name, type='artist')

        items = results['artists']['items']
        try:
            if len(items) > 0:
                artist = items[0]

                query = Artist.query.filter_by(id=artist['id']).first()

                # If we already have this artist stored in the local database then just update the popularity and image
                if query:
                    print (artist['images'])
                    query.popularity = artist['popularity']
                    query.image = artist['images'][1]['url']

                # Otherwise create an entry for this artist
                else:
                    query = Artist(artist['id'], artist['name'], artist['popularity'], artist['images'][1]['url'])

                db.session.add(query)
                db.session.commit()

        except IndexError as e:
            print(f"Couldn't find an image for {artist['name']}")

