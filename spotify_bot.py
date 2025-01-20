import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Set your Spotify credentials
client_id = "daccc75eac95417bb1a7d6af713569ec"
client_secret = "f63aad051b0748f7b51de83f97aef31f"
redirect_uri = "http://localhost:8888/callback"

# Create the SpotifyOAuth object
sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri, scope="user-library-read user-modify-playback-state user-read-playback-state")

# Paste your authorization code here
auth_code = "AQCosjBuyhNx46S9BdKuPUc8wOoTzyptViJLXPcYSWMKLeGD_a5z9Ng-U4Gw4oKDK2adWa27a5tO22vqZIE6GrtCf40GAGU8fYjmRYAZ0vHyG_Ww_2LWVJr-_GOBAOA42-bvSo1vdZFfeZWHdJw6_PDhreAYFluZpwFNQ-kRoRdYY2UhboEQtJMMJ_nCoK6-RdFeqD_DaD9kkdbK6M6EremFpdQ9rGo6BcBclZ8C2rjp3M0C4PPFBd6ZFTjBrLy8II9Lg4WKHbwUJCc"

# Get the token using the authorization code
token_info = sp_oauth.get_access_token(auth_code)

# Initialize Spotipy with the token
sp = spotipy.Spotify(auth=token_info['access_token'])

# Device ID from your previous result
device_id = '193d3482d8fb5f2f3f5796606722f1d4b6bb5acb'  # Your device ID
# Playlist URI from the playlist link you provided
playlist_uri = 'spotify:playlist:4beauqcBlaUMTmtsIucXeP'  # Your playlist URI

# Now, you can interact with the Spotify API
def play_song():
    sp.start_playback(device_id=device_id, uris=[playlist_uri])

play_song()
