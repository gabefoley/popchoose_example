import pylast

# Last.fm API keys
LAST_FM_KEY = "8b0127a181610915579ace1075b9e7c1"  # this is a sample key
LAST_FM_SECRET = "a712cc96462a96c841c917391ee0a2f5"


network = pylast.LastFMNetwork(api_key=LAST_FM_KEY, api_secret=LAST_FM_SECRET)
