import app.lastfm
import app.spotify


artist_list = app.lastfm.get_artist_list(10)

app.spotify.add_artists(artist_list)